# import time
#
# def get_list_by_default(val):
#     start = time.time()
#     my_list = []
#     for i in range(val):
#         my_list.append(i)
#     end = time.time()
#     print("Итоговое время:", end - start)
#     return my_list
#
# def get_list_by_comp(val):
#     start = time.time()
#     my_list =  [i for i in range(val)]
#     end = time.time()
#     print("Итоговое время:", end - start)
#     return my_list
#
# get_list_by_comp(10 ** 6 * 15)
# get_list_by_default(10 ** 6 * 15)
#


import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print("Время работы функции '{func_name}' составило {total_time}".format(func_name=func.__name__, total_time=time.time() - start))
        return result

    return wrapper

@timer

def get_list_by_default(val):
    my_list = []
    for i in range(val):
        my_list.append(i)
    return my_list

def get_list_by_comp(val):
    return [i for i in range(val)]


get_list_by_comp(10 ** 6 * 15)
get_list_by_default(10 ** 6 * 15)



