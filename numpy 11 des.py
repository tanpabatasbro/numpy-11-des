import numpy as np

mxa = [12,64,37,58,90]
mxb = [31,95,40,26,87]

print(f"Array A = {mxa}")
print(f"Array B = {mxb}")

nmxa = np.array(mxa)
nmxb = np.array(mxb)

hasil = nmxb / nmxa ** 2

print(hasil)
