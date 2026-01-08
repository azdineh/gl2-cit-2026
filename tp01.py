import random
import string

letters=string.ascii_letters

car=""
while car != "w":
    car=random.choice(letters)
    print(f"La lettre choisie est {car}")