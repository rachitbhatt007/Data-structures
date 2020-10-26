def TPduplicate(arr):
    j=0
    for i in range(1,len(arr)):
        if(arr[i]!=arr[j]):
            arr[j+1]=arr[i]
            j=j+1
    print(arr)
    print(j+1)
    for i in range(0,j+1):
        print(arr[i], end=" ")
if __name__=="__main__":
    arr=[1,2,2,2,2,3,3,3,3,4,5,6,6,7,8]
    TPduplicate(arr)                        
            



