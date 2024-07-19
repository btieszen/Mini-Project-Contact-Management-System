import re
import os

def add_contact(contact):
    
 
        
        name=input("What is the name of the contact you want to add: ")
    
        phone=input("What is the phone number: ")
        match_phone = re.findall(r"[\d]{3}-[\d]{3}-[\d]{3}", phone)
        if match_phone:
            print("Phone number added")
        else:
            print("Invalid phone number pleae enter as xxx-xxx-xxxx")
            phone = input("What is the phone number: ")
  
        email=input("What is the email address: ")
        match_email = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",email)
        if match_email:
            print("Email added")
        else:
            print("Invalid email please enter as xxx@xxxx.xxx" )
            email=input ("What is the email address: ")
    
    
        info=input("Add any Additional information: ")
        contact_list=({"Name":(name),"Phone":(phone),"Email":(email),"Additional Notes":(info)})
        if contact_list in contact:
            print(f"contact alreadt exist")
        else:
            contact.append(contact_list)
        for count, contacts in enumerate(contact, start=1):
            contact_update ={"Contact" : (count)}
            contact_update.update(contacts)
            #print(contact_update)
        
      
        
        

def edit_contact(contact):
     
    editname=input("What contact name would you like to edit: ")
    res = next((sub for sub in contact if sub['Name'] == (editname)),None)
    #print("The edited contact information is : " +str(res))
    print(res) 
    edit_info=input("What would you like to edit: Name, Phone, Email, or Additional Notes: ")
    
    if edit_info=="Name":  
        new_name=input("What is the new contact name: ") 
        res.update({"Name": (new_name)})
        print("The update contact is: ")
        print(res)
    elif edit_info=="Phone":  
        new_phone=input("What is the new phone number (Enter as: xxx-xxx-xxxx): ") 
        res.update({"Phone": (new_phone)})
        print("The update contact is: ")
        print(res)
    elif edit_info=="Email":  
        new_email=input("What is the new Email (Enter as: xxxx@xxxx.xxx): ") 
        res.update({"Email": (new_email)})
        print("The update contact is: ")
        print(res)
    elif edit_info=="Additional Notes":  
        new_notes=input("What Additional Notes would you Like to add: ") 
        res.update({"Additional Notes": (new_notes)})
        print("The update contact is: ")
        print(res)
    else:
        print("Invalid entry")
    
    
def delete_contact(contact):
    delete_name=input("What contact name would you like to delete: ")
    res = next((sub for sub in contact if sub['Name'] == (delete_name)),None)
    res.clear()
    print("Contact has been deleted")
    

def search_contact(contact):
    editname=input("What contact name would you like to search for: ")
    res = next((sub for sub in contact if sub['Name'] == (editname)),None)
    print("The contact information is : " +str(res)) 
        

def display_contact(contact):
   
    print(" Your contacts are: ")
    for count, contacts in enumerate(contact, start=1):
        contact_update ={"Contact" : count}
        contact_update.update(contacts)
        print(contact_update)
       
        #print(f"Contact {count}: {contacts}")
           # initializing update dictionary



def export_contacts(contact):
    add_folder=input("What contact would you like to add to a file: ")
    res = next((sub for sub in contact if sub['Name'] == (add_folder)),None)
    folder=str(res)
    with open((add_folder), 'w') as file:
        file.write(folder)
   

    
def main():
    contact=[]
    while True: 
        print("\nWelcome to the Contact Managment System")
        print("1.  Add a new contact") 
        print("2.  Edit an existing contact")  
        print("3.  Delete a Contact")
        print("4.  Search for a contact")
        print("5.  Display all contacts")
        print("6.  Export contacts to a text file")
        print("7.  Quit")
    
        choice=input("\nPlease make your selection: ")
        
        if choice =="1":
            add_contact(contact)
        elif choice == "2":
            edit_contact(contact)  
        elif choice == "3":
            delete_contact(contact)
        elif choice =="4":
            search_contact(contact)
        elif choice =="5":
            display_contact(contact)
        elif choice=="6":
            export_contacts(contact)
        elif choice=="7":
            print(" Thank you, GOODBYE!!!")
            break
        else:
            print("Not a valid choice please enter a number from 1-7")
            
    


main()
    
