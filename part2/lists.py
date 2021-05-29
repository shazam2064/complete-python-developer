# my_list = [1, 2, 3, 4, 5]
#
# print(type(my_list))

# my_list = [1, 2, 3, 4, 5]
#
# my_list.pop()
#
# print(my_list)

# my_list = [1, 2, 3, 4, 5]
#
# my_list[0] = ['Ari Ari Ari', 'Arrivederci']
#
# print(my_list)

# my_list = [1, 2, 3, 4, 5]
#
# my_list.append("This is requiem")
#
# print(my_list)

# my_list = [1, 2, 3, 4, 5]
#
# my_list.append("This is requiem")
#
# my_list.pop()
#
# print(my_list)

# my_list = [1, 2, 3, 4, 5]
#
# my_list.append("This is requiem")
#
# sentence = my_list.pop()
#
# print(my_list)
# print(sentence)

# my_list = [1, 2, 3, 4, 5]
#
# appended = my_list.append("This is requiem")
#
# sentence = my_list.pop()
#
# print(my_list)
# print(sentence)
# print(appended)

# my_list = [4, 5, 3, 1, 2]
#
# my_list.sort()
#
# print(my_list)

# my_list = [4, 5, 3, 1, 2]
#
# my_list.reverse()
#
# print(my_list)

# my_list = [4, 5, 3, 1, 2]
#
# my_list.sort()
# my_list.reverse()
#
# print(my_list)

# my_list = ['a', 'b', 'c', 1, 2, 3, ["Magician's Red", "Hierophant Green", "Silver Chariot"], 'd']
#
# extracted_stand = my_list[6]
#
# print(extracted_stand[2])

# my_list = ['a', 'b', 'c', 1, 2, 3, ["Magician's Red", "Hierophant Green", "Silver Chariot"], 'd']
#
# extracted_stand = my_list[6][2]
#
# print(extracted_stand)

# my_list = ['a', 'b', 'c', 1, 2, 3, ["Magician's Red", "Hierophant Green", "Silver Chariot"], 'd']
#
# print(my_list[6][2])

# my_list = ['a', 'b', 'c', 1, 2, 3, ["Magician's Red", "Hierophant Green", ["Iggy", "The Fool"], "Silver Chariot"]]
#
# print(my_list[6][2][1])

# my_list = ['a', 'b', 'c', 1, 2, 3, ["Magician's Red", "Hierophant Green", ["Iggy", "The Fool"], "Silver Chariot"]]
#
# my_list[2] = 'Star Platinum'
# print(my_list)

# my_list = ['a', 'b', 'c', 1, 2, 3, ["Magician's Red", "Hierophant Green", ["Iggy", "The Fool"], "Silver Chariot"]]
#
# my_list[6][2][0] = 'Jotaro'
# my_list[6][2][1] = 'Star Platinum'
# print(my_list)

# my_list = ["Star Platinum", "Magician's Red", "Hierophant Green", "Silver Chariot"]
#
# idx_pos = my_list.index("Hierophant Green")
#
# print(idx_pos)

my_list = ["Star Platinum", "Magician's Red", "Hierophant Green", "Silver Chariot"]
# ".count" counts how many of the object there are. In this case there is only one Hierophant Green so it returns 1
hierophant_green_count = my_list.count("Hierophant Green")

print(hierophant_green_count)
