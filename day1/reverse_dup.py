input_string = input("Enter a string: ")
reversed_string = input_string[::-1]
output_string = ""
for char in reversed_string:
    if char not in output_string:
        output_string += char
print(output_string)
