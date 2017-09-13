
print("You are in a Forest")
print("\n********************\n********************")
print(" :)")
print("********************\n********************\n")

counter = 0
go = input("Go Left or Right?")

while go == "right":
    counter += 1
    
    if counter > 2:
        print("\n\t :( \t_|___|_")
    else:
        print("\n\t :(")
    
    go = input("You are lost again. Go Left or Right?")
    
print("You got out")