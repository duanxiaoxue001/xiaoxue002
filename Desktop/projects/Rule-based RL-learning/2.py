# import pandas as pd
#
# file_path = r"D:\Reinforcement learning\Rule-based RL-learning\output_results\results-4\dataset2\summary.csv"
# # 读取CSV
# df = pd.read_csv(file_path)
#
# # 找出Makespan最小的行
# min_row = df.loc[df["Makespan"].idxmin()]
#
# print("最小Makespan对应的结果：")
# print(f"Iteration: {min_row['Iteration']}, Makespan: {min_row['Makespan']}")


import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

# # -----------------------------
# # 设置中文字体
# # -----------------------------
# # 方法1：rcParams 全局设置
# rcParams['font.sans-serif'] = ['SimHei']  # 黑体，支持中文
# rcParams['axes.unicode_minus'] = False    # 解决负号显示问题
# #
# # -----------------------------
# # 数据设置
# # -----------------------------
# jobs = np.arange(1, 11)       # 工序数量 1~10
# machines_list = [2, 3, 5]     # 典型机器数量
#
# plt.figure(figsize=(8, 5))
#
# # -----------------------------
# # 计算状态-动作对总量并绘图
# # -----------------------------
# for m in machines_list:
#     total_pairs = m ** jobs
#     plt.plot(jobs, total_pairs, marker='o', label=f'{m}台机器')
#
# # -----------------------------
# # 设置图形属性
# # -----------------------------
# plt.yscale('log')  # 对数坐标
# plt.xlabel('工序数量')
# plt.ylabel('状态-动作对总量（对数坐标）')
# plt.title('调度问题中状态-动作空间的指数增长示意图')
# plt.grid(True, which='both', ls='--', lw=0.5)
# plt.legend(title='机器数量')
#
# plt.tight_layout()
# plt.show()


