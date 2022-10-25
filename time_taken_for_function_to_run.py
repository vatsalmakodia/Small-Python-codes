from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'\ntime taken {t2 - t1}s')
        return result
    return wrapper

# EXAMPLES - Just use the @performance method to find the time taken for a function to run

@performance

def long_time():
    for i in range(999999):
        i*99

long_time()

@performance 

def list1(): 
    print(list(range(0,101101)))

list1()