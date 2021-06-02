from stands import Stand, Requiem, OverHeaven

stand1 = Stand("Crazy Diamond", "Natural Humanoid", "Close Ranged", "Normal")
requiem1 = Requiem("Golden Experience Requiem", "Evolved", "Close Ranged", "Requiem")
overHeaven1 = OverHeaven("Za Warudo Over Heaven", "Evolved", "Close Ranged", "Over Heaven")

for stand in [stand1, requiem1, overHeaven1]:
    print(stand.stand_name)
    print(stand.stand_type)
    print(stand.stand_range)
    print(stand.stand_form)
    stand.attack()
    print("---------------------------------")
