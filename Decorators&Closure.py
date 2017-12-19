'''def printLog(self, func):
    def wrapper(self, *args,**kwargs):
        print("CALLING: {}".format(func.__name__))
        return func(self, *args, **kwargs)
    return wrapper


class OBJ():
    def add(self,x,y):
        return x+y

    def subtract(self,x,y):
        return x-y

    def division(self,x,y):
        f = float(x)/float(y)
        return "{0:.2f}".format(f)

    def multiply(self,x,y):
        return x*y

    def add_3_no(self,x,y,z):
        return x+y+z


a=OBJ()

print(a.add(3,6))
print(a.add_3_no(1,4,9))
print(a.division(9,4))
print(a.multiply(9,8))'''

#Data in decorators

'''def running_average(func):
    data={"total":0, "count":0}
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        data["total"] += val
        data["count"] += 1
        print("average of {} so far: {:.2f}".format((func.__name__), data["total"]/data["count"]))
        return func(*args, **kwargs)
    return wrapper

@running_average
def foo(x):
    return x

foo(2)
foo(3)
foo(4)
foo(8)'''

#to see the data in dictionary
'''def collect_stats(func):
    data={"total":0, "count":0}
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        data["total"] += val
        data["count"] += 1
        print("average of {} so far: {:.2f}".format((func.__name__), data["total"]/data["count"]))
        return func(*args, **kwargs)
    wrapper.data=data#assign the data in wrapper.data to peek into dictionary
    return wrapper

@collect_stats
def vikruc(x):
    return x
print(vikruc.data)
vikruc(3)
print(vikruc.data)
vikruc(5)
print(vikruc.data)
vikruc(7)
print(vikruc.data)
vikruc(9)'''

#non-local variable


def countcall(func):
    count = 0
    def wrapper(*args,**kwargs):
        nonlocal count
        count += 1
        print("# of times this function has been called: {}".format(count))
        return func(*args, **kwargs)
    return wrapper

@countcall
def foo(x):return x

@countcall
def bar(x):return x**2

foo(1)
foo(5)
foo(99)
bar(4)
