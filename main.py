def getArray():
    size=int(input("Enter the size of ur array : "))
    array = []
    for i in range(size):
        array.append(int(input(f"enter the value of index[{i}] : ")))
    return array
def mergeSort(array):
    if len(array)>1:
        middle =(len(array)//2)
        left=array[:middle]
        rigth=array[middle:]
        mergeSort(left)
        mergeSort(rigth)
        merge(left,rigth,array)

def merge(left,rigth,array):
    i=j=k=0
    while (i<len(left) and j <len(rigth) ):
        if (left[i] <= rigth[j]):
            array[k] =left[i]
            i = i+1
        else:
            array[k]=rigth[j]
            j =j+1
        k=k+1
    while i<len(left):
        array[k]= left[i]
        k+=1
        i+=1
    while j<len(rigth):
        array[k]= rigth[j]
        k+=1
        j+=1
    
array=getArray()
mergeSort(array)
print(f"ur sorted array is : {array}")