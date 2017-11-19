input()
a = map(int,raw_input().split())
input()
b = map(int,raw_input().split())
c = set(a).intersection(set(b))
for i in b:
    if i in c:
        print 1
    else:
        print 0
'''
def search(arr,len,target):
    first = 0
    last = len - 1
    while first <= last:
        mid = (first + last) / 2
        if arr[mid] == target:
            return 1
        else:
            if arr[mid] > target:
                last = mid - 1
            else:
                first = mid + 1
    return 0
input()
a = sorted(map(int,raw_input().split()))
input()
b = map(int,raw_input().split())
for i in range(len(b)):
    print search(a,len(a),b[i])
'''