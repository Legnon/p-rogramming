import time

cached_1 = {}

def mysum(x,y):
    key = (x,y)
    if key not in cached_1:
        time.sleep(1)
        cached_1[key] = x+y
    return cached_1[key]

cached_2 = {}

def mymultiple(x,y):
    key = (x,y)
    if key not in cached_2:
        time.sleep(1)
        cached_2[key] = x * y
    return cached_2[key]

print(mysum(1,2))
print(mysum(1,3))
print(mysum(1,2))
print(mysum(1,2))

print(mymultiple(1,2))
print(mymultiple(1,4))
print(mymultiple(1,2))
print(mymultiple(1,2))
