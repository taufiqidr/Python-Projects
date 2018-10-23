import math
data = [ 128, 63, 97,134,133,136,125,110,118,94,76,84,132,105,80,87,100,77,120,109,90,72,103,78,94,118,117,80,140,94]
sturgess = 1 + (3.3 *math.log10(len(data)))
k = math.ceil(sturgess)
x_min = min(data)
x_max = max (data)
print ("nilai minimum: ",x_min)
print ("nilai maksimum: ",x_max)
R = x_max - x_min
print ('nilai R: ',R)
print ('nilai interval kelas: ',k)
i = math.ceil(R/k)
print('nilai lebar interval',i)

interval=[]
for q in range(1,k+2,1):
    print(q)
    print(i)
    interval.append(x_min + (q-1) *i)

print()
m=[]
f=[]
print(interval)


for q in range(0,k,1):
    m.append(interval[q]+0.5*i)
    f.append(0)
print()

print (m)
print()
print (f)

for p in range (1,len(data),1):
    for q in range (1,k,1):
        if data[p] >= interval[q] & data[p] < interval [q+1]:
            f.append(f[q]+1)
       

print(f)

    
        


