
number = 81
root = 0
power = 0


for guess in range(abs(number) + 1):
    if guess**2 >= abs(number):
        root = guess
        break
    
if guess**2 != abs(number):
    print(number, "is not a perfect root!")
else:
    for i in range(1, 6):
        if root**i == abs(number):
            power = i
        
    if number < 0:
        guess = -guess

if guess != 0 and power != 0:
    print("Root:",str(guess), "Power", str(power))
else:
    print("Not Found")