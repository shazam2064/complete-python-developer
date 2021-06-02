class Stand:
    stand_counter = 0

    def __init__(self, name, type, range, form):
        self.stand_name = name
        self.stand_type = type
        self.stand_range = range
        self.stand_form = form
        Stand.stand_counter += 1

    def get_stand_count(self):
        return Stand.stand_counter

    def attack(self):
        print("[Attacking Noises]")


class Requiem(Stand):
    def attack(self):
        print("[Requiem Attacking Noises]")


class OverHeaven(Stand):
    def attack(self):
        print("[Over Heaven Attacking Noises]")

# stand1 = Stand("Dirty Deed Done Dirt Cheap", "Natural Humanoid", "Close Ranged", "Normal")
# stand2 = Stand("Tusk", "Evolved", "Close Ranged", "Act 4")
#
# print(stand1.stand_name)
# print(stand1.stand_type)
# print(stand1.stand_range)
# print(stand1.stand_form)
#
# print(stand2.stand_name)
# print(stand2.stand_type)
# print(stand2.stand_range)
# print(stand2.stand_form)
