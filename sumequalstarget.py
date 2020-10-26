def sumequalstarget(arr,s):
    i=0
    j=len(arr)-1
    for _ in range(len(arr)):
        if(arr[i]+arr[j]==s):
            print(arr[i],arr[j])
            break
        elif(arr[i]+arr[j]>s):
            j=j-1
        else:
            i=i+1

def dictsumequalstarget(arr,s):
    pass
    

if __name__=="__main__":
    arr=[1,2,3,4,5,6,7,8,9]
    sumequalstarget(arr,5)