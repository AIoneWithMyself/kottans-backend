import os.path

a = r'E:\GitPy\kottans-backend\file_system\counter.txt'

if os.path.isfile(a):
    f = open('counter.txt', 'r+')
    f.read()
    if f.read() is int:
        k = 0
        f.write('5')
        k = k + 1
        exit(0)
    else:
        exit(1)
    f.close()

else:
    f = open('counter.txt', 'w+')
    f.write('1')
    f.read()
    f.close()
    exit(0)
