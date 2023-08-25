import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

usr_tbl = """
            CREATE TABLE IF NOT EXISTS users (
                fname TEXT,
                lname TEXT,
                username TEXT,
                hpass TEXT,
                email TEXT
            )
            """

cmd_add_usr = "INSERT INTO users VALUES('{}', '{}', '{}', '{}', '{}')"
cmd_chk_usrnm_exists = "SELECT 1 FROM users WHERE username = '{}'" #supposed to return either (1,) or None


connection = sqlite3.connect("DBs/userlogins.db", check_same_thread=False)

def connect_cursor():
    cursor = connection.cursor()
    cursor.execute(usr_tbl)
    return cursor


cc = connect_cursor()


def chk_usr_exists(usrnm):
    cc.execute(cmd_chk_usrnm_exists.format(usrnm))
    return cc.fetchone()

#add registered user to DB
def add_usr(fname, lname, usrnm, pswd, email):
    hashedpass = generate_password_hash(pswd)           #hashed password using werkzeug
    cc.execute(cmd_add_usr.format(fname, lname, usrnm, hashedpass, email))
    connection.commit()

#validate login, allow to proceed on matching credentials
def chk_login(usrnm, pswd):
    hpass = cc.execute("SELECT hpass FROM users WHERE username = '{}'".format(usrnm)).fetchone()            #will fail if username doesn't exist
    #print(hpass[0])            #debug print
    return check_password_hash(hpass[0], pswd)  # hashed password using werkzeug
