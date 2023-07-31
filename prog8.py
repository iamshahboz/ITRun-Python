### ordinary functions
# def my_func(x,y):
#     result = x**2
#     return result 
# print(my_func(7))

# print("----------")

# # ### this is lambda function
# my_calculation = lambda x,y: x*y
# print(my_calculation(7,5))


# this is ordinary method
# numbers = [2,0,-1,-9,13,44,101]
# positive_int = []
# negative_int =[]

# for i in numbers:
#     if i>0:
#         positive_int.append(i)
#     else:
#         negative_int.append(i)

# print(positive_int)
# print(negative_int)

# this is with list comprehension

numbers = [2,0,-1,-9,13,44,101]
negative_num = [i for i in numbers if i<0] 
positive_num = [i for i in numbers if i>0]
print(negative_num)
print(positive_num)