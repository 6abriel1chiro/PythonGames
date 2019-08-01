import math
import random
import time
import numpy as np
#import functools
#import operator

print("calculate fast!")
time.sleep(2)
print("Guess the correct answer to keep playing!")
time.sleep(3)
print("3,2,1.. GO")
user_time=time.time()
score=0

while True:
    difficulty_set=2 # 2 numbers
    difficulty_progress=math.floor(score/10) #  +score == +difficulty
    overall_difficulty=difficulty_set + difficulty_progress
    number_list=[]
    for x in range(overall_difficulty):
        value=random.randint(1,9)
        number_list.append(value)

    #answer=functools.reduce(operator.mul,number_list,1)
    answer= np.prod(np.array(number_list))
    time.sleep(3)
    print("Solve: ", number_list)
    guess=int(input())
    if guess==answer:
        score=score + (1*overall_difficulty)
        continue
    else:
        print("Game Over, the answer was ", answer)
        passed_time= time.time()-user_time
        print("Final score:", score, "points, In:","{0:0.1f}".format(passed_time),"seconds")
        break
