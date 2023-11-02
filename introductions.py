#Write a function that two pieces of input (2 people), and introduces one to another
#Prompt the user for 2 names
#call your function, which should then print an introduction: introducing one person to the other

def introduce(person1, person2):
    return person1 + " allow me to introduce you to " + person2 + "!"

p1= input("Name a person: ")
p2= input("Name another person: ")

print(introduce(p1, p2))

#p1 and p2 are the arguments
# person1 and person 2 are parameters

        