colors = ["red", "orange", "yellow", "green", "blue", "purple", "white", "black", "pink"]
styles = ["comic", "realistic", "painterly", "anime", ""]
objects = ["basket of fruit", "woman", "man", "cats and dogs", "technology from the year 2100"]
your_parameters = []

def randomization(random_idea, colorindex, styleindex, objectindex, your_parameters):
    random_idea = input("Would you like to generate something random to draw? Yes/No")
    if random_idea == "Yes":
        colorindex = int(input("Choose a number between 0 and 5 to get a random color to use!"))
        your_parameters.append(colorindex,colors[colorindex])
        styleindex = int(input ("Choose another number between 0 and 5 to get a random style to draw in!"))
        your_parameters.append(styleindex, styles[styleindex])
        objectindex = int(input("Choose a number between 0 and 5 to get a random object to draw!"))
        your_parameters.append(objectindex, objects[objectindex])
    else:
        print("That's fine. Maybe next time!")
    print(f"Your random color is {your_parameters[0]}." 
    "Your random style to draw in is {your_parameters[1]}." 
    "Your random object to draw is {your_parameters[2]}")
    
print(randomization("Yes",1,2,3,your_parameters))