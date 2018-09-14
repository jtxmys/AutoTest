# def foo():
#     print('hello')

'''---------------------------'''
# import time
# def foo():
#     start = time.time()
#     print('hello')
#     end = time.time()
#     print(end-start)
'''------------------------'''
# import  time
# def foo():
#     print('hello')
#
# def timeit(func):
#     start = time.time()
#     func()
#     end = time.time()
#     print(end-start)
'''--------------------------'''
# import time
# def foo():
#     print('hello')
# def timeit(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print(end-start)
#     return wrapper
'''-----------------------------'''
import time

# def timeit(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print(end-start)
#     return wrapper
# @timeit
# def foo():
#     print('hello')
#foo()
def timeit(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        print(end -start)
    return wrapper
@timeit
def foo(_str,mm):
    print(_str,mm)
foo('hello','hh')

# if __name__ == '__main__':
#     # foo() #2
#     # timeit(foo)#3
#     # foo = timeit(foo)#4
