# result = sum((1, 2, 3, 4, 5))
#
# print(result)

# def four_digit_sum(a, b, c, d):
#     return a + b + c + d
#
#
# print(four_digit_sum(1, 2, 3, 4))

# def four_digit_sum(a, b, c, d, e, f, g):
#     return a + b + c + d + e + f + g
#
#
# print(four_digit_sum(1, 2, 3, 4, 5, 6, 7))

# def my_sum(*args):
#     return sum(args)
#
#
# result = my_sum(10, 20, 30, 1, 1, 1, 1, 10, 5, 6, 19, 9, 0, 2, 7, 8, 40)
#
# print(result)

# def key_value_func(**kwargs):
#     print(kwargs)
#
#
# key_value_func(stand="Golden Experience", form="Requiem")

# def key_value_func(**kwargs):
#     print(kwargs.keys())
#
#
# key_value_func(stand="Golden Experience", form="Requiem")

# def key_value_func(**kwargs):
#     print(kwargs.values())
#
#
# key_value_func(stand="Golden Experience", form="Requiem")

# def key_value_func(**kwargs):
#     print(kwargs.get("stand"))
#
#
# key_value_func(stand="Golden Experience", form="Requiem")

# def key_value_func(**kwargs):
#     print(kwargs.get("form"))
#
#
# key_value_func(stand="Golden Experience", form="Requiem")

# def key_value_func(**kwargs):
#     print(kwargs.get("sub_stand"))
#
#
# key_value_func(stand="Golden Experience", form="Requiem")

# def key_value_func(**stand_info):
#     print(stand_info.get("sub_stand"))
#
#
# key_value_func(stand="Golden Experience", form="Requiem")

def key_value_func(**stand_info):
    print(stand_info)


key_value_func(stand="Golden Experience", form="Requiem")
