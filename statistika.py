da = [10,2,3,4,11,43,11,45,32,100]
print (da)
k = 6;
min = 0
for i in range (min,len(da),1):
    if da[min]>da[i]:
        min=i;

minimum = da[min]
print('nilai minimal: '+str(da[min]))

max = 0
for i in range (min,len(da),1):
    if da[max]<da[i]:
        max=i;

maksimum = da[max]
print('nilai maksimum: '+str(da[max]))


R = maksimum - minimum

print ('nilai Range: '+str(R))


for j in 
