class Character:
    def __init__(self, name, health=10, power=5):
        self.name = name
        self.health = health
        self.power = power
        self.weapons = []

    def attack(self, enemy):
        print(f"{self.name} attacks {enemy.name}!")
        enemy.health -= self.power

    def is_alive(self):
        return self.health > 0

class Hero(Character):
    def __init__(self, name, health, power, cape):
        super().__init__(name, health, power)
        self.cape = cape

class Villain(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

hero = Hero('Batman', 20, 8, True)
villain = Villain('Joker', 40, 2)

if hero.cape == True:
    print(f"{hero.name} has a cape")
else:
    print(f"NO CAPES!")

def main():

    while villain.health > 0 and hero.health > 0:
        print("You have %d health and %d power." % (hero.health, hero.power))
        print(f"The {villain.name} has {villain.health} health and {villain.power} power.")
        print()
        print("What do you want to do?")
        print(f"1. fight {villain.name}")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            hero.attack(villain)
            print("You do %d damage to the %s." % (hero.power, villain.name))
            if not villain.is_alive():
                print(f"The {villain.name} is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if villain.is_alive():
            # Goblin attacks hero
            villain.attack(hero)
            print("The %s does %d damage to you." % (villain.name, villain.power))
            if not hero.is_alive():
                print("You are dead.")

main()
