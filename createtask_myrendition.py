#This program randomly generates a color, style, and thing to draw based on user input. 
# This tool can help artists warm up, or even for those that have trouble thinking of things to draw.

#lists input into the call function
#the first value in the list is the name of the list (which is called in the function)
categories = {
    1: ['color',"red", "orange", "yellow", "green", "blue", "purple"],
    2: ['style',"comic", "realistic", "painterly", "anime", ""],
    3: ['thing',"a basket of fruit", "a woman", "a man", "cats and dogs", "technology from the year 2100"]
}
#create a list to insert the values that you choose, the numbers are place holders
my_parameters = [1,2,3]

# conditional statement
random_idea = input("Would you like to generate something random to draw? Yes/No")

#set the variables to be used in the function
#random idea is the value from above (Yes/No)
#p1, p2, and p3 are the list inserted
#your_parameters is the list to insert the values you choose

def randomization(random_idea,dictionary,your_parameters):
    for v in range(3):
        if random_idea == "Yes":category[p1][1]
            #ask the user for a number (which will be the index of the list mentioned)
            #insert the value from above into the "empty" function at position 0
            iv = int(input(f"Choose a number between 1 and 5 to get a random {categories[pv][0]}!"))
            your_parameters.insert(0,p1[iv])
            v += 1
            pv = 

    #print the 3 randomly chosen factors
            print(f"Your random categories are {your_parameters}. Have fun drawing!")
        else:
            print("That's fine. Maybe next time!")

#call the function
randomization(random_idea,categories,my_parameters)
