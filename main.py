import random
import gym
import numpy as np  

env = gym.make("CartPole-v1", render_mode="human")

episodes = 10

for episode in range(1, episodes + 1):
    state = env.reset()
    done = False
    score = 0
    while not done:
        action = random.choice([0, 1])
        obs, reward, terminated, truncated , info = env.step(action)
        done = terminated or truncated  
        score += reward
        env.render()

    print(f"episode {episode}, score: {score}")

env.close()
