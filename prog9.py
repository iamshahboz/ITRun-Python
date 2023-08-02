
# my_list = ["1202","3400","390","1121","3350","1010"]
# to_int = []

# for number in my_list:
#     to_int.append(int(number))

# to_int = sorted(to_int)
# # print(to_int)
# to_str = []
# for i in to_int:
#     to_str.append(str(i))

# print(to_str)

import random
# the one who wins will get Alpen Gold and Sneakers

# names = ["Bobojon","Suman","Siyovush","Fayziddin","Alisher","Akai Umed","Zimfira","Umedjon","SuperMan"]
# print(random.choice(names))

# # my_random = random.randint(10,250)
# # print(my_random)

# print(random.random())

names = ["Bobojon","Suman","Siyovush","Fayziddin","Alisher","Umed","Zimfira","Umedjon"]
print(random.choices(names,k=1))



