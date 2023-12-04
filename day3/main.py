import os
import sys

file1 = open(os.path.dirname(os.path.abspath(__file__)) + '/input.txt', 'r')
lines = file1.readlines()

sum = 0
input_matrix = []

for line in lines:
    line = line.strip()
    row = []
    for char in line:
        row.append(char)
    input_matrix.append(row)

class Gear():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class NumberInMatrix():
    def __init__(self, val, i1, j1, i2, j2) -> None:
        self.start_x = i1
        self.start_y = j1
        self.end_x = i2
        self.end_y = j2
        self.val = val
    
#find all numbers and store the coordinates of start and end number
# now search in the surrounding rectangle for any symbol which is not a dot(.)
all_numbers = []
all_gears = []

i = 0
while( i < len(input_matrix)):
    j = 0
    while (j < len(input_matrix[i])):
        if (input_matrix[i][j] == '*'):
            all_gears.append(Gear(i, j))
        j = j + 1
    i = i + 1

i = 0
while( i < len(input_matrix)):
    j = 0
    while (j < len(input_matrix[i])):
        # print("current j is", j)
        current_number = ""
        if input_matrix[i][j].isdigit():
            i1 = i
            j1 = j
            while(j<len(input_matrix[i]) and input_matrix[i][j].isdigit()):
                current_number = current_number + input_matrix[i][j]
                j = j + 1
                # print("\ti and j is", i, j)
            i2 = i
            j2 = j
            # print("came here with val, i2, j2", current_number, i2, j2)
            # print("found", current_number, "b/w cordinates (", i1, ",", j1, ") and (", i2, ",", j2 -1, ")")
            found_number = NumberInMatrix(int(current_number), i1, j1, i2, j2-1) 
            all_numbers.append(found_number)
            if (j >= len(input_matrix[i])):
                break
        j = j + 1   
    i = i + 1

sum = 0

def is_valid_position(i, j):
    return i>=0 and i<len(input_matrix) and j>=0 and j<len(input_matrix[i])

def is_number_adjacent_to(number, x, y):
    if (x== number.start_x):
        return y>=number.start_y and y<=number.end_y
    
    return False

def get_adjacency_of_gear(gear):
    res = []
    res.append({'x': gear.x-1, 'y': gear.y-1})
    res.append({'x':gear.x-1, 'y':gear.y})
    res.append({'x':gear.x-1, 'y':gear.y+1})
    res.append({'x':gear.x, 'y':gear.y-1})
    res.append({'x':gear.x, 'y':gear.y+1})
    res.append({'x':gear.x+1, 'y':gear.y-1})
    res.append({'x':gear.x+1, 'y':gear.y})
    res.append({'x':gear.x+1, 'y':gear.y+1})
    return res

for gear in all_gears:
    # print("gear is at", gear.x, gear.y)
    adjacency_of_gear = get_adjacency_of_gear(gear)
    # print(adjacency_of_gear)
    adjacent_numbers = []
    for pos in adjacency_of_gear:
        if is_valid_position(pos["x"], pos["y"]):
            for number in all_numbers:
                if (is_number_adjacent_to(number, pos["x"], pos["y"])):
                    # print("adjacent number found", number.val)
                    adjacent_numbers.append(number)
    product_of_numbers = 1
    # print("set of adjacent number", set(adjacent_numbers))
    gear_ratio_numbers = set(adjacent_numbers)
    if len(gear_ratio_numbers) == 2:
        for num in gear_ratio_numbers:
            product_of_numbers = product_of_numbers * num.val
        sum = sum + product_of_numbers

print(sum)
