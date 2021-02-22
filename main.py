import gym
import random
def main():
    actions_dict = {2: "UP", 3: "RIGHT", 4: "LEFT", 5: "DOWN"}
    env = gym.make('MsPacman-v0')
    env.reset()
    total_reward = 0
    for i in range(1000):
        env.render()
        #action = env.action_space.sample()
        action = random.randint(2, 5)
        obs, reward, done, info = env.step(action) # take a random action
        print(i, " Action = ", actions_dict[action], " Reward = ", reward)
        total_reward += reward
    env.close()
    print("Total reward = ", total_reward)
if __name__ == "__main__":
    main()