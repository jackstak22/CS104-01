names = []

while(len(names)<10):
    acceptName = input("Enter Name ")
    names.append(acceptName)

while(len(names)>0):
    print(names.pop(0))

    
