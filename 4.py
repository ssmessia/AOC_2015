raw = 'bgvyzdsv'
import hashlib

for i in range(1000000):
    r = raw+str(i)
    result = hashlib.md5(r.encode())
    if result.hexdigest()[:5] == '00000':
        break
print(i)
for i in range(10000000):
    r = raw+str(i)
    result = hashlib.md5(r.encode())
    if result.hexdigest()[:6] == '000000':
        break
print(i)