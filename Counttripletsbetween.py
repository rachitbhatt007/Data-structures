def counttriplet(arr):
    c=0
    
    for i in range(len(arr)-2):
        k=len(arr)-1
        j=i+1
        while(j<k):
            if(arr[i]+arr[j]+arr[k]>=4 and arr[i]+arr[j]+arr[k]<=12):
                c=c+1
                print(arr[i],arr[j],arr[k])
                k=k-1
            if(arr[i]+arr[j]+arr[k]>12):
                k=k-1
            elif(arr[i]+arr[j]+arr[k]<4):
                j=j+1    
    print(c)



if __name__=="__main__":
    arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    arr2=[1,2,3,4,5,6,7,8]
    counttriplet(arr2)
