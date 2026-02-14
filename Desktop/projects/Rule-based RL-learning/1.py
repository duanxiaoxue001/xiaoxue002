import matplotlib.pyplot as plt
import numpy as np

# 问题编号
problems = np.arange(1, 11)

# 数据
iSARSA = [713.3, 583.0, 712.2, 584.4, 443.1, 349.5, 428.5, 482.5, 459.2, 551.8]
iDynaQ = [738.6, 575.2, 725.5, 578.0, 446.1, 503.6, 426.6, 483.3, 454.3, 509.0]
DQN = [600.1, 632.5, 754.0, 596.7, 445.5, 357.2, 432.8, 628.7, 457.3, 546.0]
RuleLearn = [658.3, 574.9, 710.4, 595.0, 438.6, 345.9, 425.8, 502.9, 451.7, 536.9]
SPT = [1654, 1614.8, 2089.8, 1863.0, 1132.1, 885.8, 1281.2, 1651.9, 1278.0, 1623.1]

# 操作数量（用于点大小）
operations = [273, 259, 262, 259, 228, 181, 183, 229, 211, 235]

# 设置点大小比例
size_scale = 0.5
point_sizes = [op * size_scale for op in operations]

# 创建图
plt.figure(figsize=(10,6))

# 画折线 + 点
plt.plot(problems, iSARSA, marker='o', label='iSARSA')
plt.scatter(problems, iSARSA, s=point_sizes, alpha=0.6)

plt.plot(problems, iDynaQ, marker='s', label='iDyna-Q')
plt.scatter(problems, iDynaQ, s=point_sizes, alpha=0.6)

plt.plot(problems, DQN, marker='^', label='DQN')
plt.scatter(problems, DQN, s=point_sizes, alpha=0.6)

plt.plot(problems, RuleLearn, marker='D', label='Rule-Learn', linewidth=2.5, color='red')
plt.scatter(problems, RuleLearn, s=point_sizes, alpha=0.8, color='red')

plt.plot(problems, SPT, marker='x', label='SPT')
plt.scatter(problems, SPT, s=point_sizes, alpha=0.6)

# 添加标题和标签
# plt.title('Scheduling Performance Comparison')
plt.xlabel('Problem instance')
plt.ylabel('Makespan')
plt.xticks(problems)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()

plt.show()

# --- 可选：箱型图展示算法稳定性 ---
# plt.figure(figsize=(8,5))
# plt.boxplot([iSARSA, iDynaQ, DQN, RuleLearn, SPT], labels=['iSARSA','iDyna-Q','DQN','Rule-Learn','SPT'])
# plt.ylabel('Makespan')
# plt.title('Algorithm Stability Comparison (10 Problems)')
# plt.grid(True, linestyle='--', alpha=0.5)
# plt.tight_layout()
# plt.show()
data = [iSARSA, iDynaQ, DQN, RuleLearn, SPT]
labels = ['iSARSA','iDyna-Q','DQN','Rule-Learn','SPT']

# 箱型图颜色
colors = ['lightgray', 'silver', 'darkgray', 'red', 'lightgray']

plt.figure(figsize=(8,5))
box = plt.boxplot(data, labels=labels, patch_artist=True)

# 设置每个箱体颜色
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# 中位数线加粗
for median in box['medians']:
    median.set(color='black', linewidth=2)

# 须和帽子颜色
for whisker in box['whiskers']:
    whisker.set(color='gray', linewidth=1)
for cap in box['caps']:
    cap.set(color='gray', linewidth=1)

# 异常值设置
for flier in box['fliers']:
    flier.set(marker='o', color='orange', alpha=0.5)

# 标注中位数数值
for i, d in enumerate(data):
    median = np.median(d)
    plt.text(i+1, median + 15, f'{median:.1f}', ha='center', color='black', fontweight='bold')

plt.ylabel('Makespan')
# plt.title('Algorithm Stability Comparison (10 Problems)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()




