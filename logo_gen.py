import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim
import tensorflow as tf

class LogoEnvironment:
    """
    RL Environment for logo generation with intentionally punitive reward system.
    Note: The reward function is designed to heavily penalize:
    - Shapes far from center (strong symmetry requirement)
    - Non-brand colors
    - Excess complexity
    This creates a challenging optimization problem suitable for advanced RL agents.
    """
    def __init__(self, target_simplicity=3, brand_colors=[(255,0,0), (0,0,255)]):
        self.canvas = np.zeros((64, 64, 3))  # Small canvas → simplicity
        self.state = self.get_vector_representation()  # Vector state (see below)
        self.brand_colors = brand_colors
        self.target_simplicity = target_simplicity  # Max preferred shapes

    def reset(self):
        self.canvas = np.zeros((64, 64, 3))
        return self.get_vector_representation()

    def get_vector_representation(self):
        # REPRESENTS STATE AS SHAPE PARAMETERS (NOT PIXELS) → SCALABLE FOR LOGOS
        # Parameters like shape_type, center_x, center_y, radius, color
        return np.random.rand(10)  

    def step(self, action):
        # ACTION STRUCTURE: [shape_type (0-1), x (grid-8x8), y, size, color_idx]
        # LOGO CONSTRAINT: Shapes placed on 8x8 grid → alignment
        x_grid = action[1] * 8
        y_grid = action[2] * 8
        color = self.brand_colors[action[4]]  # Enforce brand colors

        # Draw shape (mock: just record parameters)
        self.state = np.append(self.state, [action[1], action[2], action[4]])

        reward = self._calculate_reward(action)
        done = len(self.state) // 3 >= self.target_simplicity  # Stop at N shapes
        return self.state, reward, done

    def _calculate_reward(self, action):
        """Punitive reward function (intentionally strict)"""
        simplicity = -0.5 * (len(self.state) // 3)  # Heavy penalty per shape
        symmetry = self._calculate_symmetry_score(action[1], action[2])  # Strict symmetry
        brand_compliance = 2 if action[4] in [0,1] else -1  # Strong color preference
        return simplicity + symmetry + brand_compliance

    def _calculate_symmetry_score(self, x, y):
        # Reward proximity to center (for demo I am taking the absolute centre of the canvas)
        center_x, center_y = 32, 32
        return -0.1 * (abs(x - center_x) + abs(y - center_y)) # higher reward if closer to the centre

class PolicyNetwork(tf.keras.Model):  # untrained neural network
    def __init__(self, num_actions):
        super().__init__()
        self.dense1 = tf.keras.layers.Dense(32, activation='relu')
        self.dense2 = tf.keras.layers.Dense(num_actions, activation='softmax')

    def call(self, state):
        x = self.dense1(state)
        return self.dense2(x)


if __name__ == "__main__":
    env = LogoEnvironment()
    policy = PolicyNetwork(num_actions=5)
    state = env.reset()

    print("Running punitive RL environment...")
    for step in range(10):
        action_probs = policy(tf.expand_dims(state, 0))
        action_idx = np.random.choice(5, p=action_probs.numpy()[0])
        action = [
            action_idx // 4,  # shape_type
            action_idx % 4,   # x_grid
            action_idx % 3,   # y_grid
            1,                # size
            action_idx % 2    # color_idx
        ]
        state, reward, done = env.step(action)
        print(f"Step {step}: Reward {reward:.2f}")
        if done:
            print("Reached maximum shape complexity!")
            break