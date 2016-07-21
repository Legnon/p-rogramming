def alert(maximum):
    def wrap(fn):
        def inner(x,y):
            result = fn(x,y)
            if result > maximum:
                print('{} is bigger than {}'.format(result, maximum))
            return result
        return inner
    return wrap


@alert(10)
def mysum(x,y):
    return x+y

print(mysum(5,5))
print(mysum(6,6))

# 인자 무제한으로 받는 절대값 함수
def absolute(fn):
    def wrap(*args):
        # 1)
        # args = list(args)
        # for idx,val in enumerate(args):
        #     args[idx] = abs(val)

        # 2)
        # args = [abs(i) for i in args]

        # 3)
        args = map(abs, args)
        return fn(*args)
    return wrap


@absolute
def mysum1(*args):
    return sum(args)

print(mysum1(-10,1,2))
