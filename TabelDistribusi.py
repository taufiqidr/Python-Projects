from prettytable import PrettyTable
from texttable import Texttable
import math
import time

x = [128, 63, 97,134,133,136,125,110,118,94,76,84,132,105,80,87,100,77,120,109,90,72,103,78,94,118,117,80,140,94]

sturgess = 1 + (3.3 *math.log10(len(x)))
k = math.ceil(sturgess) #6
x_min = min(x) #63
x_max = max (x) #140
R = x_max - x_min #77
i = math.ceil(R/k) #13

print ("Nilai minimum : ",x_min)
print ("Nilai maksimum : ",x_max)
print ('Nilai R : ',R)
print ('Nilai interval kelas : ',k)
print ('Nilai lebar interval : ',i)
print()

interval=[]
m=[]
f=[] 
fr=[]
fk=[]

#mencari interval
for q in range(0,k+1,1):
    interval.append(x_min + (q) *i)
    #63, 76, ..., 

#mencari median
for q in range(0,k,1):
    m.append(interval[q]+0.5*i)
    f.append(0) #inisialisasi frekuensi

#mencari frekuensi
for p in range (0,len(x),1):
    for q in range (0,k,1):
        if x[p] >= interval[q] and x[p] < interval[q+1]: #128 >= 63 and 128 < 76
        	f[q]+=1

#mencari frekuensi relatif
for q in range(0,k,1):
    fr.append (round(f[q]/len(x),3))

#mengisi nilai awal frekuensi ke frekuensi kumulatif
fk.append(f[0])

#mencari nilai frekuensi kumulatif
for q in range (1,k,1):
    fk.append(fk[q-1]+f[q])

#Mencari nilai rata-rata tidak dikelompokkan
def rata2():
	n=len(x)
	jumlah=0
	for i in range(0,n,1):
		jumlah+=x[i]
	mean=jumlah/n
	return mean

#Mencari nilai rata-rata dikelompokkan
def rata2_K():
	jumlah=0
	for i in range(0,k,1):
		jumlah+=m[i]*f[i]
	mean2=jumlah/fk[5]
	return mean2

#Mencari nilai variansi tidak dikelompokkan
def Variansi():
	n=len(x)
	jumlah=0
	for i in range(0,n):
		jumlah=jumlah+math.pow(x[i],2)
	variansi=math.sqrt((jumlah-n*math.pow(rata2(),2))/(n-1))
	return variansi

#Mencari nilai variansi dikelompokkan
def Variansi_K():
	jumlah=0
	for p in range(0,k):
		jumlah+=f[p]*math.pow(m[p],2)
	variansiK=math.sqrt((jumlah-fk[5]*math.pow(rata2_K(),2))/(fk[5]-1))
	return variansiK

def Tabel():
    pt=PrettyTable(['no.', 'Interval', 'm', 'f', 'fr', 'fk'])

    for baris in range(6):
    	pt.add_row([baris+1,str(interval[baris])+str(" - ")+str(interval[baris+1]),m[baris],f[baris],fr[baris],fk[baris]])
    return print(pt)

def Tabel2():
    Tt=Texttable()
    Tt.add_row(['no.', 'Interval', 'm', 'f', 'fr', 'fk'])
    for baris in range(6):
    	Tt.add_row([baris+1,str(interval[baris])+str(" - ")+str(interval[baris+1]),m[baris],f[baris],fr[baris],fk[baris]])
    return print(Tt.draw())

Tabel()
print()
Tabel2()

print("Rata-rata tidak dikelompokkan : ",round(rata2(),3))
print("Rata-rata dikelompokkan : ",round(rata2_K(),3))
print("Variansi data tidak dikelompokkan : ",round(Variansi(),3))
print("Variansi data dikelompokkan : ",round(Variansi_K(),3))


time.sleep(5000)