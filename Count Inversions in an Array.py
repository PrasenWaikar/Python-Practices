def count_inversions(arr):
    def merge_count_split_inv(arr):
        if len(arr) < 2:
            return arr, 0
        mid = len(arr) // 2
        left, left_inv = merge_count_split_inv(arr[:mid])
        right, right_inv = merge_count_split_inv(arr[mid:])
        merged, split_inv = merge_and_count(left, right)
        return merged, left_inv + right_inv + split_inv

    def merge_and_count(left, right):
        i = j = count = 0
        merged = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                count += len(left) - i
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, count

    _, count = merge_count_split_inv(arr)
    return count

arr = [1, 20, 6, 4, 5]
print("Inversion count:", count_inversions(arr))
