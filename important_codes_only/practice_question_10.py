def findGreatestElement(n):
    if n<0:
        return f"enter greater than 0"
    arr = [0]*n
    if n>=1:
        arr[1] = 1
    
    for i in range(2,n):
        if i%2==0:
            arr[i] = 2*i
        else:
            arr[i] = arr[i-1] + arr[i-2]
    
    maxi = max(arr)
    return arr,maxi        

n = int(input("enter a number"))
arr,maxi = findGreatestElement(n)
print(arr,maxi)
