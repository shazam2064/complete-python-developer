class Stand:

    # def __init__(self, name):
    #     self.stand_name = name

    def attack(self):
        raise NotImplementedError("Child class should be implementing this")


class ZaWarudo(Stand):

    def attack(self):
        print("MUDA MUDA MUDA")


class GoldenExperienceRequiem(Stand):

    def attack(self):
        print("Muda Muda Muda")

    def specialAttack(self):
        print("Korega Requiem Da")


stand1 = ZaWarudo()
stand1.attack()

stand2 = GoldenExperienceRequiem()
stand2.specialAttack()
