# f=  open('czy_input2.txt', 'r')
# n, m = map(int, f.readline().strip().split(' '))
# father_list = map(int, f.readline().strip().split(' '))
import sys

n, m = map(int, sys.stdin.readline().strip().split(' '))
father_list = map(int, sys.stdin.readline().strip().split(' '))

parent_list = [0 for _ in range(n)]
for idx, _f in enumerate(father_list):
    parent_list[idx+1] = _f


def isparent(a, b):
    while parent_list[a-1] != 0 and parent_list[a-1] !=  b:
        a = parent_list[a-1]
    if  parent_list[a-1] ==  b:
        return True

    else:
        return False

for _ in range(m):
    p = True
    a, b = map(int, sys.stdin.readline().strip().split(' '))
    while p and parent_list[a-1] != 0 and parent_list[b-1] != 0 and (not isparent(a, b)) and (not isparent(b, a)):
        a = parent_list[a-1]
        if isparent(b, a):
            print 'A'
            p = False
        b = parent_list[b-1]
    if p and (isparent(a, b) or parent_list[b-1] == 0):
        print 'B'
    elif p and (isparent(b, a) or parent_list[a-1] == 0):
        print 'A'
