# my_tuple = (1, 2, 3, "Stardust Crusaders", ["Star Platinum", "Hierophant Green", "Magician's Red", "Silver Chariot"])
#
# print(my_tuple[4])

# # The piece of code below won't work, because a tuple's values can't be modified.
# my_tuple = (1, 2, 3, "Stardust Crusaders", ["Star Platinum", "Hierophant Green", "Magician's Red", "Silver Chariot"])
#
# my_tuple[3] = "JJBA Part 3 Main Characters Stands"
#
# print(my_tuple)

# # The piece of code below does work, because you are changing the list inside the tupple.
# my_tuple = (1, 2, 3, "Stardust Crusaders", ["Star Platinum", "Hierophant Green", "Magician's Red", "Silver Chariot", "Iggy"])
#
# my_tuple[4][4] = "The Fool"
#
# print(my_tuple)

# my_tuple = (1, 2, 3, "Stardust Crusaders", ["Star Platinum", "Hierophant Green", "Magician's Red", "Silver Chariot"])
#
# count = my_tuple.count("Stardust Crusaders")
#
# print(count)

# my_tuple = (1, 2, 3, "Stardust Crusaders", ["Star Platinum", "Hierophant Green", "Magician's Red", "Silver Chariot"])
#
# print(my_tuple[3:6])

# my_tuple = (1, 2, 3, "Stardust Crusaders", ["Star Platinum", "Hierophant Green", "Magician's Red", "Silver Chariot"])
#
# str_tuple = my_tuple[3:6]
#
# print(str_tuple)

my_tuple = (1, 2, 3, "Stardust Crusaders", ["Star Platinum", "Hierophant Green", "Magician's Red", "Silver Chariot"])

extracted = my_tuple[4]

print(type(extracted))
