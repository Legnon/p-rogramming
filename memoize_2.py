import time

def memoize(fn):
    cached = {}
    def wrap(x,y):
        key = (x,y)
        if key not in cached:
            time.sleep(1)
            cached[key] = fn(x,y)
        return cached[key]
    return wrap


def base(i):
    def wrap(fn):
        def inner(x,y):
            return fn(x,y) + i
        return inner
    return wrap


@memoize
def mysum(x,y):
    return x+y

@memoize
def mymultiple(x,y):
    return x*y

@base(10)
def mysum1(x,y):
    return x+y


print(mysum(1,2))
print(mysum(1,3))
print(mysum(1,2))
print(mysum(1,2))

print(mymultiple(1,2))
print(mymultiple(1,3))
print(mymultiple(1,2))
print(mymultiple(1,2))

print(mysum1(1,2))
