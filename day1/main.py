file1 = open('input.txt', 'r')
lines = file1.readlines()

def get_first_digit_from_line(line):
    res = ""
    for x in range(len(line)):
        if line[x].isdigit():
            res = line[x]
            break
        else:
            sliced_line = line[x:]
            if sliced_line.startswith("one"):
                res = "1"
                break
            elif sliced_line.startswith("two"):
                res = "2"
                break
            elif sliced_line.startswith("three"):
                res = "3"
                break
            elif sliced_line.startswith("four"):
                res = "4"
                break
            elif sliced_line.startswith("five"):
                res = "5"
                break
            elif sliced_line.startswith("six"):
                res = "6"
                break
            elif sliced_line.startswith("seven"):
                res = "7"
                break
            elif sliced_line.startswith("eight"):
                res = "8"
                break
            elif sliced_line.startswith("nine"):
                res = "9"
                break
    return res

def get_last_digit_from_line(line):
    res = ""
    for x in range(1, len(line)+1, 1):
        # print("val of x", x)
        if line[-1*x].isdigit():
            res= line[-1*x]
            break
        else:
            sliced_line = line[-1*x:]
            if sliced_line.startswith("one"):
                res = "1"
                break
            elif sliced_line.startswith("two"):
                res = "2"
                break
            elif sliced_line.startswith("three"):
                res = "3"
                break
            elif sliced_line.startswith("four"):
                res = "4"
                break
            elif sliced_line.startswith("five"):
                res = "5"
                break
            elif sliced_line.startswith("six"):
                res = "6"
                break
            elif sliced_line.startswith("seven"):
                res = "7"
                break
            elif sliced_line.startswith("eight"):
                res = "8"
                break
            elif sliced_line.startswith("nine"):
                res = "9"
                break
    return res

sum = 0
for line in lines:
    first_digit_str = get_first_digit_from_line(line)
    last_digit_str = get_last_digit_from_line(line)
    sum = sum + int(""+first_digit_str+last_digit_str)

print(sum)
