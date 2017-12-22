n = input()
a = map(int,raw_input().split())
m = input()
b = map(int,raw_input().split())
c = set(a).intersection(set(b))
d = []
for i in range(len(b)):
    if b[i] in c:
        d.append('1')
    else:
        d.append('0')
print " ".join(d)
'''
def search(arr,len,target):
    first = 0
    last = len - 1
    mid = 0
    while first <= last:
        mid = (first + last)/2
        if arr[mid] == target:
            return 1
        else:
            if arr[mid] > target:
                last = mid - 1
            else:
                first = mid + 1
    return 0
n = input()
a = sorted(map(int,raw_input().split()))
m = input()
b = map(int,raw_input().split())
c = []
for i in range(len(b)):
     c.append(search(a,len(a),b[i]))
print " ".join([str(c[i]) for i in range(len(c))])
'''