def parsed(self, response):
    # emails list of uniqueemail set
    emails = list(self.uniqueemail)
    finalemail = []
 
    for email in emails:
        # avoid garbage value by using '.in' and '.com'
        # and append email ids to finalemail
        if ('.in' in email or '.com' in email or 'info' in email or 'org' in email):
 
            finalemail.append(email)
 
    # final unique email ids from geeksforgeeks site
    print('\n'*2)
    print("Emails scraped", finalemail)
    print('\n'*2)
