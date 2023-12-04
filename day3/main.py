import os

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
            print("found", current_number, "b/w cordinates (", i1, ",", j1, ") and (", i2, ",", j2 -1, ")")
            found_number = NumberInMatrix(int(current_number), i1, j1, i2, j2-1) 
            all_numbers.append(found_number)
            if (j >= len(input_matrix[i])):
                break
        j = j + 1   
    i = i + 1

sum = 0

def is_valid_position(i, j):
    return i>=0 and i<len(input_matrix) and j>=0 and j<len(input_matrix[i])

def is_symbol(i, j):
    return (not input_matrix[i][j].isalnum()) and input_matrix[i][j]!='.'
        

for number in all_numbers:
    i1 = number.start_x
    j1 = number.start_y
    i2 = number.end_x
    j2 = number.end_y

    found_symbol = False
    # iterate over top row
    curr_j = j1-1
    curr_i = i1-1
    while(curr_j<=j2+1):
        if(number.val == 114):
            print("searching for symbol at", curr_i, curr_j)
        if (is_valid_position(curr_i, curr_j) and is_symbol(curr_i, curr_j)):
            found_symbol = True
            break
        curr_j = curr_j + 1
    
    if found_symbol == False:
        curr_j = j1-1
        curr_i = i1+1
        while(curr_j<=j2+1):
            if(number.val == 114):
                print("searching for symbol at", curr_i, curr_j)
            if (is_valid_position(curr_i, curr_j) and is_symbol(curr_i, curr_j)):
                found_symbol = True
                break
            curr_j = curr_j + 1
    
    if found_symbol == False:
        found_symbol = is_valid_position(i1, j1-1) and is_symbol(i1, j1-1) 
    
    if found_symbol == False:
        found_symbol = is_valid_position(i1, j2+1) and is_symbol(i1, j2+1)
    print("found symbol result for:", number.val, found_symbol)
    if found_symbol == True:
        print("found symbol in vicintiy of ", number.val)
        sum = sum + number.val
    
print(sum)
    
    


