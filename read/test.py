'''
f=open('test.txt','r')

for line in f:
    print(line,end='')
'''

f=open('test1.txt','rb+')
f.write(b'0123456789abcdef')
for line in f:
    print(line,end='')