s = "abcabc"
count = [0]*3
for i in range(0,len(s)):
	count[ord(s[i])-97]+=1

mul=1
mod = 1000000007
for i in range(0,len(count)):
	mul*=count[i]
	mul = mul%mod

if(mul==0):
    print(0)
else:
    mul = mul-1
    print(mul)
        