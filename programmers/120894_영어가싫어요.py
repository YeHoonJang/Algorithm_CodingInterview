def solution(numbers):
    numbers_dict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

    word = ""
    digit = ""
    for char in numbers:
        word += char
        if word in numbers_dict.keys():
            digit += str(numbers_dict[word])
            word = ""
    return int(digit)


# most voted solution
def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))

    return int(numbers)