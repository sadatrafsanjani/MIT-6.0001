
def isIn(s1, s2):
    if (s1 in s2) or (s2 in s1):
        return True
    else:
        return False
    
if isIn("Dragunov", "Dragunov is a sniper rifle"):
     print("Yes")
else:
    print("No")
    