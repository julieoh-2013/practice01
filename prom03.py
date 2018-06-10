s = '/usr/local/bin/python'
l = s.split('/')

s1=""
for i,v in enumerate(l):
    if i==0:
        continue
    elif i == len(l)-1:
        s1 += "'"+ l[i] +"'"
    else:
        s1 += "'"+ l[i] +"',"
print(s1)
s2=""
s2= "'/"+'/'.join(l[1:4])+"','"+ str(l[4])+"'"
print(s2)
 