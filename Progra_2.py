# 3/13/2024
# Amanda M
# Lottery Number Generator

# I'll make a 7 digit lottery number program using array, random generator,  and loops to display the contents of the array.
# array
gen_ = [ [0, 0, 0],
         [0, 0, 0, 0], ]

import random
# random gen 
LOT_ROLLS = 7
gen_[0][0] = random.randint(0, 9)
gen_[0][1] = random.randint(0, 9)
gen_[0][2] = random.randint(0, 9)
gen_[1][0] = random.randint(0, 9)
gen_[1][1] = random.randint(0, 9)
gen_[1][2] = random.randint(0, 9)
gen_[1][3] = random.randint(0, 9)


print(gen_)