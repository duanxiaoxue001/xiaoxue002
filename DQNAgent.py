import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import random
from collections import deque

# 1. DQN 网络
class DQNNetwork(nn.Module):
    def __init__(self, state_dim, action_dim, hidden_dim=128):
        super(DQNNetwork, self).__init__()
        self.fc1 = nn.Linear(state_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, hidden_dim)
        self.fc3 = nn.Linear(hidden_dim, action_dim)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)


# 2. 经验回放池
class ReplayBuffer:
    def __init__(self, capacity=5000):
        self.buffer = deque(maxlen=capacity)

    def push(self, state, action, reward, next_state, done):
        self.buffer.append((state, action, reward, next_state, done))

    def sample(self, batch_size):
        batch = random.sample(self.buffer, batch_size)
        states, actions, rewards, next_states, dones = zip(*batch)
        return (
            torch.tensor(np.array(states), dtype=torch.float32),
            torch.tensor(actions, dtype=torch.int64),
            torch.tensor(rewards, dtype=torch.float32),
            torch.tensor(np.array(next_states), dtype=torch.float32),
            torch.tensor(dones, dtype=torch.float32)
        )

    def __len__(self):
        return len(self.buffer)


# 3. DQN 智能体
class DQNAgent:
    def __init__(self, env, hidden_dim=128, lr=1e-3, gamma=0.99,
                 exploration_rate=1.0, min_exploration=0.05, exploration_decay=0.995,
                 batch_size=64, target_update=10):
        self.env = env
        self.state_dim = env.num_operations * 2 + env.num_machines  # ready + completed + machine_times
        self.batch_size = batch_size
        self.gamma = gamma
        self.exploration_rate = exploration_rate
        self.min_exploration = min_exploration
        self.exploration_decay = exploration_decay
        self.target_update = target_update

        # 动作数量动态，由当前候选动作决定
        self.policy_net = None
        self.target_net = None

        # 初始化 replay buffer
        self.replay_buffer = ReplayBuffer()
        self.optimizer = None
        self.loss_fn = nn.MSELoss()

    def init_networks(self, action_dim):
        self.policy_net = DQNNetwork(self.state_dim, action_dim)
        self.target_net = DQNNetwork(self.state_dim, action_dim)
        self.target_net.load_state_dict(self.policy_net.state_dict())
        self.optimizer = optim.Adam(self.policy_net.parameters(), lr=1e-3)

    def choose_action(self, state):
        candidates = self.env.get_candidate_actions()
        action_dim = len(candidates)
        if self.policy_net is None or self.target_net is None:
            self.init_networks(action_dim)

        if np.random.rand() < self.exploration_rate:
            action_index = np.random.choice(action_dim)
        else:
            state_tensor = torch.tensor(state, dtype=torch.float32).unsqueeze(0)
            q_values = self.policy_net(state_tensor)
            action_index = torch.argmax(q_values).item()
            # 防止超出候选动作范围
            action_index = min(action_index, action_dim - 1)
        return action_index

    def learn(self):
        if len(self.replay_buffer) < self.batch_size:
            return

        states, actions, rewards, next_states, dones = self.replay_buffer.sample(self.batch_size)

        q_values = self.policy_net(states)
        next_q_values = self.target_net(next_states)

        actions = actions - 1
        actions = torch.clamp(actions, min=0, max=q_values.size(1) - 1)
        q_value = q_values.gather(1, actions.unsqueeze(1)).squeeze(1)
        next_q_value = rewards + self.gamma * (1 - dones) * next_q_values.max(1)[0]

        loss = self.loss_fn(q_value, next_q_value.detach())

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

    def update_target_network(self):
        self.target_net.load_state_dict(self.policy_net.state_dict())

    def update_exploration_rate(self):
        self.exploration_rate = max(self.min_exploration, self.exploration_rate * self.exploration_decay)









