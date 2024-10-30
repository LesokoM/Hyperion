class Email:

    has_been_read = False #setting has been read to false

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        #creating objects 
      
    def __repr__(self):
        #whenever i  want to print my object it will give me the subject line
    
        subject_list =self.subject_line
        subject_list.split(",")
        return  subject_list
    
    def get_email_address(self):
        #fetch email adress
        return self.email_address

    def get_subject_line(self):
        #fetch subject line
        return self.subject_line

    def get_content(self):
        #fetch content 
        return self.email_content

    def mark_as_read(self): 
        
        #we put self in as a parameter because it will change the been reade
        #for that specifc object self is pointing to; chnaging the status of that email 
        self.has_been_read = True        

#now theyre called functions not instances 

def populate_inbox():
    
    global program_startup
    if program_startup == False:
            #creating the first 3 emails to go inside inbox 
        new_email = Email("hyperion@gmail.com", "Welcome to HyperionDev!", "We love having you here. Welcome to our platform")
        inbox.append(new_email)
        new_email = Email("hyperion@gmail.com", "Great work on the bootcamp", "You have successfully completed the bootcamp")
        inbox.append(new_email)
        new_email = Email("hyperiongrad@gmail.com", "Your excellent marks!", "Your marks have now been uploaded onto the portal")
        inbox.append(new_email)
        program_startup = True
        return
    #whenever we need to create new email objects we run the below code ONLY (if statement wont run on same script )
    email_address = input("Please enter email address: ")
    subject_line = input("Please enter subject line for email: ")
    email_content = input("Please enter email content: ")
    new_email = Email(email_address, subject_line, email_content)
    inbox.append(new_email)

def list_emails():
    #list emails using index method
    for email in inbox: 
        
        print(f"{inbox.index(email)} {email}")

def read_email(i):
    selected_email = inbox[i]
    print("--------------------------------")
    print(f"Email is from: {selected_email.get_email_address()}")
    print(f"Subject: {selected_email.get_subject_line()}")
    print(f"Content: {selected_email.get_content()}")
    print("--------------------------------")

    selected_email.mark_as_read()

def menu():
    populate_inbox()
    while True: #as long as we dont exit function leave everything to run as normal 

        menu_option = int(input('''
    Please select an option: 
        1. Read an email 
        2. View Unread emails
        3. Quit Application
        >>'''))

        if menu_option == 1:
            list_emails()
            index = int(input("Please enter position you want to read: "))
            read_email(index)

        elif menu_option == 2:
            for mail in inbox:
                if mail.has_been_read == False: #accessing class variable using dot notation only prining emails that are unread 
                    print(f">> {inbox.index(mail)} {mail}") 

        elif menu_option ==3:
            print("Goodbye...")
            exit()
        else:
            print("Incorrect menu chosen")

inbox = [] #inbox will hold email objects should be outside
program_startup = False

menu()

