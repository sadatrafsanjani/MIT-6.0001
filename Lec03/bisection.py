
cube = 27
epsilon = 0.01
tries = 0
low = 0
high = cube

guess = (low+high)/2.0

while abs(guess**3 - cube) >= epsilon:
    
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (low+high)/2.0
    tries += 1
    
print("Bi-Section Method")
print("Number of guesses:", tries)
print(guess, "is close to the cube root of", cube)
    
    