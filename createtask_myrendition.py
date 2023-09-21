#lists input into the call function
#the first value in the list is the name of the list (which is called in the function)
#the rest of the values are whatever random options you want for that category
color = ['color',"red", "orange", "yellow", "green", "blue", "purple"]
style = ['style',"comic", "realistic", "painterly", "anime", ""]
thing = ['thing',"a basket of fruit", "a woman", "a man", "cats and dogs", "technology from the year 2100"]

#create a list to insert the values that you choose, the numbers are place holders
my_parameters = [1,2,3]

#determine the output of the function
random_idea = input("Would you like to generate something random to draw? Yes/No")

#set the variables to be used in the function
#random idea is the value from above (Yes/No)
#p1, p2, and p3 are the list inserted
#your_parameters is the list to insert the values you choose

def randomization(random_idea,p1,p2,p3,your_parameters):
    if random_idea == "Yes":
        #ask the user for a number which will be the index of the first list (p1)
        #insert the value from above into the "empty" function at position 0
        i1 = int(input(f"Choose a number between 1 and 5 to get a random {p1[0]}!"))
        your_parameters.insert(0,p1[i1])

        i2 = int(input(f"Choose another number between 1 and 5 to get a random {p2[0]}!"))
        your_parameters.insert(1,p2[i2])

        i3 = int(input(f"Choose a number between 1 and 5 to get a random {p3[0]}!"))
        your_parameters.insert(2,p3[i3])

#print the 3 randomly chosen factors
        print(f"Your random {p1[0]} is {your_parameters[0]}." 
        f" Your random {p2[0]} is {your_parameters[1]}." 
        f" Your random {p3[0]} is {your_parameters[2]}.")
    else:
        print("That's fine. Maybe next time!")
#use random_idea from the prompt above the function
#use three specified lists of values
#enter a list to append
randomization(random_idea,color,style,thing,my_parameters)
