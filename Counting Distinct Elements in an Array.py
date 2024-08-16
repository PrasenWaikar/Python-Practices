def count(arr, n):

   # Mark all array elements as not visited
    visited = [False for i in range(n)]
    count_dis=0

   # Traverse through array elements
   # and count frequencies
    for i in range(n):
     # Skip this element if already
     # processed
        if (visited[i] == True):
          continue

     # Count frequency
        for j in range(i + 1, n, 1):
            if (arr[i] == arr[j]):
                visited[j] = True
         
        count_dis = count_dis+1;
   
    print(count_dis)

# Driver Code
arr = [10, 30, 40, 20, 10, 20, 50, 10]
n = len(arr)
count(arr, n)