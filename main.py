import random

import game_data
from game_data import data
import game_logo
class HighLow:
    def __init__(self):
        self.data=game_data.data
        self.logo=game_logo.logo
        self.vs=game_logo.vs
        self.score=0
    def display(self):
        print(data)
        print(self.vs)
        print(self.logo)
    def genOpponents(self):
        rand=random.choice(self.data)
        idx=self.data.index(rand)
        return idx
    def pop(self,index):
        self.data.pop(index)
        return
    def mainplay(self):
        pass

    def main(self):
       play1=self.genOpponents()
       play2=self.genOpponents()
       print(play1,play2)
       while(True):
            print(f"Compare A: {self.data[play1]['name']}, a {self.data[play1]['description']}, from {self.data[play1]['country']}\n")
            print(self.vs)
            print(f"Compare B: {self.data[play2]['name']}, a {self.data[play2]['description']}, from {self.data[play2]['country']}\n")
            inp=input("Who has more followers ( A or B)\n")
            if inp=="A":
                if self.data[play1]['follower_count'] > self.data[play2]['follower_count']:
                    self.score+=1
                    self.pop(play2)
                    play2=self.genOpponents()
                    print(play2)
                    continue
                else:
                    print("Wrong Guess !!!!\n")
                    print(f"Total Score: {self.score}")
                    self.score=0
                    break


            elif inp=="B":
                if self.data[play1]['follower_count'] < self.data[play2]['follower_count']:
                    self.score+=1
                    self.pop(play1)
                    play1=self.genOpponents()
                    print(play1)
                    continue
                else:
                    print("Wrong Guess !!!!\n")
                    print(f"Total Score: {self.score}")
                    self.score=0
                    break
       inpp = input("Do you want to play again ( y / n)\n")
       if inpp == "y":
           self.main()
       else:
           exit()


if __name__=="__main__":
    game=HighLow()
    game.main()