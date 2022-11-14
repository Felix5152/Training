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


#Find the next perfect square!
import math
def find_next_square(sq):
    sq1 = math.sqrt(sq)
    if sq % sq1 == 0:  
        return ((sq1 + 1) ** 2)
    elif sq % sq1 != 0:
        return (-1)


#2 bullets in order to kill 1 dragon
def hero(bullets, dragons):
    if dragons * 2 <= bullets:
        return True
    else:
        return False


#Miliseconds in given hour
def past(h, m, s):
    h1 = 3600000 #Amount of miliseconds in certain unit 
    m1 = 60000
    s1 = 1000
    return(h * h1 + m * m1 + s * s1) #Counting total amount of miliseconds in certain hour.