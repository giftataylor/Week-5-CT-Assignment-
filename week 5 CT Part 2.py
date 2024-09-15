# Part 2: Book Club Points Award System

# Ask the user for the number of books purchased
books_purchased = int(input("Enter the number of books purchased this month: "))

# Determine points based on the number of books purchased
if books_purchased == 0:
    points = 0
elif books_purchased == 2:
    points = 5
elif books_purchased == 4:
    points = 15
elif books_purchased == 6:
    points = 30
elif books_purchased >= 8:
    points = 60
else:
    points = 0

# Display the points awarded
print(f"Points awarded: {points}")
