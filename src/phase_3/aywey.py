def extract_number(lst):
    string = lst[0]  # Assuming the input list contains only one element
    number = ''

    for char in string:
        if char.isdigit():
            number += char

    return int(number)

# Test cases
input1 = ['[SI+789]']
input2 = ['[SI+8]']

output1 = extract_number(input1)
output2 = extract_number(input2)

print(output1)  # Output: 789
print(output2)  # Output: 8
