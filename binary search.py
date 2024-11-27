def RBS (arr, n , k,low,high) :
    mid =(low+high)//2
    if low>high:
        return -1
    if k == arr[mid]:
        return mid
    if k<arr[mid]:
        return RBS(arr, n ,k,low,mid-1)
    else:
        return RBS(arr, n ,k,mid+1,high)
        
n= int(input("enter the size of the array:"))
arr= []

low= 0
high=n-1
for i in range(n):
    element =  int(input(f"enter the elements in the array [{i}]:"))
    arr.append(element)
k= int(input("enter number to search in array: "))
index =RBS(arr,n,k,low,high)
if index!= -1:
    print("element found at index",index)
else:
    print("element not found in the array")
