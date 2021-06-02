my_file = open('/Users/Gabriel/Downloads/complete-python-developer/part6/sample.txt')

content = my_file.read()
print(content)

my_file.seek(0)

print(
    "-------------------------------------------------------------------------------------------------------------------------------")
data = my_file.read()
print(data)

content_list = my_file.readlines()
my_file.close()
print(content_list)
