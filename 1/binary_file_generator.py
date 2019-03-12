import os


#for _ in range(10):
with open('file.binary', 'wb') as f:
f.write(os.urandom(512 * 1024 * 1024))
