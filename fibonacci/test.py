import myModule
import time

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2);

if __name__ == '__main__':
    s1 = time.time()
    print(myModule.fib(33))
    c_time = time.time() - s1
    print(f'C took = {c_time}')
    
    s2 = time.time()
    print(fib(33))
    python_time = time.time() - s2
    print(f'Python took = {python_time}')
    print(f'C was {python_time/c_time} times faster than Python')