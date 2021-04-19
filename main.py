
#################### Coding Question 1 ####################

'''
Q1: War of Numbers

There's a great war between the even and odd numbers. Many numbers already lost their life in this war and it's your task to end this. You have to determine which group sums larger: the even, or the odd. The larger group wins.

Create a function that takes an array of integers, sums the even and odd numbers separately, then returns the difference between sum of even and odd numbers.

Examples

warOfNumbers([2, 8, 7, 5]) ➞ 2
// 2 + 8 = 10
// 7 + 5 = 12
// 12 is larger than 10
// So we return 12 - 10 = 2

warOfNumbers([12, 90, 75]) ➞ 27

warOfNumbers([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]) ➞ 168
Notes
The given array contains only positive integers. 
'''
def war_of_numbers(even_odd):

  even = 0
  odd = 0


  try:
    for num in even_odd:
      if num % 2 == 0:
        even += num
      else:
        odd += num
  except TypeError:
    return None
  return abs(even-odd)

# print(war_of_numbers([2, 8, 7, 5]))
# print(war_of_numbers([12, 90, 75]))
# print(war_of_numbers([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]))
# print(war_of_numbers([2, 8, 7, ""]))

#################### Coding Question 2 ####################

'''
Q2: Switcharoo

Create a function that takes a string and returns a new string with its first and last characters swapped, except under two conditions:

If the length of the string is less than two, return "Incompatible.".
If the first and last characters are the same, return "Two's a pair.".
Examples
flipEndChars("Cat, dog, and mouse.") ➞ ".at, dog, and mouseC"

flipEndChars("ada") ➞ "Two's a pair."

flipEndChars("Ada") ➞ "adA"

flipEndChars("z") ➞ "Incompatible."
Notes
Tests are case sensitive (e.g. "A" and "a" are not the same character). 
'''
def flip_end_chars(string_val):
  if len(string_val) < 2:
    return "Incompatible."

  new_string = ""
  new_string += string_val[-1]
  new_string += string_val[1:-1]
  new_string += string_val[0]
  # print(new_string)

  if new_string == string_val:
    return "Two's a pair."
  else:
    return new_string

# flipEndChars("The")

# print(flip_end_chars("Cat, dog, and mouse."))
# print(flip_end_chars("ada"))
# print(flip_end_chars("Ada"))
# print(flip_end_chars("z"))

#################### Logic Question 1 ####################

'''
Q1: If you have a three-gallon jug and a five-gallon jug, how can you measure out exactly four gallons of water? 
'''

def fill(jugLim):
  return jugLim

def transfer(jug_trans_to_lim, jug_trans_to, jug_trans_from):
  
  while(jug_trans_to != jug_trans_to_lim and jug_trans_from != 0):
    jug_trans_to += 1
    jug_trans_from -= 1

  return jug_trans_to, jug_trans_from

def empty():
  return 0

def jug_print(jug1, jug1_lim, jug2, jug2_lim):
  print("%d/%d %d/%d" % (jug1, jug1_lim, jug2, jug2_lim))

# jug1 = 0
# jug2 = 0
# JUG1_LIM = 3
# JUG2_LIM = 5

# jug2 = fill(JUG2_LIM)
# jug1, jug2 = transfer(JUG1_LIM, jug1, jug2)
# jug1 = empty()
# jug1, jug2 = transfer(JUG1_LIM, jug1, jug2)
# jug2 = fill(JUG2_LIM)
# jug1, jug2 = transfer(JUG1_LIM, jug1, jug2)



# jug_print(jug1, JUG1_LIM, jug2, JUG2_LIM)

#################### Logic Question 2 ####################

'''
Q2: A farmer needs to cross the river with his fox, his chicken, and a bag of corn. However, the boat can only fit the farmer and one other thing at a time. The problem is, the fox and the chicken are both hungry, so if he leaves the fox and chicken together, the fox might eat the chicken. If he leaves the chicken and corn together, the chicken might eat the corn. 
'''

class river():
  def __init__(self):
  #   self.side1_fox = True
  #   self.side1_chicken = True
  #   self.side1_corn = True
  #   self.farmer_fox = False
  #   self.farmer_chicken = False
  #   self.farmer_corn = False
  #   self.side2_fox = False
  #   self.side2_chicken = False
  #   self.side2_corn = False
    self.fox = "side1"
    self.chicken = "side1"
    self.corn = "side1"
    self.farmer_location = "side1"

  def print(self):
    if self.fox == "side1":
      print("The fox has not crossed the river")
    elif self.fox == "farmer":
      print("The fox is with the farmer")
    elif self.fox == "side2":
      print("The fox has crossed the river")
    
    if self.chicken == "side1":
      print("The chicken has not crossed the river")
    elif self.chicken == "farmer":
      print("The chicken is with the farmer")
    elif self.chicken == "side2":
      print("The chicken has crossed the river")
    
    if self.corn == "side1":
      print("The corn has not crossed the river")
    elif self.corn == "farmer":
      print("The corn is with the farmer")
    elif self.corn == "side2":
      print("The corn has crossed the river")

    if self.farmer_location == "side1":
      print("The farmer has not crossed the river")
    elif self.farmer_location == "side2":
      print("The farmer has crossed the river")

    print()

  def pickup(self, item):

    if item == "fox":
      location = self.fox
    elif item == "chicken":
      location = self.chicken
    elif item == "corn":
      location = self.corn

    if self.fox == "farmer":
      print("Cannot pick up %s, already carrying %s" % (item, "fox"))
      return
    elif self.chicken == "farmer":
      print("Cannot pick up %s, already carrying %s" % (item, "chicken"))
      return
    elif self.corn == "farmer":
      print("Cannot pick up %s, already carrying %s" % (item, "corn"))
      return

    if self.farmer_location != location:
      print("Cannot pick up %s, farmer and %s are on opposite sides" % (item, item))
      return

    if item == "fox":
      self.fox = "farmer"
    elif item == "chicken":
      self.chicken = "farmer"
    elif item == "corn":
      self.corn = "farmer"

  def drop(self):
    if self.fox == "farmer":
      self.fox = self.farmer_location
    elif self.chicken == "farmer":
      self.chicken = self.farmer_location
    elif self.corn == "farmer":
      self.corn = self.farmer_location
    else:
      print("Nothing to drop!")
    
  def cross(self):
    if self.farmer_location == "side1":
      self.farmer_location = "side2"
    elif self.farmer_location == "side2":
      self.farmer_location = "side1"

    if self.fox == self.chicken and self.farmer_location != self.fox:
      print("The fox ate the chicken!")
      print("Resetting...")
      self.fox = "side1"
      self.chicken = "side1"
      self.corn = "side1"
      self.farmer_location = "side1"
      return
    elif self.chicken == self.corn and self.farmer_location != self.chicken:
      print("The chicken ate the corn!")
      print("Resetting...")
      self.fox = "side1"
      self.chicken = "side1"
      self.corn = "side1"
      self.farmer_location = "side1"
      return

  def win_condition(self):
    if self.fox == "side2" and self.chicken == "side2" and self.corn == "side2" and self.farmer_location == "side2":
      return True
    else:
      return False

#################### End of Class ####################

def game_simulation(game):
  while(not game.win_condition()):
    try:
      command = input("Enter an action (If you need a list of actions, type help): ")
      print()
      command = command.lower()
      tokens = command.split()
    except KeyboardInterrupt:
      print("\nReceived shutdown request, exiting")
      break

    try:
      if tokens[0] == "help":
        print("pickup [fox, chicken, corn]")
        print("drop")
        print("cross")
      elif tokens[0] == "pickup":
        if tokens[1] != "fox" or tokens[1] != "chicken" or tokens[1] != "corn":
          game.pickup(tokens[1])
      elif tokens[0] == "drop":
        game.drop()
      elif tokens[0] == "cross":
        game.cross()
      else:
        print("Invalid Option")


    except:
      print("Unexpected Input or Behavior")

    game.print()
  if (game.win_condition()):
    print("You helped the farmer cross the river with all their items!")

# game = river()
# game.print()
# game_simulation(game)

# test.pickup("chicken")
# test.cross()
# test.drop()
# test.cross()
# test.pickup("corn")
# test.cross()
# test.drop()
# test.pickup("chicken")
# test.cross()
# test.drop()
# test.pickup("fox")
# test.cross()
# test.drop()
# test.cross()
# test.pickup("chicken")
# test.cross()
# test.drop()
