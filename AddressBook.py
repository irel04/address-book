# CMPE 3022 Programming Logic and Design

print(f'\n{"***** This programming script is made by *****" : >62}')
print(f'{"***** Irel Kian Bacolod and Uriel Esmeralda *****" : >65}\n')


print("-" * 85)
print('|' + " " * 30 + " ADDRESS BOOK " + " " * 38 + ' |')
print("-" * 85)


# Def function for printing menu
def menu():
    print("-" * 85)
    print('|' + " " * 25 + " What would you like to do? " + " " * 29 + ' |')
    print("-" * 85)
    print('|' + " " * 25 + " 1. ADD CONTACT " + " " * 41 + ' |')
    print('|' + " " * 25 + " 2. EDIT CONTACT " + " " * 40 + ' |')
    print('|' + " " * 25 + " 3. DELETE CONTACT " + " " * 38 + ' |')
    print('|' + " " * 25 + " 4. VIEW CONTACT " + " " * 40 + ' |')
    print('|' + " " * 25 + " 5. SEARCH ADDRESS BOOK " + " " * 33 + ' |')
    print('|' + " " * 25 + " 6. EXIT PROGRAM " + " " * 40 + ' |')
    print("-" * 85)


# Some major variables for storing lists and running the whole program
menu()
option = input("\nChoose an option: ")
start = 0
contact_list = [" "]
firstname_storage = [" "]
lastname_storage = [" "]
address_storage = [" "]
addcontact_storage = [" "]


# Def Function for updating the contact list everytime the user will make changes
def view_update():
    if contact_list != [" "]:
        contact_list.pop(0)
        order = 0
        if option == "3":
            order = 0
        for i in contact_list:
            order += 1
            print(str(order) + ".", i)
        contact_list.insert(0, " ")
        return contact_list
    elif contact_list == [" "]:
        print("No contacts found. Please add now!!!")


# Def Function for search
def search():
    choose = input("\nChoose from above (letters from a to d): ")
    count = 0
    search_found = []
    if choose == "a":
        info_type = input("Enter First Name: ")
        for j in firstname_storage:
            if info_type in j:
                for i in contact_list:
                    if info_type in i:
                        search_found.append(i)
                        count += 1
    elif choose == "b":
        info_type = input("Enter Last Name: ")
        for j in lastname_storage:
            if info_type in j:
                for i in contact_list:
                    if info_type in i:
                        search_found.append(i)
                        count += 1
    elif choose == "c":
        info_type = input("Enter Address: ")
        for j in address_storage:
            if info_type in j:
                for i in contact_list:
                    if info_type in i:
                        search_found.append(i)
                        count += 1
    elif choose == "d":
        info_type = input("Contact Number: ")
        for j in addcontact_storage:
            if info_type in j:
                for i in contact_list:
                    if info_type in i:
                        search_found.append(i)
                        count += 1
    else:
        print("Invalid Option!!!")

    if choose == "a" or choose == "b" or choose == "c" or choose == "d":
        if count == 0:
            print("\n" + " " * 3 + "<<<<<<<< Search Result: Contact not found. "
                                   "Doesn't match any information >>>>>>>>\n")
        elif count > 0:
            print("\n" + " " * 3 + "<<<<<<<< Search Result: {} contact/s found >>>>>>>>\n".format(count))
            for i in search_found:
                print("   " + i)


# Body of whole program where decisions, options, and other operations are executed
while start == 0:
    # if statement for starting the program and prompting the user
    if option == "":
        menu()
    # Elif statement for adding contacts
    elif option == "1":
        print("-" * 85)
        print('|' + " " * 30 + " ADD CONTACT/S " + " " * 37 + ' |')
        print("-" * 85)
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        address = input("Enter address: ")
        add_contact = input("Enter contact number: ")
        complete = "NAME: " + first_name + " " + last_name + " " * (45 - len(first_name + last_name)) + \
                   "CONTACT NUMBER: " + add_contact + "\n" + "   " + "ADDRESS: " + address + "\n"
        firstname_storage.append(first_name)
        lastname_storage.append(last_name)
        address_storage.append(address)
        addcontact_storage.append(add_contact)
        contact_list.append(complete)
        repeat = input("\nDo you want to add more contact? (y/n): ")
        if repeat == 'y':
            continue
        elif repeat == 'n':
            print(" ")
            menu()
        else:
            print("Invalid Option!!!!!\nPlease choose in the menu")
            print(" ")
            menu()
    # Elif statement for editing contacts
    elif option == "2":
        print("-" * 85)
        print('|' + " " * 30 + " EDIT CONTACT/S " + " " * 37 + '|')
        print("-" * 85)
        view_update()
        try:
            index = input("\nChoose the number you want to edit: ")
            contact_list.pop(int(index))
            firstname_storage.pop(int(index))
            lastname_storage.pop(int(index))
            address_storage.pop(int(index))
            addcontact_storage.pop(int(index))
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            address = input("Enter address: ")
            add_contact = input("Enter contact number: ")
            complete = "NAME: " + first_name + " " + last_name + " " * (45 - len(first_name + last_name)) + \
                       "CONTACT NUMBER: " + add_contact + "\n" + "   " + "ADDRESS: " + address + "\n"
            firstname_storage.insert(int(index), first_name)
            lastname_storage.insert(int(index), last_name)
            address_storage.insert(int(index), address)
            addcontact_storage.insert(int(index), add_contact)
            contact_list.insert(int(index), complete)
        except IndexError:
            print("\nInvalid Input")
        except ValueError:
            print("\nInvalid Input")
        repeat = input("\nDo you want to edit other contacts? (y/n): ")
        if repeat == 'y':
            continue
        elif repeat == 'n':
            print(" ")
            menu()
        else:
            print("Invalid Option!!!!!\nPlease choose in the menu")
            print(" ")
            menu()
    # Elif statement for deleting and moving forward the contacts
    elif option == "3":
        print("-" * 85)
        print('|' + " " * 28 + " DELETE CONTACT/S " + " " * 36 + ' |')
        print("-" * 85)
        view_update()
        try:
            index = input("\nChoose a number to delete (Type Del to delete all): ")
            if index == "Del" or index == "del":
                contact_list.clear()
                firstname_storage.clear()
                lastname_storage.clear()
                address_storage.clear()
                addcontact_storage.clear()
                contact_list.append(" ")
                firstname_storage.append(" ")
                lastname_storage.append(" ")
                address_storage.append(" ")
                addcontact_storage.append(" ")
                print("\n" + " " * 25 + "<<<<<<<< UPDATED CONTACT/S >>>>>>>>\n")
                view_update()
                enter = input("\nPress Enter to continue")
                print(" ")
                menu()
            elif int(index) > 0:
                contact_list.pop(int(index))
                firstname_storage.pop(int(index))
                lastname_storage.pop(int(index))
                address_storage.pop(int(index))
                addcontact_storage.pop(int(index))
                repeat = input("\nDo you want to delete more? (y/n): ")
                if repeat == "y":
                    continue
                elif repeat == "n":
                    print("\n" + " " * 25 + "<<<<<<<< UPDATED CONTACT/S >>>>>>>>\n")
                    view_update()
                    enter = input("\nPress Enter to continue")
                    print(" ")
                    menu()
        except IndexError:
            print("\nInvalid Input")
        except ValueError:
            print("\nInvalid Input")
    # Elif statement for viewing contacts
    elif option == "4":
        print("-" * 85)
        print('|' + " " * 28 + " VIEW CONTACT/S " + " " * 38 + ' |')
        print("-" * 85)
        view_update()
        enter = input("\nPress Enter to continue")
        print(" ")
        menu()
    # Elif statement for searching contacts
    elif option == "5":
        print("-" * 85)
        print('|' + " " * 28 + " SEARCH CONTACT/S " + " " * 36 + ' |')
        print("-" * 85)
        print("What information do you want to search on?")
        print("a. First Name")
        print("b. Last Name")
        print("c. Address")
        print("d. Contact Number")
        search()
        enter = input("\nPress Enter to continue")
        print(" ")
        menu()
    # Elif statement for terminating the program
    elif option == "6":
        terminate = input("Are you sure you want to end the program (y/n)? ")
        if terminate == "y":
            break
        elif terminate == "n":
            print(" ")
            menu()
        else:
            print("Invalid Option!!!!!\nPlease choose in the menu")
            print(" ")
            menu()
    else:
        print("Invalid Option!!!!!\nPlease choose in the menu")
        print(" ")
        menu()
    option = input("\nChoose an option: ")
print(f'\n{"-" * 34 + " End of Program " + "-" * 34}')
