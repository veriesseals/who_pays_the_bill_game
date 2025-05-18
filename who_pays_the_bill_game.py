# import random
# ----------------------------------------------------------
import random

# 1st method
# ----------------------------------------------------------
# Who pays the bill?
# This is a simple game where players take turns to pay the bill.

# List of friends
# ----------------------------------------------------------
friends = ["Alice", "Bob", "Charlie", "David"]

# Use the random.choice function to select a random friend
# ----------------------------------------------------------
if random.choice(friends):
    print(f"{random.choice(friends)} is going to pay the bill!")

# ----------------------------------------------------------

# 2nd method
# ----------------------------------------------------------
# Who pays the bill?
# This is a simple game where players take turns to pay the bill.
# List of friends
# ----------------------------------------------------------
friends = ["Alice", "Bob", "Charlie", "David"]
# Use the random.randint function to select a random friend
# ----------------------------------------------------------
random_friend = random.randint(0, 3)
print(f"{friends[random_friend]} is going to pay the bill!")