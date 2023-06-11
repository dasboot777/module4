#асимптотика
# def strcount(s):# решение за O(N^2)
#     for sym in set(s):#set - преобразуем список в множество (толко уникальные эдемеенты)
#         counter = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 counter += 1
#         print(sym, counter)
#
# strcount('aabcde')
#
# # l = ['aabcde']
# # print(set(l))#преобразуем список в множество (толко уникальные эдемеенты)

def strcount(s):# решение за O(2*N или N+M) --> O(N)
    mydict = {}
    for sym in s:
        mydict[sym] = mydict.get(sym, 0) + 1
    for key in mydict:
        print(key, mydict.get(key))


strcount('aabcde')