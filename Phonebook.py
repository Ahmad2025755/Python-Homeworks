import sys

def initial_phonebook():

    rows , col = int(input("Please enter initial number of contacts:")), 5

    phone_book = []

    print(phone_book)

    for i in range(rows): 

        print("\n Enter contact %d details in the following order ONLY: "%(i+1))
        print("................................................................")

        temp = []

        for j in range(col):

            if j == 0:
                temp.append(str(input("Enter Name")))


            if j < len(temp) and (temp[j] == '' or temp[j] == ''):
                sys.exit("Name is a mandatory field. Process exiting due to blank field...")
        

        if j == 1:
            temp.append(str(input("Enter number*:")))

        
        if j == 2:
            temp.append(str(input("Enter e-mail address:")))

            if temp[j] == "" or temp[j] == '0':
                temp[j] = None

    phone_book.append(temp)

def menu():
    print("***************************************")
    print("\tYou can now perform the following operations on this phonebook\n")
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit phonebook")
    choice = int(input("Please enter your choice:"))
    return choice



def add_content(pb):

            dip = []

            for i in range(len(pb[0])):

                if i == 0 :
                   dip.append(str(input("Enter name:")))

                if i == 1 :
                    dip.append(str(input("Enter number:")))

                if i == 2 :
                    dip.append(str(input("Enter your e-mail address:")))

                if i == 3 :
                    dip.append(str(input("Enter your date of birth (dd/mm/yy):")))

                if i == 4 :
                    dip.append(str(input("Enter category (Friend/Family/Work/Others):")))

            pb.append(dip)

            return pb


def remove_existing():
    query = str(input("Please enter the name of the contact you wish to remove:"))

    temp = o

    for i in range(len(pb)):
        if query == pb [i][0]:

            temp += 1

            print(pb.pop(i))

            print("This query now has been removed...")

            return pb

            if temp == 0:

              print("Sorry, you have entered an invalid query, \n please recheck and try again later.")

            return pb



def delete_all(pb):

    return pb.clear()   


def search_existing(pb):

    choice = int(input("Enter search criteria\n\n\n 1. Name\n2. Number\n3. Email-id\n4. DOB\n5. Category(Family/Friends/Work/Others)\ \nPlease enter:"))

    temp = []
    check = -1

    if choice == 1:
        query = str(input("Please enter the name of the contact you wish to search:"))

        for i in range(len(pb)):
            if query == len(pb[i][0]):
               check = i
               temp.append(pb[i])


    elif choice == 2:

        query = int(input("Please enter the number of the contact you wish to search:"))
        for i in range(len(pb)):
            if query == len(pb[i][1]):
               check = i
               temp.append(pb[i])


    elif choice == 3:

        query = int(input("Please enter the email ID of the contact you wish to search:"))
        for i in range(len(pb)):
            if query == len(pb[i][2]):
               check = i
               temp.append(pb[i])

    elif choice == 4:

        query = int(input("Please enter the DOB (dd/mm/yyyy format only) of the contact you wish to search:"))
        for i in range(len(pb)):
            if query == len(pb[i][3]):
               check = i
               temp.append(pb[i])

    elif choice == 5:

        query = int(input("Please enter the category of the contact you wish to search:"))
        for i in range(len(pb)):
            if query == len(pb[i][4]):
               check = i
               temp.append(pb[i])


    else:

        print("Invalid search criteria")
        return -1

    if check == -1:
           return -1

    else:
        display_all(temp)
        return check



def display_all(pb):
    if not pb:


                print("List is empty: []")


    else:
          for i in range(len(pb)):
              print(pb[i])


def thanks():

    print("**************************************************")
    print("Thank you for using our smartphone directory system!")
    print("Please visit again!")
    print("**************************************************")
    sys.exit("Goodbye, have a nice day ahead!")


    print(".........................................................")
    print("Hello dear, welcome to our smartphone directory system.")
    print("You made proceed to explore this directoryb system")



ch = 1
pb = initial_phonebook()



while ch in (1 , 2, 3 , 3 , 4 , 5):
 

    ch = menu()

    if ch == 1:
        pb = add_contact(pb)

    elif ch == 2:
        pb = remove_existing(pb)

    elif ch == 3:
        pb = delete_all(pb)

    elif ch == 4:
        d = search_existing(pb)

    if d == -1:
        print("The contact doesn't exist, pealse try again later.")
    
    elif ch == 5:
        display_all(pb)

    else:
        thanks()








