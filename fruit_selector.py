mysteryFruits = ["apple" , "banana", "blueberry", "kiwi", "mango", "orange", "peach", "pineapple", "raspberry", "strawberry"]
selectedFruits = []
counter = 0
moreFruit = "yes"


while moreFruit == "yes" and counter < 6  :
    fruits = input("What fruit would you like to add to your drink? ")
    while len(fruits) < 4 :
      print ("Your fruit must be at least 4 characters long!")
      fruits = input("What fruit would you like to add to your drink? ")
    counter = counter + 1
    selectedFruits.append(fruits)
    moreFruit = input("Would you like to add another fruit yes/no ? ")
    while moreFruit != "yes" and moreFruit != "no" :
        print("You must reply yes or no!")
        moreFruit = input("Would you like to add another fruit yes/no ? ")
    

import random
randomNumber = random.randint(0,9)

print("The fruits you entered were ")
for index in range(len(selectedFruits)) :
  print(selectedFruits[0 + (index)])

print("The mystery fruit is " + mysteryFruits[randomNumber])
counter = counter + 1

if counter < 3 :
  print("Your drink should be a milkshake")
elif counter == 3 or counter == 4 :
  print("Your drink should be a smoothie")
else :
  print("Your drink should be a fruit juice")