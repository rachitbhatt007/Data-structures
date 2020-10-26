def bsearch(arr,key):
    f=0
    l=len(arr)
    mid=(f+l)//2
    c=0
    while(l>=f):
        c=c+1
        if(key==arr[mid]):
            return("Found",c)
            break
        elif(key<arr[mid]):
            l=mid-1
            mid=(f+l)//2
        else:
            f=mid+1
            mid=(f+l)//2
    else:
        return("notfound")
if __name__=="__main__":
    arr=[1,2,3,4,5,6,7,8,9,10]
    print(bsearch(arr,8))


