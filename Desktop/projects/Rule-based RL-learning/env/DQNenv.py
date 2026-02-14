import gym
from gym import spaces
import numpy as np
import random
import pickle
import os
INF = float('inf')

class FlexibleFlowShopEnv(gym.Env):
    def __init__(self, num_machines, num_operations, computation_time_matrix1,
                 communication_time_matrix1, in_OR1):
        super(FlexibleFlowShopEnv, self).__init__()
        self.num_machines = num_machines
        self.num_operations = num_operations
        self.processing_times = computation_time_matrix1
        self.in_OR1 = in_OR1
        self.threshold = float("inf")

        self.communication_time_matrix = np.copy(communication_time_matrix1)
        self.initial_communication_time_matrix = np.copy(communication_time_matrix1)
        self.original_communication_time_matrix = np.copy(communication_time_matrix1)

        self.original_ready_operations = []

        # 状态空间和动作空间不再固定，用 DQN 动态生成
        self.state_dim = self.num_operations * 2 + self.num_machines

        self.reset()

    # ------------------------
    # 1. 重置环境
    # ------------------------
    def reset(self):
        self.schedule = []
        self.machine_end_times = [0] * self.num_machines
        self.operation_end_times = [0] * self.num_operations
        self.machine_available_times = [0] * self.num_machines
        self.operation_times = {}
        self.communication_time_matrix = np.copy(self.initial_communication_time_matrix)

        communication_time_matrix1_T = np.transpose(self.communication_time_matrix)
        self.ready_operations = [i + 1 for i, col in enumerate(communication_time_matrix1_T)
                                 if all(col[j] == INF for j in range(len(col)) if j != i)]

        self.original_ready_operations = self.ready_operations.copy()
        return self.encode_state()

    # ------------------------
    # 2. 状态编码
    # ------------------------
    def encode_state(self):
        # 就绪操作 one-hot
        ready_ops = np.zeros(self.num_operations, dtype=np.float32)
        for op in self.ready_operations:
            ready_ops[op - 1] = 1.0

        # 机器可用时间归一化
        max_time = max(max(self.machine_end_times), 1.0)
        machine_times = np.array(self.machine_end_times, dtype=np.float32) / max_time

        # 操作完成情况
        completed_ops = np.zeros(self.num_operations, dtype=np.float32)
        for i, end_time in enumerate(self.operation_end_times):
            if end_time > 0:
                completed_ops[i] = 1.0

        # 拼接成最终状态向量
        state_vector = np.concatenate([ready_ops, machine_times, completed_ops])
        return state_vector

    # ------------------------
    # 3. 候选动作生成
    # ------------------------
    def get_candidate_actions(self):
        candidates = []
        for op in self.ready_operations:
            for m in self.processing_times[op - 1].keys():
                candidates.append((op, m))
        return candidates

    # ------------------------
    # 4. 动作索引映射
    # ------------------------
    def action_index_to_tuple(self, index):
        candidates = self.get_candidate_actions()
        if index < 0 or index >= len(candidates):
            raise ValueError(f"Invalid action index: {index}")
        return candidates[index]

    # ------------------------
    # 5. 随机动作
    # ------------------------
    def choose_action_randomly(self):
        candidates = self.get_candidate_actions()
        return candidates[np.random.choice(len(candidates))]

    # ------------------------
    # 6. 奖励函数
    # ------------------------
    def calculate_reward(self, operation, machine):
        max_processing_time = max(self.processing_times[operation - 1].values())
        current_processing_time = self.processing_times[operation - 1].get(machine, INF)
        reward = max_processing_time - current_processing_time
        return reward

    # ------------------------
    # 7. step函数
    # ------------------------
    def step(self, action):
        operation, machine = action
        machine_index = machine - 1
        operation_index = operation - 1

        computation_time = self.processing_times[operation_index][machine]

        # 获取前置操作完成时间
        prev_operations = [i + 1 for i, row in enumerate(self.original_communication_time_matrix)
                           if row[operation_index] == 0]
        executed_prev_operations = [op for op in prev_operations if self.operation_end_times[op - 1] > 0]
        if executed_prev_operations:
           # 如果存在已执行的前置操作，选择它们中结束时间的最大值
            prev_operation_end_time = max(self.operation_end_times[op - 1] for op in executed_prev_operations)
        else:
        # 如果没有已执行的前置操作，则使用机器的结束时间
            prev_operation_end_time = self.machine_end_times[machine_index]
        # 计算此操作在所选机器上的开始时间：应该是机器当前结束时间和已执行前置操作结束时间中的最大值
        start_time = max(self.machine_end_times[machine_index], prev_operation_end_time)
        end_time = start_time + computation_time

        # 更新结束时间
        self.machine_end_times[machine_index] = end_time
        self.operation_end_times[operation_index] = end_time
        self.machine_available_times[machine_index] = end_time
        self.operation_times[operation] = (start_time, end_time, machine)

        # 更新就绪操作
        if operation in self.ready_operations:
            self.ready_operations.remove(operation)
        self.schedule.append((operation, machine))
        self.update_ready_operations(operation)
        # print(self.ready_operations)

        done = len(self.ready_operations) == 0
        reward = self.calculate_reward(operation, machine)
        return self.encode_state(), reward, done, {}

    # ------------------------
    # 8. 总加工时间
    # ------------------------
    def get_total_time(self):
        return max(self.machine_end_times)

    # ------------------------
    # 9. 更新就绪操作
    # ------------------------
    def update_ready_operations(self, operation):
        next_operations = []
        for i in range(len(self.communication_time_matrix[operation - 1])):
            if self.communication_time_matrix[operation - 1][i] == 0:
                next_operations.append(i + 1)
                self.communication_time_matrix[operation - 1][i] = INF

        in_or_group = [op for op in next_operations if any(op in or_group for or_group in self.in_OR1)]

        if in_or_group:
            chosen_operations = []
            for or_group in self.in_OR1:
                group_ops = [op for op in in_or_group if op in or_group]
                if group_ops:
                    chosen_operations.append(np.random.choice(group_ops))
            # 添加不属于 OR 节点的操作到 chosen_operations 中
            non_or_ops = [op for op in next_operations if op not in in_or_group]
            chosen_operations.extend(non_or_ops)

            for op in chosen_operations:
                if all(self.machine_available_times[m - 1] >= 0 for m in self.processing_times[op - 1]):
                    if op not in self.ready_operations:
                        self.ready_operations.append(op)
        else:
            chosen_operations = next_operations
            for current_operation in chosen_operations:
                # 获取当前操作的所有前置操作
                predecessors = [j + 1 for j in range(len(self.communication_time_matrix))
                                if self.original_communication_time_matrix[j][current_operation - 1] != INF]

                # 检查前置操作中是否有属于 OR 节点的操作
                or_predecessors = [predecessor for predecessor in predecessors if
                                   any(predecessor in or_group for or_group in self.in_OR1)]
                non_or_predecessors = [predecessor for predecessor in predecessors if
                                       predecessor not in or_predecessors]

                # 只有在所有前置操作都已完成的情况下，才允许添加// 分为OR节点和非OR节点
                # 多条件判断
                if not non_or_predecessors:
                    # 只有 OR 节点的前置操作，任意一条完成
                    if any(predecessor in [op[0] for op in self.schedule] for predecessor in or_predecessors):
                        if all(self.machine_available_times[m - 1] >= 0 for m in
                               self.processing_times[current_operation - 1].keys()):
                            if current_operation not in self.ready_operations:
                                self.ready_operations.append(current_operation)
                elif not or_predecessors:
                    # 只有非 OR 节点的前置操作，所有需完成
                    if all(predecessor in [op[0] for op in self.schedule] for predecessor in non_or_predecessors):
                        if all(self.machine_available_times[m - 1] >= 0 for m in
                               self.processing_times[current_operation - 1].keys()):
                            if current_operation not in self.ready_operations:
                                self.ready_operations.append(current_operation)
                else:
                    # 同时有 OR 和非 OR 节点的前置操作，需满足两个条件
                    if (any(predecessor in [op[0] for op in self.schedule] for predecessor in or_predecessors) and
                            all(predecessor in [op[0] for op in self.schedule] for predecessor in non_or_predecessors)):
                        if all(self.machine_available_times[m - 1] >= 0 for m in
                               self.processing_times[current_operation - 1].keys()):
                            if current_operation not in self.ready_operations:
                                self.ready_operations.append(current_operation)
