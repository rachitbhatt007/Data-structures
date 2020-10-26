def breakar(arr):
    odd=0
    even=0
    for i in range(0,len(arr),2):
        if(i+1<len(arr)):
            odd=odd+arr[i+1]
        even=even+arr[i]
    if(odd>even):
        print(odd)
    else:
        print(even)        

if __name__=="__main__":
    arr1=[1,2,3,1]
    arr2=[2,7,9,3,1]
    breakar(arr1)
    breakar(arr2)
