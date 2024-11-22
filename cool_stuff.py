import random as r
class DiceRoller:
    def __init__(self, dice_sides, how_many_dice):
        self.dice_sides = int(dice_sides)
        self.how_many_dice = int(how_many_dice)
        self.result = {}
        #import random as r
    def roll(self):
        for i in range(self.how_many_dice):
            self.result.update({i+1: r.randint(1, self.dice_sides)}) 
        print(self.result)

class print_list:
    def __init__(self, list_to_print, leading_words, trailing_words):
        self.list_to_print = list_to_print
        output = ""
        for i in range(len(self.list_to_print)):
            output += self.list_to_print[i] + ""
            if i < len(self.list_to_print)-1:
                output += ", "
        print(leading_words + output + trailing_words)

class Help:
    def __init__(self, list_of_commands, dict_of_commands):
        self.list_of_commands = list_of_commands
        self.dict_of_commands = dict_of_commands
        
    def normal(self):

        print_list(self.list_of_commands, "Welcome to help \nList of commands: ", "\n")
        

        action = input("What would you like help with? \nCommand: ").lower()
        

        if action in self.dict_of_commands:
            print(self.dict_of_commands[action])  
        else:
            print("Command not found.")  
        
        
        
        pass



class letter_eliminator:
    def __init__(self, word, ttc):
        self.word = word
        self.ttc = ttc
        result = ""
    def letter_eliminator_main(self):
        for i in self.word:
            if self.is_this_character_in_a_string(i, self.ttc, False):
                result += i
        return(result)

    def is_this_character_in_a_string(self, inp, cool, bopo):
        for letters in cool:
            if letters == inp:
                return bopo
        return not bopo

class cedars_sub_commands:
    def __init__(self, Command, arg_1, arg_2):
        self.list_to_print = list(("letter eliminator", "Dice Roller", "Help", "exit"))
        self.dict_of_commands = {
            "letter eliminator" : 'Removes letters from words',
            "dice roller"       : 'Rolls a specifed # of dice with a specifid # of sides ',
            "help"              : 'Tells you what my commands do \nyou are here',
        }
        self.Command = Command
        self.arg_1 = arg_1
        self.arg_2 = arg_2

        def c_commands(self):
            while 1:
                print("")
                leading_words = "Cedar's commands("
                trailing_words = "):\n"
                print_list(self.list_to_print, leading_words, trailing_words)
                
                self.action = (input("what do you want to do? \n"))
                self.action = self.action.lower()
                if self.action == "letter eliminator":
                    eliminator = letter_eliminator(word, ttc)
                    eliminator.letter_eliminator_main()
                elif self.action == "roll dice":
                    self.dice_sides = input("how many dice sides? ")
                    self.how_many_dice = input("how many to roll? ")
                    self.roller = DiceRoller(self.dice_sides, self.how_many_dice)
                    self.roller.roll()
                elif self.action ==  "help":
                    help_instance = Help(self.list_to_print, self.dict_of_commands)
                    help_instance.normal()  # Call normal method on the instance
                elif self.action == "exit"
                    break

                else:
                    pass
                  
        def c_commands_headles(self, Command, arg_1, arg_2):
            if Command == "letter eliminator":
                eliminator = letter_eliminator(arg_1, arg_2)
                eliminator.letter_eliminator_main()
            elif Command == "roll dice":
                self.dice_sides = arg_1
                self.how_many_dice = arg_2
                self.roller = DiceRoller(self.dice_sides, self.how_many_dice)
                self.roller.roll()
            elif Command ==  "help":
                pass
            print("Syntax error when calling c_commands_headles \n \nNo sutch command " + self.Command + " exists"
