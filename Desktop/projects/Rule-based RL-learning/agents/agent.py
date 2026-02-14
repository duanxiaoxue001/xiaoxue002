import random
from env.scheduling_env import SchedulingEnv
from agents.policy_network import PolicyNetwork
class RuleBasedAgent:
    """基于规则的智能体"""

    def select_operation_and_machine(self, ready_operations, computation_time_matrix, machines, operations,
                                     predecessors, schedule_records):
        result_list = []

        for op in ready_operations:
            if 1 <= op <= len(computation_time_matrix):
                machine_times = computation_time_matrix[op - 1]

                for machine_id, processing_time in machine_times.items():
                    # 获取所有前置操作的结束时间（若未调度，默认0）
                    predecessor_end_times = [
                        operations[prev_op - 1].end_time or 0
                        for prev_op in predecessors.get(op, [])
                    ]
                    predecessor_max_end = max(predecessor_end_times, default=0)

                    # 获取该机器的调度列表
                    schedule = [
                        (start, end) for (opid, mid, start, end) in schedule_records if mid == machine_id
                    ]
                    # print(schedule)
                    # 查找最早可调度时间（考虑插空）
                    start_time = get_earliest_start_time(schedule, processing_time, predecessor_max_end)
                    completion_time = start_time + processing_time

                    result_list.append((op, machine_id, completion_time, start_time))


        return result_list


    def select_operation(self, result_list, OR, ready_operations, original_communication_time_matrix, alpha=0.5, beta=0.5):
        """
        从就绪操作中选择最优操作：
        - OR 节点中的操作：随机选一个保留，其余路径删除
        - 初始操作（没有前置操作）：在这些里随机选一个（增加路径多样性）
        - 其他操作：结合到达顺序排名 + SPT 策略选择
        """

        if not result_list:
            return None
        flat_OR = [op for group in OR for op in group]

        # 检查是否存在 OR 节点操作在就绪操作中
        or_ops_in_ready = [op for op in ready_operations if op in flat_OR]
        if or_ops_in_ready:
            # 如果有 OR 节点操作，就随机选择一个保留，其他删除
            best_operation = random.choice(or_ops_in_ready)
            # 找到与这个 OR 操作并列的其他路径中的操作
            best_operation_index = best_operation - 1
            predecessor_ops = [i + 1 for i, row in enumerate(original_communication_time_matrix)
                               if row[best_operation_index] == 0]
            successor_ops = []
            for pred_op in predecessor_ops:
                for op in flat_OR:
                    if op != best_operation and original_communication_time_matrix[pred_op - 1][op - 1] == 0:
                        successor_ops.append(op)
            for op in successor_ops:
                if op in ready_operations:
                    ready_operations.remove(op)
                    # print(f"删除 OR 路径: {op}，保留: {best_operation}")

            return best_operation
        # 获取没有前置操作的起始操作
        start_ops = []
        for op in ready_operations:
            op_idx = op - 1
            has_predecessor = any(original_communication_time_matrix[i][op_idx] == 0 for i in
                                      range(len(original_communication_time_matrix)))
            if not has_predecessor:
                start_ops.append(op)

        if start_ops:
            return random.choice(start_ops)

        processing_times = {op: pt for op, _, pt, _ in result_list}
        max_processing_time = max(processing_times.values()) if processing_times else 1
        # 否则按原策略选择（SPT + 随机到达排名）
        operations = [op[0] for op in result_list]
        random.shuffle(operations)
        arrival_ranks = {op: rank + 1 for rank, op in enumerate(operations)}
        max_arrival_rank = max(arrival_ranks.values()) if arrival_ranks else 1
        # composite_ranks = []
        # for op, best_machine, processing_time, start_time in result_list:
        #     arrival_rank = arrival_ranks[op]
        #     #  归一化处理
        #     arrival_rank_norm = arrival_rank / max_arrival_rank
        #     # processing_time_norm = processing_time / max_processing_time
        #     processing_time_norm = max_processing_time / processing_time
        #     score = alpha* arrival_rank_norm + beta * processing_time_norm
        #     composite_ranks.append((op, best_machine, score))
        #
        # composite_ranks.sort(key=lambda x: x[2])
        # best_operation, _, _ = composite_ranks[0]
        composite_ranks = []

        # 预处理最大值
        max_arrival_rank = max(arrival_ranks.values())
        max_processing_score = max([max_processing_time / (p[2] + 1e-6) for p in result_list])

        for op, best_machine, processing_time, start_time in result_list:
            arrival_rank = arrival_ranks[op]

            arrival_rank_norm = arrival_rank / max_arrival_rank
            processing_time_norm = (max_processing_time / (processing_time + 1e-6)) / max_processing_score

            score = alpha * arrival_rank_norm + beta * processing_time_norm
            composite_ranks.append((op, best_machine, score))

        composite_ranks.sort(key=lambda x: x[2])
        best_operation, _, _ = composite_ranks[0]


        return best_operation

    def get_predecessors(self, communication_time_matrix):
        """
        根据通信时间矩阵获取每个操作的前置操作
        :param communication_time_matrix: 邻接矩阵，INF 代表无连接，0 代表连接的后续操作
        :return: 前置操作字典 {操作: [前置操作列表]}
        """
        num_operations = len(communication_time_matrix)
        predecessors = {i+1 : [] for i in range(num_operations)}

        for i in range(num_operations):  # i 是当前操作
            for j in range(num_operations):  # j 是可能的后续操作
                if communication_time_matrix[i][j] == 0:
                    predecessors[j+1].append(i+1)

        return predecessors

    def find_predecessor_op(self, communication_time_matrix, best_operation):
        """ 查找 best_operation 的前置操作 """
        for prev_op in range(len(communication_time_matrix)):
            if communication_time_matrix[prev_op][best_operation] == 0:  # 0 表示连通
                return prev_op
        return None



def get_earliest_start_time(schedule, processing_time, earliest_from=0):  # 在 schedule 中查找插入该操作的最早可行时间点
    time_slots = sorted(schedule, key=lambda x: x[0])
    last_end = 0

    for start, end in time_slots:
        gap_start = max(last_end, earliest_from)
        gap_end = start
        if gap_end - gap_start >= processing_time:
            return gap_start
        last_end = max(last_end, end)

    return max(last_end, earliest_from)




