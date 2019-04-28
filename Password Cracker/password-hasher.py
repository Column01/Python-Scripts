import hashlib
password = '0'
h = hashlib.sha1(password.encode())
print(h.hexdigest())
