
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

word = input("I will cheer for you. Give me a word:")
times = int(input("Enthusiasm level (1-10):"))

for char in word:
    if char in letters:
        print("Give me an", char, "!", char)
    else:
        print("Give me a", char, "!", char)
        
for i in range(times):
    print(word)