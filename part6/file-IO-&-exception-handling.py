# try:
#     with open('/Users/Gabriel/Downloads/complete-python-developer/part6/sample.txt') as my_file:
#         print(my_file.read())
# except FileNotFoundError:
#     print("File does not exist: FileNotFoundError")
# except TypeError:
#     print("There was a type error")
# except:
#     print("Error Occurred Logging to the system")
# finally:
#     print('''
#     This shall always run, with or without exceptions.
#     No exception who stands before me shall stop this, regardless of their abilities.
#     This is the power of Gold Experience Requiem!
#      ''')
#
# print("This line was run")

# try:
#     my_file = open('/Users/Gabriel/Downloads/complete-python-developer/part6/sample.txt', mode='r')
#     print(my_file.read())
#     try:
#         print(my_file.read())
#     except FileNotFoundError:
#         print("File does not exist: FileNotFoundError")
#     except TypeError:
#         print("There was a type error")
#     except:
#         print("Error Occurred Logging to the system")
#     finally:
#         my_file.close()
#         print('''
#     This shall always run, with or without exceptions.
#     No exception who stands before me shall stop this, regardless of their abilities.
#     This is the power of Gold Experience Requiem!
#      ''')
# except:
#     print("Congragulations, you managed to make some odd error happen")
#
# print("This line was run")

# my_file = None
#
# try:
#     my_file = open('/Users/Gabriel/Downloads/complete-python-developer/part6/sample.txt', mode='r')
#     print(my_file.read())
#     try:
#         print(my_file.read())
#     except IOError:
#         print("Issue with working with the file")
#     finally:
#         my_file.close()
#         print('''
#     This shall always run, with or without exceptions.
#     No exception who stands before me shall stop this, regardless of their abilities.
#     This is the power of Gold Experience Requiem!
#      ''')
# except:
#     print("Congragulations, you managed to make some odd error happen")
#
# print("This line was run")

my_file = None

try:
    my_file = open('/Users/Gabriel/Downloads/complete-python-developer/part6/sample.txt', mode='r')
    print(my_file.read())

except IOError:
    print("Issue with working with the file")
finally:
    if my_file != None:
        my_file.close()
    print('''
    This shall always run, with or without exceptions.
    No exception who stands before me shall stop this, regardless of their abilities.
    This is the power of Gold Experience Requiem!
     ''')

print("This line was run")
