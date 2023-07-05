def new_contact():
    contact = ["\n"]
    fp = open("contact.txt","a+")
    name = input("Enter contact name: ")
    contact.append(name+"\n")
    tel = input("Enter phone num. :")
    contact.append(tel+"\n")
    email_ = input("Enter email: ")
    contact.append(email_+"\n")
    fp.writelines(contact)
    fp.close()
def delete():
    pass
def modify():
    pass
def contactList():
    fp = open("contact.txt","r+")
    data = fp.readline(1)
    print(data)
    fp.close()
while (True):
    print("\n*******************CONTACT BOOK************************")
    print("\nChoose an option: ")
    print("\n1)-add a contact\n2)-modify a contact\n3)-delete a contact\n4)-contact list")
    choice = int(input("\nChoice: "))
    if choice == 1:
        new_contact()
    elif choice == 2:
        modify()
    elif choice == 3:
        delete()
    elif choice == 4:
        contactList()
    else:
        print("invalid choice restart!!!")                