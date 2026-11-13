favourites = []

print("Let's create a list of your favourite items.")
favourites.append(input("Enter your first favourite item: "))
favourites.append(input("Enter your second favourite item: "))
favourites.append(input("Enter your third favourite item: "))

print("\nHere is your list of favourite items:")
for index, item in enumerate(favourites, start=1):
    print(f"{index}. {item}")
