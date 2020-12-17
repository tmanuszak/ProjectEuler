palindromeList = []
for i in range(100,1000):
    for j in range(100,1000):
        num = i*j
        temp = num
        rev = 0
        while (num > 0):
            dig = num % 10
            rev = rev * 10 + dig
            num = num // 10
        if (temp == rev):
            palindromeList.append(i*j)


# Python3 program to find maximum
# in arr[] of size n

# python function to find maximum
# in arr[] of size n
def largest(arr, n):
    # Initialize maximum element
    max = arr[0]

    # Traverse array elements from second
    # and compare every element with
    # current max
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max

n = len(palindromeList)
print(largest(palindromeList, n))