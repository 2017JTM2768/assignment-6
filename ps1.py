from pip._vendor.distlib.compat import raw_input

###### this is the first .py file ###########

####### write your code here ##########

## Parity Checking

sample = raw_input("Sample Bits :")
check = 0;

for i in sample:
    if(i!="0" or i!="1"):
        break;
    else:
        if i=="1":
            check=check+1
        else:
            continue
if (check/2 == 0):
    print("sample"+"1")
else:
    print("sample"+"0")

## Bit Stuffing
temp = str(None)
output = str(None) 
for i in range(len(sample)):
    temp = temp+sample[i]
    output=output+sample[i]
    if (len(temp)<3):
        continue
    else:
        if(temp[len(temp)-3]+temp[len(temp)-2]+temp[len(temp)-1]=='010'):
            output=output+'0'
        
    
#adding 0101 at the end of sample

if ((sample[len(sample)-2]+sample[len(sample)-1])=='01'):
    output=output+'00101'
else:
    output=output+'0101'

print(output)
    



    
        
