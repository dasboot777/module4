# class SingleTone:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not cls.__instance:
#             cls.__instance = super().__new__(cls)
#
#         return cls.__instance
#
#     def __init__(self, name):
#         self.name = name
#
#
# a = SingleTone("Никита")
# a1 = SingleTone("Миша")
#
# print(a is a1)
#
# print(a.name)
# print(a1.name)
