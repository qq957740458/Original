import math

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# print(my_abs(100))

def nop():
    pass

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

# x, y= move(100, 100, 60, math.pi / 6)
# print(x, y)

# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

nums = [1, 2, 3]
# print(calc(nums[0], nums[1], nums[2]))
# print(calc(*nums))

# 关键字参数
def person(name, age, **kw):
    print('name: ', name, 'age: ', age, 'other: ', kw)

extra = {'job': 'developer', 'city': 'Hangzhou'}
# person('Lixxxx', '25', **extra)

# 高级特性 切片
L = ['Michael', 'Sarah', 'Tracy']
print(L[0:1])
