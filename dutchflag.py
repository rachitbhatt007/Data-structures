def dutch(arr):
    i=0
    j=len(arr)-1
    k=0
    while(k<=j):
        if(arr[k]==0):
            temp=arr[k]
            arr[k]=arr[i]
            arr[i]=temp
            k=k+1
            i=i+1
            
        elif(arr[k]==2):
            temp=arr[k]
            arr[k]=arr[j]
            arr[j]=temp
            j=j-1

        else:
            k=k+1    
        
    print(arr)       
if __name__=="__main__":
    arr=[1,1,2,2,0,0,0,1,2,0,1,2,2]
    arr2=[1,1,1,0,0,0,2,2,2,0]
    dutch(arr)            