import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print("Время работы функции '{func_name}' составило {total_time}".format(
            func_name=func.__name__, total_time=time.time() - start
        ))
        return result

    return wrapper



def get_list_by_default(*args, **kwargs):
    my_list = []
    for i in range(args):
        my_list.append(i)

    return my_list


def get_list_by_comp(*args, **kwargs):
    return [i for i in range(args)]


get_list_by_comp(10 ** 6 * 15, 10, 20, 30, 40)
get_list_by_default(10 ** 6 * 15)
