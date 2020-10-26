n = (input("Input:"))
for i in n:
    a=(ord(i)+3-97)%26
    print(chr(a+97),end="")
    
