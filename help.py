from time import sleep
import sys

stringer = 'koktokotakmsdj asjd!2022'

i = 0

print(stringer[i:i+4])
while(stringer[i:i + 4] != '2022'):
    print(stringer[i], end = '')
    i += 1
print("\nSOM TI HOVORIL")