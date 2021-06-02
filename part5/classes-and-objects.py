class Stando:

    stando_counter = 0

    def __init__(self, name, type, range, form):
        self.stand_name = name
        self.stand_type = type
        self.stand_range = range
        self.stand_form = form
        Stando.stando_counter += 1

    def get_stand_count(self):
        return Stando.stando_counter


stand1 = Stando("Dirty Deed Done Dirt Cheap", "Natural Humanoid", "Close Ranged", "Normal")
stand2 = Stando("Tusk", "Natural Humanoid", "Close Ranged", "Act 4")

print(stand1.stand_name)
print(stand1.stand_type)
print(stand1.stand_range)
print(stand1.stand_form)

print(stand2.stand_name)
print(stand2.stand_type)
print(stand2.stand_range)
print(stand2.stand_form)

