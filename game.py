import random
import time

class Player():
    def __init__(self, name):
        self.health = 100
        self.name = name
        self.wins = 0

    def calculate_damage(self, damage_amount, attacker):
        if (damage_amount > self.health):
            overkill = abs(self.health - damage_amount)
            self.health = 0
            if (overkill > 0):
                print("{0} takes critical damage from {1}, with {2} overkill!"
                      .format(self.name.capitalize(), attacker, overkill))
            else:
                print("{0} takes critical damage from {1}!"
                      .format(self.name.capitalize(), attacker))
        else:
            self.health -= damage_amount
            print("{0} takes {1} damage from {2}!"
                  .format(self.name.capitalize(), damage_amount, attacker))

    def calculate_heal(self, heal_amount):
        if (heal_amount + self.health > 100):
            self.health = 100
            print("{0} heals back to full health!"
                  .format(self.name.capitalize()))
        else:
            self.health += heal_amount
            print("{0} heals for {1}!"
                  .format(self.name.capitalize(), heal_amount))


def parse_int(input):
    try:
        int(input)
        return True
    except ValueError:
        return False


def get_selection():
    valid_input = False
    while (valid_input is False):
        print()
        choice = input("Select an attack: ")
        if (parse_int(choice) is True):
            return int(choice)
        else:
            print("The input was invalid. Please try again.")


def get_computer_selection(health):
    sleep_time = random.randrange(2, 5)
    print("....Computer's Turn....")
    time.sleep(sleep_time)

    if (health <= 35):
        # Have the computer heal ~50% of its turns when <= 35
        result = random.randint(1, 6)
        if (result % 2 == 0):
            return 3
        else:
            return random.randint(1, 2)
    elif (health == 100):
        return random.randint(1, 2)
    else:
        return random.randint(1, 3)


def play_round(computer, human):
    game_in_progress = True
    current_player = computer

    while game_in_progress:
        # swap the current player each round
        if (current_player == computer):
            current_player = human
        else:
            current_player = computer

        print()
        print(
            "Your health- {0}\n"
            "Computer's health- {1}"
            .format(human.health, computer.health))
        print()

        if (current_player == human):
            print("Available attacks:")
            print("1) Cyber Hack - Causes moderate damage.")
            print("2) Electro Wave - high or low damage, "
                  "depending on your wave frequency.")
            print("3) Health ammo - Restores a moderate amount of health.")
            move = get_selection()
        else:
            move = get_computer_selection(computer.health)

        if (move == 1):
            damage = random.randrange(15, 25)
            if (current_player == human):
                computer.calculate_damage(damage, human.name.capitalize())
            else:
                human.calculate_damage(damage, computer.name.capitalize())
        elif (move == 2):
            damage = random.randrange(15, 45)
            if (current_player == human):
                computer.calculate_damage(damage, human.name.capitalize())
            else:
                human.calculate_damage(damage, computer.name.capitalize())
        elif (move == 3):
            heal = random.randrange(15, 25)
            current_player.calculate_heal(heal)
        else:
            print ("Invalied weapon choosed. Please choose again.")

        if (human.health == 0):
            print("U have been killed by Computer...")
            computer.wins += 1
            game_in_progress = False

        if (computer.health == 0):
            print("Congratulations, you beat the Computer!")
            human.wins += 1
            game_in_progress = False


def start_game():
    print("_Welcome to the Battle Screen_")
    time.sleep(1)

    computer = Player("Computer")

    name = input("Please enter your name: ")
    human = Player(name)

    keep_playing = True

    while (keep_playing is True):
        print("Current Score:")
        print("You - {0}".format(human.wins))
        print("Computer - {0}".format(computer.wins))

        computer.health = 100
        human.health = 100
        play_round(computer, human)
        print()
        response = input("Play another round?(Y/N)")
        if (response.lower() == "n"):
            input("Thanks for playing")
            break

start_game()
