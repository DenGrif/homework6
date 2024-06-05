# Работа со словарями:
my_dict = {'Denis': 1979, 'Alex': 1981, 'Anton': 1982,}
print(my_dict)
a = 'Год рождения:'
print(a, my_dict['Denis'])
my_dict['Viktor'] = 1977
print(a, my_dict['Viktor'])
my_dict.update({'Natasha': 1982, 'Sveta': 1984})
a = 'Not existing value:'
del my_dict['Anton']
print(a, my_dict.get('Anton'))
a = 'Modified dictionary:'
print(a, my_dict)

# Работа с множествами:
my_set = {1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 33, 33, 55,'aplle', (5, 4, 8)}
a = 'Set:'
print(a, my_set)
print(my_set.add(99),my_set.add(85))
print(my_set.discard(1))
a = 'Modified set:'
print(a, my_set)