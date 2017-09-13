
root = 27
epsilon = 0.01
tries = 0
low = 0
high = root

guess = (low+high)/2.0

while abs(guess**2 - root) >= epsilon:
    
    if guess**2 < root:
        low = guess
    else:
        high = guess
    guess = (low+high)/2.0
    tries += 1
    
print("Bi-Section Method")
print("Square root of", root , "is", guess)
print("Number of guesses:", tries)
    
    