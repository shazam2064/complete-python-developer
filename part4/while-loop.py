# x = 0
#
# while x < 10000000000000000:
#     x += 1
#     print(x)
# else:
#     print("print x is not less than 10")

# x = 0
#
# while x < 10:
#     x += 3
#     print(x)
# else:
#     print("print x is not less than 10")

x = 0

while x < 10:
    if x == 6:
        continue

    x += 3

    print(x)

else:
    print("print x is not less than 10")
