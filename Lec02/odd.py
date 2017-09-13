
odd = 0;
even = 0

for i in range(1,24, 2):    
    
    if(i%2 == 1):
        if(i > odd):
            odd = i
    else:
        even = i
    

if(odd == 0):
    print("Nothing")
else:
    print(odd)