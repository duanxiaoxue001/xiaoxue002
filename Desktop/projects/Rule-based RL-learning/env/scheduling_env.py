import heapq
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

INF = float('inf')

class Machine:
    """机器类：存储机器ID和最早可用时间"""
    def __init__(self, id):
        self.id = id
        self.next_available_time = 0  # 机器的最早可用时间

class Operation:
    """操作类：存储操作ID、可执行机器及加工时间、前序操作"""
    def __init__(self, id, processing_times, predecessors):
        self.id = id  # 操作ID
        self.processing_times = processing_times  # {机器ID: 加工时间}
        self.predecessors = predecessors  # 依赖的前序操作
        self.assigned_machine = None
        self.start_time = None
        self.end_time = None

    def is_ready(self, completed_operations):
        """检查是否所有前序操作都完成"""
        return all(pre in completed_operations for pre in self.predecessors)

class SchedulingEnv:
    """调度环境：执行调度过程"""
    def __init__(self, computation_time_matrix, communication_matrix, OR):
        self.num_operations = len(computation_time_matrix)
        self.communication_time_matrix = communication_matrix
        self.computation_time_matrix = computation_time_matrix
        self.operations = []
        self.OR= OR
        self.machines = {i: Machine(i) for i in range(1, 16)}  # 假设机器编号从1开始
        # 解析所有操作
        for i, machine_times in enumerate(computation_time_matrix, start=1):
            predecessors = [j+1 for j in range(self.num_operations) if communication_matrix[j][i-1] == 0]
            self.operations.append(Operation(i, machine_times, predecessors))

        self.completed_operations = set()
        communication_time_matrix_T = np.transpose(self.communication_time_matrix)
        self.ready_operations = [i + 1 for i, column in enumerate(communication_time_matrix_T) if
                                 all(column[j] == INF for j in range(len(column)) if j != i)]
        self.original_communication_time_matrix = np.copy(communication_matrix)
        self.over_schedule = []
        self.schedule = []
        self.total_time = None
        self. schedule_records = []  # 存储每个操作的调度信息

    def reset(self):
        self.schedule = []
        self.over_schedule = []
        self.completed_operations = set()
        self.schedule_records = []  # 存储每个操作的调度信息
        # 重置所有操作状态
        for operation in self.operations:
            operation.assigned_machine = None
            operation.start_time = None
            operation.end_time = None
        # 重置所有机器状态
        for machine in self.machines.values():
            machine.next_available_time = 0
        self.communication_time_matrix = np.copy(self.original_communication_time_matrix)
        communication_time_matrix1_T = np.transpose(self.communication_time_matrix)
        self.ready_operations = [i + 1 for i, column in enumerate(communication_time_matrix1_T) if
                                 all(column[j] == INF for j in range(len(column)) if j != i)]
        pass

    def step(self, operation_id, machine_id):
        """执行一个调度动作"""
        operation = self.operations[operation_id - 1]
        machine = self.machines[machine_id]
        # print(operation.predecessors)
        # 筛选已经调度的前置操作（end_time 不是 None）
        scheduled_predecessors = [
            predecessor for predecessor in operation.predecessors
            if self.operations[predecessor - 1].end_time is not None
        ]
        # print(scheduled_predecessors)
        # 计算前置操作完成时间（只考虑已调度的前置操作）
        predecessor_end_time = max(
            [self.operations[predecessor - 1].end_time for predecessor in scheduled_predecessors],
            default=0
        )
        # 计算最终开始时间：确保前置任务已完成
        start_time = max(machine.next_available_time, predecessor_end_time)
        end_time = start_time + operation.processing_times[machine.id]

        # 更新机器和操作状态
        machine.next_available_time = end_time
        operation.assigned_machine = machine.id
        operation.start_time = start_time
        operation.end_time = end_time
        self.completed_operations.add(operation.id)

        self.over_schedule.append((operation.id, machine.id, start_time, end_time))
        self.schedule.append((operation.id, machine.id))
        # hhh = self.schedule
        # print(hhh)
        # 从就绪操作列表中移除已执行的操作
        self.ready_operations.remove(operation_id)
        # hh = self.ready_operations
        # print(hh)
        # 更新就绪操作列表,添加与当前操作相连的下一个操作
        self.update_ready_operations(operation.id)


    def get_ready_operations(self):
        """获取当前可执行的操作（即没有前序依赖的操作）"""
        ready_operations = []
        for op_id in range(len(self.communication_time_matrix)):
            # 获取该操作的所有前序依赖
            predecessors = [self.communication_time_matrix[j][op_id] for j in range(len(self.communication_time_matrix))]
            # 如果所有前序都是 INF（无依赖），说明该操作是就绪操作
            if all(dep == INF for dep in predecessors):
                ready_operations.append(op_id + 1)  # 操作编号从1开始
        return ready_operations

    def update_ready_operations(self, operation):
        next_operations = []
        # 遍历通信时间矩阵，找到与当前操作相连的后续操作
        for i in range(len(self.communication_time_matrix[operation - 1])):
            if self.communication_time_matrix[operation - 1][i] == 0:
                next_operations.append(i + 1)
                self.communication_time_matrix[operation - 1][i] = INF  # 标记已处理

        # 遍历所有找到的后续操作，检查它的所有前置操作是否已经完成
        for next_op in next_operations:
            # 先判断是否属于任何一个 OR 节点组
            or_group = None
            for group in self.OR:
                if next_op in group:
                    or_group = group
                    break

            if or_group:  # 属于某个 OR 节点组
                # 该组中是否有任意一个操作，其前置操作已经完成
                at_least_one_predecessor_done = False
                for candidate in or_group:
                    for j in range(len(self.communication_time_matrix)):
                        if self.communication_time_matrix[j][candidate - 1] == INF:
                            at_least_one_predecessor_done = True
                            break
                    if at_least_one_predecessor_done:
                        break

                if at_least_one_predecessor_done and next_op not in self.ready_operations:
                    self.ready_operations.append(next_op)

            else:  # 非 OR 节点
                zero_rows = [i + 1 for i, row in enumerate(self.original_communication_time_matrix)
                             if row[next_op - 1] == 0]

                # 判断 zero_rows 中是否有属于 OR 节点的（因为它的前置是 OR）
                in_or = False
                for group in self.OR:
                    if any(z in group for z in zero_rows):
                        in_or = True
                        break

                if in_or:
                    at_least_one_predecessor = any(
                        self.communication_time_matrix[j][next_op - 1] == INF
                        for j in range(len(self.communication_time_matrix))
                    )
                    if at_least_one_predecessor and next_op not in self.ready_operations:
                        self.ready_operations.append(next_op)
                else:
                    all_predecessors_done = all(
                        self.communication_time_matrix[j][next_op - 1] == INF
                        for j in range(len(self.communication_time_matrix))
                    )
                    if all_predecessors_done and next_op not in self.ready_operations:
                        self.ready_operations.append(next_op)

        # print("当前 ready_operations:", self.ready_operations)

    def is_done(self):
        """检查是否所有操作都已完成"""
        return len(self.ready_operations) == 0

    def get_schedule(self):
        """返回当前调度计划"""
        return self.schedule

    def get_total_time(self):
        """计算所有机器的最终完成时间，并返回最大完成时间（Makespan）"""
        machine_completion_times = {}
        # 遍历调度记录，计算每台机器的完成时间
        for operation_id, machine_id, start_time, end_time in self.over_schedule:
            if machine_id not in machine_completion_times:
                    machine_completion_times[machine_id] = end_time
            else:
                machine_completion_times[machine_id] = max(machine_completion_times[machine_id], end_time)

        # 计算总执行时间（Makespan）
        self.total_time = max(machine_completion_times.values(), default=0)

        return self.total_time

    def plot_gantt_chart(self, schedule=None, title="Gantt Chart"):
        """绘制甘特图，展示每个操作的执行时间和机器"""
        if schedule is None:
            schedule = self.over_schedule  # 如果没有传入，就用当前环境中的 over_schedule

        fig, ax = plt.subplots(figsize=(12, 6))

        colors = {}  # 存储不同机器的颜色
        machine_labels = set()  # 机器编号集合

        # 遍历调度结果
        for operation_id, machine_id, start_time, end_time in schedule:
            if machine_id not in colors:
                colors[machine_id] = plt.cm.Paired(len(colors) % 12)  # 颜色映射

            machine_labels.add(machine_id)  # 记录机器编号
            ax.barh(y=machine_id, width=end_time - start_time, left=start_time,
                    height=0.6, color=colors[machine_id], edgecolor='black', label=f"Machine {machine_id}")

            # 在任务条上标注操作ID
            ax.text(start_time + (end_time - start_time) / 2, machine_id, f"O{operation_id}",
                    va='center', ha='center', fontsize=10, color='black', fontweight='bold')

        # 设置坐标轴
        ax.set_yticks(sorted(machine_labels))
        ax.set_yticklabels([f"Machine {m}" for m in sorted(machine_labels)])
        ax.set_xlabel("Time")
        ax.set_ylabel("Machines")
        ax.set_title(title)

        # 添加图例
        handles = [mpatches.Patch(color=colors[m], label=f"Machine {m}") for m in colors]
        ax.legend(handles=handles, loc='upper right')

        plt.grid(axis='x', linestyle='--', alpha=0.7)
        plt.show()



