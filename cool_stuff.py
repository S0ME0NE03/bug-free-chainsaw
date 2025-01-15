import random as r

class DiceRoller:
    def __init__(self, dice_sides, how_many_dice):
        self.dice_sides = int(dice_sides)
        self.how_many_dice = int(how_many_dice)
        self.result = []

    def roll(self):
        for _ in range(self.how_many_dice):
            self.result.append(r.randint(1, self.dice_sides))
        print(f"Roll results: {self.result}")

class ListPrinter:
    def __init__(self, list_to_print, leading_words, trailing_words):
        self.list_to_print = list_to_print
        output = ", ".join(self.list_to_print)
        print(f"{leading_words} {output} {trailing_words}")

class Help:
    def __init__(self, list_of_commands, dict_of_commands):
        self.list_of_commands = list_of_commands
        self.dict_of_commands = dict_of_commands
        
    def normal(self):
        ListPrinter(self.list_of_commands, "Welcome to help \nList of commands: ", "\n")
        action = input("What would you like help with? \nCommand: ").lower()
        if action in self.dict_of_commands:
            print(self.dict_of_commands[action])  
        else:
            print("Command not found.")

class LetterEliminator:
    def __init__(self, word, ttc):
        self.word = word
        self.ttc = ttc
        self.result = ""

    def letter_eliminator_main(self):
        for i in self.word:
            if self.is_this_character_in_a_string(i, self.ttc, False):
                self.result += i
        return self.result

    def is_this_character_in_a_string(self, inp, cool, bopo):
        for letters in cool:
            if letters == inp:
                return bopo
        return not bopo

class CedarsSubCommands:
    def __init__(self, Command, arg_1, arg_2):
        self.list_to_print = ["letter eliminator", "Dice Roller", "Help", "exit"]
        self.dict_of_commands = {
            "letter eliminator": 'Removes letters from words',
            "dice roller": 'Rolls a specified # of dice with a specified # of sides',
            "help": 'Tells you what my commands do \nyou are here',
        }
        self.Command = Command
        self.arg_1 = arg_1
        self.arg_2 = arg_2

    def c_commands(self):
        while True:
            print("")
            ListPrinter(self.list_to_print, "Cedar's commands(", "):\n")
            action = input("What do you want to do? \n").lower()
            if action == "letter eliminator":
                eliminator = LetterEliminator(self.arg_1, self.arg_2)
                print(eliminator.letter_eliminator_main())
            elif action == "dice roller":
                self.dice_sides = input("How many sides? ")
                self.how_many_dice = input("How many to roll? ")
                self.roller = DiceRoller(self.dice_sides, self.how_many_dice)
                self.roller.roll()
            elif action == "help":
                help_instance = Help(self.list_to_print, self.dict_of_commands)
                help_instance.normal()
            elif action == "exit":
                break
            else:
                print("Invalid command. Please try again.")

    def c_commands_headless(self, Command, arg_1, arg_2):
        if Command == "letter eliminator":
            eliminator = LetterEliminator(arg_1, arg_2)
            print(eliminator.letter_eliminator_main())
        elif Command == "dice roller":
            self.roller = DiceRoller(arg_1, arg_2)
            self.roller.roll()
        elif Command == "help":
            pass
        else:
            print(f"Syntax error when calling c_commands_headless. No such command '{self.Command}' exists")
def main():
    run = None,None,None
    c_commands.run
if __name__ == "__main__":
    main()
