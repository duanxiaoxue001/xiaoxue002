from env.scheduling_env import SchedulingEnv
from agents.agent import RuleBasedAgent
from agents.policy_network import PolicyNetwork
import torch
import torch.optim as optim
import os
import json
import csv
import statistics
import time

# 创建保存目录
save_root = r"D:\Reinforcement learning\Rule-based RL-learning\output_results"
experiment_name = "results"
save_base = os.path.join(save_root, experiment_name)
os.makedirs(save_base, exist_ok=True)
# 初始化结果存储列表
# all_schedules = []
# all_makespans = []
# all_chart =[]
# schedule_records = []  # 存储每个操作的调度信息
prev_makespan = None  # 记录前一轮 makespan
best_makespan = float('inf')
best_alpha_beta = None


INF = float('inf ')
inf = float('inf')
# 输入数据
datasets = [
{
        "name":"dataset11",
        "computation_time_matrix": [    {3: 35, 4: 29, 5: 36, 11: 31}, {1: 40, 3: 34, 5: 44, 10: 41, 15: 39}, {11: 15, 15: 13}, {2: 31, 6: 33, 7: 29, 10: 27, 14: 25},
        {6: 13, 12: 9, 13: 8, 14: 14}, {11: 28, 12: 29}, {2: 31, 4: 24, 10: 28, 12: 26, 14: 32}, {6: 34, 10: 33, 11: 30, 13: 29},
        {3: 41, 4: 37, 13: 40}, {1: 38, 4: 29, 5: 35, 8: 30, 9: 31}, {6: 48, 10: 50, 11: 44, 14: 41, 15: 47},
        {6: 26, 7: 32, 9: 38, 12: 29, 13: 30}, {6: 23, 10: 20, 13: 25, 14: 18, 15: 22}, {2: 14, 8: 11, 10: 17, 12:13},
        {3: 27, 5: 24, 13: 26}, {4: 20, 8: 19, 13: 14}, {2: 27, 3: 21, 4: 28, 7: 30, 14: 29}, {3: 39, 7: 34, 10: 40, 14: 35}],
        "communication_time_matrix": [   [INF,   0, INF, INF, INF, INF, INF, INF, INF,   0, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF,   0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF,   0, INF, INF,   0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF,   0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF,   0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF,   0, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF,   0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF,   0, INF, INF, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   0],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   0, INF, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   0, INF, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   0, INF, INF, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   0, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   0, INF, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   0, INF, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   0, INF],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,   0],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]
    ],
        "OR":   [(2, 3, 9, 10, 11, 12, 13), (4, 5, 6, 7, 8)]
    },
  


    # 可以继续添加更多数据集
]

for dataset in datasets:
    name = dataset['name']
    computation_time_matrix = dataset['computation_time_matrix']
    communication_time_matrix = dataset['communication_time_matrix']
    OR = dataset['OR']

    print(f"\n==== 正在运行 {name} ====")
    # 初始化环境和智能体
    env = SchedulingEnv(computation_time_matrix, communication_time_matrix, OR)
    agent = RuleBasedAgent()

    # Policy Network 初始化
    policy_net = PolicyNetwork()
    optimizer = optim.Adam(policy_net.parameters(), lr=0.01)

    # 超参数
    num_iterations = 50

    # 初始化结果存储列表
    all_schedules = []
    all_makespans = []
    all_chart = []

    max_time_seconds = 60  # 设置最大运行时间 (秒)
    start_time = time.time()
    iteration = 0

    for iteration in range(num_iterations):
    # while time.time() - start_time < max_time_seconds:
        print(f"\n==== 第 {iteration + 1} 次调度开始 ====")
        env = SchedulingEnv(computation_time_matrix, communication_time_matrix, OR)
        agent = RuleBasedAgent()
        env.reset()

        #构造当前状态（仅用 normalized iteration）
        normalized_iter = iteration
        makespan_diff = 0.0 if prev_makespan is None else 0.0  # 暂时不能算，先设为0
        state = torch.tensor([[normalized_iter, makespan_diff]], dtype=torch.float32)

        # 策略网络采样
        logits = policy_net(state)  # shape: [1, 2]
        params = torch.nn.functional.softplus(logits[0])  # shape: [2], 保证为正数
        dirichlet = torch.distributions.Dirichlet(params)

        if best_alpha_beta is not None:
            alpha, beta = best_alpha_beta[0], best_alpha_beta[1]
            log_prob = None  # 不更新网络时无需 log_prob
            print("使用保存的最优 alpha 和 beta")
        else:
            alpha_beta = dirichlet.sample()
            alpha, beta = alpha_beta[0], alpha_beta[1]
            log_prob = dirichlet.log_prob(alpha_beta)

        print(f"alpha = {alpha.item():.3f}, beta = {beta.item():.3f}")

        # 用于运行记录
        while not env.is_done():
            ready_operations = env.ready_operations
            if ready_operations:
                predecessors = agent.get_predecessors(communication_time_matrix)
                result_list = agent.select_operation_and_machine(
                    ready_operations,
                    env.computation_time_matrix,
                    env.machines,
                    env.operations,
                    predecessors,
                    env.schedule_records,
                )

                if result_list:
                    best_operation = agent.select_operation(
                        result_list,
                        env.OR,
                        env.ready_operations,
                        env.original_communication_time_matrix,
                        alpha=alpha,
                        beta=beta
                    )
                    candidates = [(op, machine, ctime, stime) for op, machine, ctime, stime in result_list if op == best_operation]
                    # print(candidates)
                    best_machine_id, best_completion_time, best_start_time = min(candidates, key=lambda x: x[2])[1:]

                    env.schedule_records.append((best_operation, best_machine_id, best_start_time, best_completion_time))
                    env.step(best_operation, best_machine_id)

        # 调度完成，计算 reward
        total_time = env.get_total_time()
        reward = -total_time

        # 更新 makespan 差异并重新构造状态
        if prev_makespan is not None:
            makespan_diff = (prev_makespan - total_time) / prev_makespan
        else:
            makespan_diff = 0.0
        prev_makespan = total_time

        state = torch.tensor([[normalized_iter, makespan_diff]], dtype=torch.float32)
        logits = policy_net(state)
        params = torch.nn.functional.softplus(logits[0])  # shape: [2]
        dirichlet = torch.distributions.Dirichlet(params)


        if total_time < best_makespan:
            best_makespan = total_time
            best_alpha_beta = torch.tensor([alpha, beta])
        else:
            log_prob = dirichlet.log_prob(torch.tensor([alpha, beta]))
            loss = -reward * log_prob
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()


        # 输出结果
        schedule = env.get_schedule()
        total_time = env.get_total_time()
        print(f"第 {iteration + 1} 次调度完成，总加工时间（Makespan）: {total_time}")
        print(schedule)
        all_schedules.append(schedule)
        all_makespans.append(total_time)
        all_chart.append(env.over_schedule)
        iteration += 1  # 更新迭代计数

        # === 保存结果 ===
    dataset_name = name.replace(" ", "_")
    save_dir = os.path.join(save_base, dataset_name)
    os.makedirs(save_dir, exist_ok=True)

    with open(os.path.join(save_dir, "schedules.csv"), "w", encoding="utf-8", newline='') as f_csv:
        writer = csv.writer(f_csv)
        writer.writerow(["Iteration", "schedules"])
        for i, schedule in enumerate(all_schedules, 1):
            writer.writerow([i, schedule])

    with open(os.path.join(save_dir, "summary.csv"), "w", newline='', encoding="utf-8") as f_csv:
        writer = csv.writer(f_csv)
        writer.writerow(["Iteration", "Makespan"])
        for i, time in enumerate(all_makespans, 1):
            writer.writerow([i, time])

    with open(os.path.join(save_dir, "over_schedule.csv"), "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Iteration", "over_schedule"])
        for i, chart in enumerate(all_chart, start=1):
            chart_str = json.dumps(chart, ensure_ascii=False)
            writer.writerow([i, chart_str])

    # === 分析结果 ===
    min_time = min(all_makespans)
    best_iter = all_makespans.index(min_time) + 1
    best_schedule = all_schedules[best_iter - 1]
    best_chart = all_chart[best_iter - 1]
    #
    # max_time = max(all_makespans)
    # bad_iter = all_makespans.index(max_time) + 1
    # bad_schedule = all_schedules[bad_iter - 1]

    std_dev = statistics.stdev(all_makespans)

    print(f"\n==== 结果 for {name} ====")
    print(f"标准差: {std_dev:.2f}")
    print(f"最优调度轮次: {best_iter}")
    print(f"最短总加工时间: {min_time}")
    print(f"最优调度结果: {best_schedule}")
    # env.plot_gantt_chart(schedule=best_chart, title=f"Gantt Chart - {name} - Best Iteration {best_iter}")



