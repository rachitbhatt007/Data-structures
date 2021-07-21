def counttriplet(arr,s):
    c=0
    i=0
    k=len(arr)-1
    for i in range(len(arr)-3):
        j=i+1
        while(j<k):
            if(arr[i]+arr[j]+arr[k]==s):
                c=c+1
                print(arr[i],arr[j],arr[k])
                j=j+1
            elif(arr[i]+arr[j]+arr[k]<s):
                j=j+1
            else:
                k=k-1
    print(c)



if __name__=="__main__":
    arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    arr2=[1,3,4,5,7]
    counttriplet(arr2,12)
