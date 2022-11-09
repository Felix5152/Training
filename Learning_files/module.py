def kgs_to_lbs(weight):
    return weight / 0.45


def lbs_to_kgs(weight):
    return weight * 0.45


def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum
    
