def getArray(size):
    array = []
    for i in range(size):
        array.append(int(input(f"enter the value of index[{i}] : ")))
    return array

def swap(array,i):
    tamp = array[i]
    array[i] = array[i +1]
    array[i +1] = tamp
    
def bubbleSort(array,size):
    for i in range(size):
        for j in range(size-i-1):
            if array[j]>array[j+1]:
                swap(array,j)
    
size = int(input("enter the size of ur array it should be positive number :"))
array = getArray(size)
bubbleSort(array,size)
print(f"ur sorted array is : {array}")