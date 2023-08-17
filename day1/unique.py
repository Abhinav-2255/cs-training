def remove_duplicates(arr):
    unique_array = []
    for element in arr:
        if element not in unique_array:
            unique_array.append(element)
    return unique_array
 n=int(input("Enter the number of elements:"))
arr = []
for i in range(n):
    element = int(input("Enter element {i=1}:"))
    arr.append(element)
unique_array = remove_duplicates(arr)

print("Array after removing duplicates:",unique_array)