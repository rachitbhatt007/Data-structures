def bsearch(arr,key):
    f=0
    l=len(arr)
    mid=(f+l)/2
    while(l>f):
        if(key==arr[mid]):
            return("Found")
        elif(key<arr[mid]):
            l=mid-1
        else:
            f=mid+1
    else:
        return("notfound")
if __name__="__main__":
    arr=[1,2,3,4,5,6,7,8,9,10]
    print(bsearch(arr,5))



