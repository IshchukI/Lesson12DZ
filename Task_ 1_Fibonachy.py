import datetime


def benchmark(func):
    def wrapper():
        t = datetime.datetime.now()
        print(f'Время запуска <{t}>')
        res = func()
        print(f'результат: {res}')
        print(f'функция <{func.__name__}> выполняется: <{datetime.datetime.now()-t}>')
        return res
    return wrapper


@benchmark
def sum_fibonacci():
    fib1 = 1
    fib2 = 1
    sum_f = fib1 + fib2
    i = 0
    while i < 98:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        sum_f += fib2
        i = i + 1
    return sum_f



def sum_fibonacci_gen():
    fib1 = 1
    fib2 = 1
    i = 0
    yield fib1 + fib2
    while i < 98:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        yield fib2
        i = i + 1

@benchmark
def sum_fibonacci_gen_calc():
    sum_f_generator = 0
    f = sum_fibonacci_gen()
    for i in f:
        sum_f_generator += i
    return sum_f_generator


sum_fib = sum_fibonacci()
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
sum_fib_gen = sum_fibonacci_gen_calc()
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print(f'сумма чисел фибоначи без генератора: {sum_fib}')
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print(f'сумма чисел фибоначи с генератором: {sum_fib_gen}')