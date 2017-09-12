###### this is the first .py file ###########

####### write your code here ##########

## Parity Checking

sample = input("Sample Bits :")
check = 0;

for i in sample
	if(i!="0" || i!="1"):
		break;
	else:
		if i="1":
			check=check+1
		else:
			continue
if (check/2 == 0)
	print("sample"+"1")
else
	print("sample"+"0")

## Bit Stuffing
temp = None
count = 0
output = None 
for i in sample:
	temp = temp+i
	count = count+1
	if (count==3 and temp = "010"):
		output = output+temp+'0'
		temp=None
		count = 0
		i=i-2 	#going back two spaces in the sample
		continue
	else:
		continue

#adding 0101 at the end of sample

length = len(sample)
lasttwo = None
for j in sample range(length-2,length):
	lasttwo=lasttwo+j
	if(lasttwo=="10"):
		output = output+'00101'	#frame ends in 01, a 0 would be stuffed after the 1st 0 in the actual terminating string 0101.
	else:
		output = output+"0101"

print('output')
	



	
		
		

