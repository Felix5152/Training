numbers = [1,2,3,4,5,6,7,8,9,5,5,5,5,5,5,5]
noduplicates = []
for number in numbers:
    if number not in noduplicates:
        noduplicates.append(number)
print(noduplicates)