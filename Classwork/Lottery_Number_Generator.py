# 3/13/2024
# Amanda M
# Lottery Number Generator

# I'll make a 7 digit lottery number program using array ~~random generator~~, and ~~loops to display the contents~~ of the array.
# array

import random
# random gen
gen_ = [ [],
         [] ]


class celeb_voice():
    print("Good evening and get ready for tonights lucky numbers!")
    
def rolls():
        i = 0
        LOT_ROLLS = 7
        while i < (LOT_ROLLS + 1):
            gen_ = [[] for j in range(2)]
            gen_[0] = [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)]
            gen_[1] = [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)]
            gen_.extend([0])
            gen_.extend([1])
            

# While loop to display the numbers
index = 0
while index < len(gen_):
    print(gen_[index])
    index += 1

celeb_voice()
rolls()
