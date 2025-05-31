#create an empty dictionary 
countryDb = {}
while True:
    #print menu 
    print("1. Insert")
    print("2. Display all the countries")
    print("3. Display all the capitals")
    print("4. Get capital")
    print("5. Delete")
    #user input 
    choice = int(input("enter your choice (1-5)"))
    if choice == 1:
        country = input("Enter the country : ").upper()
        capital = input("Enter the capital ").upper()
        countryDb[country] = capital
    #display the data of countries 
    elif choice  == 2:
        print(list(countryDb.keys()))
    #display the data of capitals
    elif choice == 3:
        print(list(countryDb.values()))
    # to display specific capital
    elif choice == 4:
        country = input("Enter the country : ").upper()
        print(countryDb.get(country))
    #delete the entry from the dictionary countryDb
    elif choice == 5:
        country = input("Enter the country : ").upper()
        del(countryDb[country])
    #if user choses the wrong option
    else: 
        print("enter the valid choice")
        break



    