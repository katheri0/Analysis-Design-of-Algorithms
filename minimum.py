def min(arr):
    for i in (2,len(arr)-1):
        if arr[i] <= mine :
            x = arr[i]
            return x
    return -1
    
n=int(input("enter the size of the array:"))
arr= []
for i in range(n):
    element =  int(input(f"enter the elements in the array [{i}]:"))
    arr.append(element)
n=len(arr)
mine = arr[0]
val= min(arr)
if val!= -1:
    print("minmum value is ",val)
