
cube = 1000
epsilon = 0.01
guess = 0.0
increment = 0.01
tries = 0

while(abs(guess**3 - cube) >= epsilon) and guess <= cube:
    guess += increment
    tries += 1
print("Number of guesses:", tries)

if abs(guess**3 - cube) >= epsilon:
    print("Failed on cube root of", cube)
else:
    print(guess, "is close to the cube root of", cube)
    