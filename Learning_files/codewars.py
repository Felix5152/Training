#Average grades from codewars.


def get_grade(s1, s2, s3):
    average = (s1 + s2 + s3) / 3
    if average <= 100 and average >= 90:
        return('A')
    if average < 90 and average >= 80:
        return('B')
    if average < 80 and average >= 70:
        return('C')
    if average < 70 and average >= 60:
        return('D')
    if average < 60 and average >= 0:
        return('F')


#Banjo
def are_you_playing_banjo(name):
    # Implement me!
    if name[0].lower() == 'r':
        return(f"{name} plays banjo")
    else:
        return(f"{name} does not play banjo")

#DNA to RNA conversion
def dna_to_rna(dna):
    return dna.replace('T', 'U')


#Summation of next numbers
def summation(num):
    return (num * (num + 1) // 2)


#Multiplay of numbers in list
def grow(arr):
    total = 1
    for num in arr:
        total *= num
    return(total)