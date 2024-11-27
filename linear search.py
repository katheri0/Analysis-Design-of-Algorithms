x= int(input("enter the number u are searchung for :"))
arr= [1,2,3,4,5,6,7]
def linearsearch(arr,x):
    for i in range(len(arr)):
        if x == arr[i]:
            return arr[i]
    return -1
    
val= linearsearch(arr,x)
if val != -1:
    print("\n your element ",val)
else:
    print("not fuond") 