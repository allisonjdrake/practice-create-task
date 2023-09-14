restaurants = ["in n out", "mcdonalds", "chick fil a", "jack in the box", "taco bell"]

#make sure it's description for both input and output - user understands input and output
new_res = input("what restaurant would you like to rank into your list?")

#making function with parameters makes the code "reuseable" (one of the requirements)
def rank_restaurant(new_res, restaurants):
    for i in range (len(restaurants)):
        rank = input(f"do you like A) {new_res} or B) {restaurants[i]} more A/B?")
        if rank == "A":
            restaurants.insert(i, new_res)
            break
        elif rank == "B":
            continue
    return restaurants

    if new_res not in restaurants:
        restaurants.append(new_res)
print(f"Your new ranking of restaurants is {rank_restaurant(new_res, restaurants)}")
