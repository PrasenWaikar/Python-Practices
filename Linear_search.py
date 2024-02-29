list = [4, 6, 2, 8, 3, 1, 9]
key = 3
found = False
for i in range(len(list)):
    if list[i] == key:
        print("Element found at index position:", i)
        found = True
        break
if not found:
    print("Element not found in the list.")
