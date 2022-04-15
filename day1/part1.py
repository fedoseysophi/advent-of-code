import re

input_string = 'input1.txt'

with open(input_string, 'r') as input_file:
    for line in input_file:

        open_p = re.findall(r'\(', line)
        close_p = re.findall(r'\)',line)

        open_p_count = len(open_p)
        close_p_count = len(close_p)

        floor = open_p_count - close_p_count
#        print("Santa, go to floor " + str(floor))

with open("output1.txt", "w") as f:
    print(floor, file = f)