color = ["red", "orange", "yellow", "green", "blue", "purple", "white", "black", "pink"]
style = ["comic", "realistic", "painterly", "anime", ""]
object = ["basket of fruit", "woman", "man", "cats and dogs", "technology from the year 2100"]
your_parameters = []
my_parameters = [1,2,3,4,5,6]
taste = ['good','bad', 'bitter', 'sweet', 'sour']
sound = ['loud', 'quiet', 'sharp', 'mellow', 'angry']
sight = ['fun', 'boring', 'pretty', 'nice', 'terrible']

random_idea = input("Would you like to generate something random to draw? Yes/No")

def randomization(random_idea,color,style,object,your_parameters):
    if random_idea == "Yes":
        i1 = int(input(f"Choose a number between 0 and 5 to get a random {color} to use!"))
        your_parameters.insert(i1,color[i1])

        i2 = int(input(f"Choose another number between 0 and 5 to get a random {style} to draw in!"))
        your_parameters.insert(i2, style[i2])

        i3 = int(input(f"Choose a number between 0 and 5 to get a random {object} to draw!"))
        your_parameters.insert(i3, object[i3])
    else:
        print("That's fine. Maybe next time!")
    print(f"Your random {color} is {your_parameters[0]}." 
    f"Your random {style} to draw in is {your_parameters[1]}." 
    f"Your random {object} to draw is {your_parameters[2]}.")
randomization(random_idea,taste,sound,sight, my_parameters)
