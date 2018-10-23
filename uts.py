A = [[1,2,3,4],[4,3,2,1]]
B = [1,2,9,10]
for i in range (len(B)):
    for j in range (len(A)):
        for k in range (len(A[0])):
            if B[i] == A[j][k]:
                jawab ='angka ',B[i],' ditemukan pada baris ',j,' kolom ',k
                print(jawab)
                indeksDitemukan=i
    if (i != indeksDitemukan ):
        jawab='angka ', B[i],' tidak ditemukan'
        print(jawab)