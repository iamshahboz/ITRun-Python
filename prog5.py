# my_dictionary = {1: 12, 2: 14, 3: 16}
# my_dictionary[4] = 48
# print(my_dictionary)

# emails = {'bob@gmail.com': "Bob", 'andrew@gmail.com': 'Andrew', 'anna@bell': 'Anna'}

# print(emails.keys())   # this way we can get the keys
# print(emails.values())  # we can get the values this way

# population = {'Berlin': 402133, 'Cologne': 200133, 'Hamburg': 440980, 'Munich': 1002234}
# print(population['Hamburg'])




# translations= {'name': 'имя', 'city': 'город', 'pen': 'ручка', 'laptop': 'ноутбук'}
# word = input('Напишите слово:')
# if word == 'name':
#     print(f'Перевод данного слова будет {translations.get("name")}')

# else:
#     print('Bye')

# population = {'Berlin': 402133, 'Cologne': 200133, 'Hamburg': 440980, 'Munich': 1002234}
# print(population.get('Dushanbe','Not found'))

# we can change the value of the object this way 
# products = {'table':100, 'chair':20, 'pillow': 25, 'bed': 200}
# products['bed'] = 180
# print(products)

population = {'Berlin': 402133, 'Cologne': 200133, 'Hamburg': 440980, 'Munich': 1002234}
# for city in population:   # we get all the keys(cities)
#     print(city)
# print("---------")

# for people in population.values():
#     print(people)

count = 0
for people in population.values():
    count = count+ people   #count += people
print(count)

    












