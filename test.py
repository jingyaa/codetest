def sort_arr(arr):
    res = arr.sort()

    return res

import sys

if __name__ == "__main__":
    mn = sys.stdin.readline().strip()
    mn = map(int, mn.split())
    n = mn[0]
    m = mn[1]
    lines1 = sys.stdin.readline().strip()
    arr = map(int, lines1.split())
    for i in range(m):
        value_i = sys.stdin.readline().strip()
        value_i = map(int, value_i.split())
        print('B')



