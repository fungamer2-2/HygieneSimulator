##
# Name: Ollie Joe
# Date: 07/06/022
# Description: RPG battle simulator which teaches dental hygiene.

from random import randint
from time import sleep

# Constants
MAX_HP = 100
SEPARATOR = "-" * 40
SPACE_LENGTH = 13
weaken_weapons = [
               ["Toothbrush", 25],
               ["Dental Floss", 25],
               ["Mouthwash", 25]
               ]
kill_weapons = [
             ["Dental Scaler", 1],
             ["Filling", 1],
             ]
MAX_MULTIPLIER = 30


# class enemy():
#     def __init__(self, health):
#         self.health = health


# one = enemy(100)
# two = enemy(100)
# three = enemy(100)

# enemies = [one, two, three]
# dead = []
# while len(enemies) > 0:
#     en = int(input("Enemy: ")) - 1
#     enemies[en].health -= randint(25, 75)
#     if enemies[en].health <= 0:
#         enemies[en].health = 0
#         dead.append(enemies[en])
#         if enemies[en] in dead:
#             print("That enemy has already been defeated.")
#     for i in range(len(enemies)):
#         print(enemies[i].health)


class characters():
    def __init__(self, type, health, base_dmg, money):
        self.type = type
        self.health = health
        self.base_dmg = base_dmg
        self.money = money


def user_info():
    print(f"{SEPARATOR}\n")
    print("              Player:\n")
    print(f"    Health:           {player.health}/{MAX_HP} HP")
    print(f"    Wallet:           ${player.money}")
    print("\n    Main Damage Weapons:")
    for count, value in enumerate(weaken_weapons, start=1):
        sleep(0.2)
        print(f"      {count}: " + value[0])
    sleep(0.5)
    print("\n    Finishing Weapons:")
    for count, value in enumerate(kill_weapons, start=1):
        sleep(0.2)
        print(f"      {count}: " + value[0])


def enemy_info():
    print(f"\n{SEPARATOR}\n")
    sleep(0.5)
    print("              Enemies:\n")
    for count, i in enumerate(range(len(enemies_list[1])), start=1):
        sleep(0.3)
        print(f"    {count}: {enemies_list[1][i].type} " +
              (" " * (SPACE_LENGTH - (len(enemies_list[1][i].type)))) +
              f"{str(enemies_list[1][i].health)}/{MAX_HP} HP")
    print("\n" + SEPARATOR + "\n")
    sleep(0.5)


def weapon_selection():
    print("\n" + SEPARATOR)
    while True:
        sleep(0.5)
        try:
            print("\n    Main Weapons:")
            for count, value in enumerate(weaken_weapons, start=1):
                print(f"    {count}: " + value[0])
            print("\n" + SEPARATOR)
            chosen_weapon = int(input("\nEnter a number " +
                                      "to select a weapon : "))
            if chosen_weapon in range(1, len(weaken_weapons) + 1):
                print(f"You have chosen " +
                      f"{weaken_weapons[chosen_weapon - 1][0]}!")
                print("\n" + SEPARATOR)
                return chosen_weapon - 1
            else:
                print("Please enter a number from {} to {}."
                      .format(1, len(weaken_weapons)))
                print("\n" + SEPARATOR)
        except Exception:
            print("Sorry, that is not a valid choice.")
            print("\n" + SEPARATOR)


def chosen_enemy():
    sleep(0.5)
    while True:
        try:
            target_enemy = int(input("Select an enemy's number to attack: "))
            if target_enemy in range(1, len(enemies_list[1]) + 1):
                print(f"You have chosen enemy {target_enemy}, " +
                      f"{enemies_list[1][target_enemy-1].type}!")
                return target_enemy - 1
            else:
                print(f"Please enter a number from {1} to " +
                      f"{len(enemies_list[1])}.")
                enemy_info()
        except ValueError:
            print(f"Please enter a number from {1} to " +
                  f"{len(enemies_list[1])}.")
            enemy_info()


player = characters("Player", 100, 0, 0)
plaque = characters("Plaque", 100, 3, 0)
tartar = characters("Tartar", 100, 3, 0)
tooth_decay = characters("Tooth Decay", 100, 3, 0)
# enemies_list = [plaque,
#                 tartar,
#                 tooth_decay]
# current_enemies_list = []
# for i in range(3):
#     current_enemies_list.append(enemies_list[random.randint(0, 2)])


enemies_list = [[plaque,
                tartar,
                tooth_decay],
                []]
for i in range(3):
    enemies_list[1].append(enemies_list[0]
                           [randint(0, len(enemies_list))])


# CLEAR THE LIST AT THE END OF EACH ROUND.

enemy = 2
# PLAYER RANDOM DAMAGE MULTIPLIER.
# critical_hit = int(10 * (random.randint(1, 2) + (random.randint(0, 9) * 0.1))
#                    if random.randint(1, 3) == 1 else 0)
# current_attack = weaken_weapons[player.base_dmg][1] + critical_hit

# player_attack = (int(weaken_weapons[player.base_dmg][1] *
#                  (randint(11, 30))/10)
#                  if randint(1, 3) ==
#                  1 else weaken_weapons[player.base_dmg][1])


# enemy_attack = (int(enemies_list[1][enemy].base_dmg *
#                 (randint(12, 30))/10)
#                 if randint(1, 3) == 1 else 3)


def attack(damage, min):
    if enemies_list[1][enemy].base_dmg == damage and randint(1, 24) == 1:
        print(f"{enemies_list[1][enemy].type} has missed.")
        return 0
    elif weaken_weapons[player.base_dmg][1] == damage and randint(1, 8) == 1:
        return 0
    if enemies_list[1][enemy].base_dmg == damage and randint(1, 1) == 1:
        while True:
            try:
                player_guess = int(input("Guess a number between" +
                                         " 1 and 2 to dodge the attack: "))
                random_num = randint(1, 2)
                if player_guess == random_num:
                    print("CORRECT! You have dodged the enemy's attack.")
                    return 0
                elif player_guess != random_num and player_guess in range(1, 2):
                    print("INCORRECT! You failed to dodge the attack.")
                    break
                else:
                    print("Please enter a number between 1 and 2.")
            except ValueError:
                print("Please enter a number between 1 and 2.")
    elif (weaken_weapons[player.base_dmg][1] == damage
          and randint(1, 10) == 1):
        return 0
    return (int(damage * randint(min, MAX_MULTIPLIER) / 10)
            if randint(1, 3) == 1 else damage)


print(f"Your attack dealt {attack(weaken_weapons[player.base_dmg][1], 11)} damage.")
print(f"{enemies_list[1][enemy].type} has dealt {attack(enemies_list[1][enemy].base_dmg, 12)} to you.")


def battle():
    round = 1
    if len(enemies_list) != 0 and round <= 5:
        user_info()
        sleep(1)
        print(f"\n{SEPARATOR}\n")
        print(f"              ROUND {round}!")
        enemy_info()
        enemy = chosen_enemy()
        player.base_dmg = weapon_selection()
        round += 1
    elif round == 6:
        print("")


battle()
