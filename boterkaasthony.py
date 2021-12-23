import random
from bke import EvaluationAgent, start, can_win, MLAgent, is_winner, opponent, train, train_and_plot, load, save, validate, RandomAgent, plot_validation



class MyRandomAgent(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        return random.randint(1, 500)

my_random_agent = MyRandomAgent()
 
class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward

random.seed(1)
   
my_agent = MyAgent()
#train(my_agent, 3000)
#save(my_agent, 'MyAgent_3000')

train_and_plot(
    agent=my_agent,
    validation_agent=my_random_agent,
    iterations=50,
    trainings=100,
    validations=1000)

#my_agent = load('MyAgent_3000')


my_agent.learning = False
 
#start(player_x=my_agent)

validation_agent = RandomAgent()

validation_result = validate(agent_x=my_agent, agent_o=validation_agent, iterations=100)
 
#plot_validation(validation_result)


    
while True:
  choice = input("\n 1: speel met 2 spelers \n 2: speel tegen de computer (makkelijk) \n 3: speel tegen de computer (moeilijk) \n Kies wat je wilt spelen: \n")

  if choice == '1':
    start()

  if choice == '2':
    start(player_o=validation_agent)


  if choice == '3':
    start(player_o=my_agent)
   
