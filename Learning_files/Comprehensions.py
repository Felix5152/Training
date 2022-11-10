#List comprehensions and for loop
input = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20]
y = []

for x in input:
    if x % 2 == 0:
        y.append(x)
print(y)

list_using_comp = [var**2 for var in range(1, 10)]
print(list_using_comp)


#Dictionary comprehensions
output_dictionary = {}

#Using for loop
for var in input:
    if var % 2 != 0:
        output_dictionary[var] = var**3
print(output_dictionary)

#Using dictionary comprehensions
dict_using_comp = {var:var ** 3 for var in input if var % 2 != 0}
print(dict_using_comp)


country = ['Poland', 'Germany', 'Spain', 'USA']
capital = ['Warsaw', 'Berlin', 'Madrit', 'Washington D.C']
country_capital_dict = {}

for (key, value) in zip(country, capital):
    country_capital_dict[key] = value

print(country_capital_dict)

country_capital_dict_comp = {key: value for (key, value) in zip(country, capital)}
print(country_capital_dict_comp)

  
output_set = set()
  
# Using loop for constructing output set
for var in input:
    if var % 2 == 0:
        output_set.add(var)
  
print(output_set)

set_using_comp = {var for var in input if var % 2 == 0}
print(set_using_comp)