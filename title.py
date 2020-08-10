import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    arr = sys.stdin.readline().strip()
    values = map(int, arr.split())
    max_v = max(values)
    res = []
    for i in range(max_v):
        #cha = 0
        #for j in range(N):
            #cha = cha + abs(values[j]-i)
        cha = map(lambda x:abs(x-i), values)
        #cha = map(lambda x:abs(x), cha)
        cha = sum(cha)
        res.append(cha)
    print(min(res))