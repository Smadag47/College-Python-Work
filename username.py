def get_username(email):
    atsign = email.find("@")
    username = email[:atsign]
    return username

def main():
    username = get_username("t.wilson@dundeeandangus.ac.uk")
    print(username)

if __name__ == "__main__":
    main()



