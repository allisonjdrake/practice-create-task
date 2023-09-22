#This program randomly generates a color, style, and thing to draw based on user input. 
# This tool can help artists warm up with a fun, random topic,
    #  or assist those that have trouble thinking of things to draw (such as myself).

#set different categories as lists in a dictionary (with their keys being 1, 2, and 3)
#the first value in the list is the name of the list (which is called in the function)
categories = {
    1: ['color',"red", "orange", "yellow", "green", "blue", "purple"],
    2: ['style',"superhero comicbook style", "realistic", "cartoonish", "anime", "surrealist", "child-like (scribbly)"],
    3: ['thing',"a basket of fruit", "a woman", "a man", "cats and dogs", "technology from the year 2100"]
}
# empty list to insert the values that you choose
my_parameters = []

# conditional statement
random_idea = input("Would you like to generate something random to draw? Yes/No")

#set the variables to be used in the function: the true/false statement from above, the dictionary, and an empty list
def randomization(random_idea,dictionary,your_parameters):
#establish variables to use in the for loop
    i=1
    key = i
    v = 0
   
    if random_idea == "Yes":
        
        for key in categories:
#ask the user for a number (which will be the index it's inputted at)
            iv = int(input(f"Choose a number between 1 and 5 to get a random {categories[i][0]}!"))
#insert the value from above into the "empty" function at position v (established above)
            your_parameters.insert(v,categories[i][iv])
#increase each variable to continue the loop and choose for the next category
            i+=1
            v+=1
#print the newly created list
        print(f"Your random categories are {your_parameters}. Have fun drawing!")
    
    else:
        print("That's fine. Maybe next time!")

#call the function
randomization(random_idea,categories,my_parameters)
