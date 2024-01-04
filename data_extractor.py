def get_email(text):
    '''Extract the email addresses from the text'''
    # Seperate the text into a list 
    text = text.split()
    # Filter and find all words containing a @ symbol
    email_list = [x for x in text if "@" in x]

    return(email_list)


def get_username(email_list):
    '''Extract usernames from the email addresses'''
    # Split each email address at the @ symbol and keeps the first part
    usernames = [email.split('@')[0] for email in email_list]
    return usernames


def main():
    email_header = '''----------Example Incomplete Header---------- 
    Date: Fri, 29 May 03 08:53:48 EST 
    From: MyFriend@friendly.com 
    Subject: NEW! 600K Hot List... No AOL 
    Reply-To: yourfriend@nowhere.com 
    --------End Example Incomplete Header-------- '''

    # Extract email addresses from the header
    email_addresses = get_email(email_header)
    # Extract usernames from the email addresses
    usernames = get_username(email_addresses)

    print(usernames)

    
if __name__ == "__main__":
    main()














# def get_username(email):
#     atsign = email.find("@")
#     username = email[:atsign]
#     return username

# print(get_username(email_header))

