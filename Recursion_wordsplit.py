def wordsplit(s,lit,output=None):
	if output==None:
		output=[]

	if(len(s)==0):
		return 0
	else:	
		for i in lit:
			
			if(s.startswith(i)):
				output.append(i)
				

		return wordsplit(s[len(i):],lit,output)
					


output=[]
wordsplit('themanran',['man','ran','the'],output)
print(output)
