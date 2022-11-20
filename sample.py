def largest(arr, n):
 
    arr.sort()
 

    return arr[n-1]

arr = [10, 20, 30]
n = len(arr)
Ans = largest(arr, n)
print("Largest in given array ", Ans)