# Authentification Related Stuff

import hashlib

# Read and Write to Usernames and Passwords
# ===============================================================
def read_usernames():
    f = open("data/username.csv", "r")
    raw = f.read().strip().split("\n")
    f.close()
    for i in raw: print i # Debugging
    return raw

def read_passwords():
    f = open("data/password.csv", "r")
    raw = f.read().strip().split("\n")
    f.close()
    for i in raw: print i # Debugging
    return raw

def write_data(username, password):
    u = open("data/username.csv", "r")
    p = open("data/password.csv", "r")
    uraw = u.read().strip()
    praw = p.read().strip()
    u.close()
    p.close()
    uraw += "\n" + username
    praw += "\n" + encrypt(password)
    u = open("data/username.csv", "w")
    p = open("data/password.csv", "w")
    u.write(uraw)
    p.write(praw)
    u.close()
    p.close()

def clear_data(): # For Database Initialization Use Only
    u = open("../data/username.csv", "w")
    p = open("../data/password.csv", "w")
    u.write("")
    p.write("")
    u.close()
    p.close()

# Encryption
# ===============================================================
def encrypt(password):
    # We all need more salt in our lives
    hashed = password + "733f8d6d68ab4e5bd46a3ab56186311b3bfd3705f2f4029f0f3e06a6e91f03d89b94d1546c669b0aceb10cd5000ca4d0"
    return hashlib.sha384(hashed).hexdigest()

# Verification
# ===============================================================
def verify(username,password):
    usernames = read_usernames()
    passwords = read_passwords()
    try:
        row = usernames.index(username)
    except:
        return -2 
    if (encrypt(password) == passwords[row]):
        return 1
    return -1

def register(username,password):
    usernames = read_usernames()
    plen = len(password)
    ulen = len(username)

    # Possible Errors
    if username in usernames:
        return -1 # Username Already Exists
    for ch in username:
        c = ord(ch)
        if (c < 48 or
            (c > 57 and c < 65) or
            (c > 90 and c < 97) or
            c > 122):
            return -2 # Invalid Username
    if (ulen < 2):
        return -5 # Short Username
    if (ulen > 32):
        return -6 # Long Username
    if (plen < 4):
        return -3 # Short Password
    if (plen > 64):
        return -4 # Long Password

    # Success
    write_data(username,password)
    return 1

# Database Clearing
# ===============================================================
if __name__ == "__main__":
    print "Clearing database..."
    clear_data()
