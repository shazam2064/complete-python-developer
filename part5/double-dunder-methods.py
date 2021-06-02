class Part3Character:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + "'s age is " + str(self.age)


Jotaro = Part3Character("Jotaro Kujo", 17)

print(Jotaro)
