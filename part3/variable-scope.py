age = 27

print(age)


def increase_age():
    age = 30

    def add_4_to_age(age):
        age = age + 4
        print("NESTED METHOD: " + str(age))

    add_4_to_age(age)
    print(age)


increase_age()

print(age)
