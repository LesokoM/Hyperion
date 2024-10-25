class Email:

    has_been_read = False 

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content


    def mark_as_read(self): 
        
        #we put self in as a parameter because it will change the been reade
        #for that specifc object self is pointing to; chnaging the status of that email 
        self.has_been_read = True        

inbox = [] #inbox will hold email objects should be outside
program_startup = False
#now theyre called functions not instances 

def populate_inbox(email_address, subject_line,email_content):
    if program_startup == False:
        for i in range(0,3):
            new_email = Email(email_address, subject_line, email_content)
        program_startup = True
    
    new_email = Email(email_address, subject_line, email_content)
    inbox.append(new_email)

def list_emails()