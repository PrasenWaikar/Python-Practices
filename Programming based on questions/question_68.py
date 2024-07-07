#Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.
def binary_search(sorted_list, item):
    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == item:
            return mid
        elif sorted_list[mid] < item:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Example usage
if __name__ == "__main__":
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    item_to_search = 7

    index = binary_search(sorted_list, item_to_search)
    if index != -1:
        print(f"Element {item_to_search} is at index {index}.")
    else:
        print(f"Element {item_to_search} is not in the list.")
