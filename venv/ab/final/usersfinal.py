import sqlite3
import  tkinter.messagebox
import hashlib
import tkinter as tk
from tkinter import messagebox

class User(object):
    def __init__(self, tablename = "Users", Id = "Id", email = "email", password = "password", firstname = "firstname"):
        self.__tablename = tablename
        self.__Id = Id
        self.__email = email
        self.__password = password
        self.__firstname = firstname
        super().__init__()
        conn = sqlite3.connect('test.db')
        print ("Opened database successfully")
        str = "CREATE TABLE IF NOT EXISTS " + self.__tablename + "(" + self.__Id + " " + "INTEGER PRIMARY KEY AUTOINCREMENT ,"
        str += " " + self.__email + " TEXT    NOT NULL ,"
        str += " " + self.__password + " TEXT    NOT NULL, "
        str += " " + self.__firstname + " TEXT    NOT NULL) "
        conn.execute(str)
        print("Table created successfully");
        conn.commit()
        conn.close()
    def get_table_name(self):
        return self.__tablename
    def select_all_users(self):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully");
            str1 = "select*from " + self.__tablename
            print(str1)
            cursor = conn.execute(str1)
            rows = cursor.fetchall()
            arr_users = []
            for row in rows:
                str_rows = str(row[0]) + " " + row[1] + " " + str(row[2])
                arr_users.append(str_rows)
            print(arr_users)
            return arr_users
        except:
            return False


    def insert_user(self, email, password, firstname):
        if "@" not in email:
            print("Error: Email must contain @")
            #messagebox.showerror("ERROR", "Email must contain @")
            return False
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM " + self.__tablename + " WHERE " + self.__email + " = '" + email + "'")
            if cursor.fetchone():
                print("Error: User already exists")
                return False
            salt = "letsgo"
            md5hash = hashlib.md5(salt.encode('utf-8') + password.encode()).hexdigest()
            str_insert = "INSERT INTO " + self.__tablename + " (" + self.__email + "," + self.__password + "," + self.__firstname + ") VALUES (" + "'" + email + "'" + "," + "'" + md5hash + "'" + "," + "'" + firstname + "');"
            print(str_insert)
            conn.execute(str_insert)
            conn.commit()
            print("Record created successfully")
            return True
        except:
            print("Failed to insert user")
            messagebox.showerror("ERROR", "Failed Register")
            return False

    def delete_by_firstname(self, email):
        try:
            conn = sqlite3.connect('test.db')
            str_delete = "DELETE  from " + self.__tablename + " where " + self.__email + "=" + "'"+str(email)+"'"
            print(str_delete)
            conn.execute(str_delete)
            conn.commit()
            conn.close()
            print("Record deleted successfully")
            return "Success"
        except:
            return "Failed to delete user"

    def return_user_by_email_password(self, email, password):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully")
            salt = "letsgo"
            md5hash = hashlib.md5(salt.encode('utf-8') + password.encode()).hexdigest()
            strsql = "SELECT * from " + self.__tablename + " where " + self.__email + "=" + "'" + str(
                email) + "'" + " and " + self.__password + "=" + "'" + str(md5hash) +"'"
            print(strsql)
            cursor = conn.execute(strsql)
            row = cursor.fetchone()
            conn.commit()
            conn.close()
            if row:
                print("hello" + " " +  row[3])

                return row[3]
            else:
                print("Failed to find user")
                return False
        except:
            return False


    def login_12(self,):
        password = str(self.__password.get())
        arr = User().return_user_by_email_password(email,password)
        try:
            if not User.login_1(email,password):
                self.massage.set("please login")
                messagebox.showerror("error massage", 'error')
                return False
            else:
                self.message.set("welcome, " + arr[3])
                return True
        except:
            messagebox.showerror("error massage", 'error')
            return False

    def show_message_box():
        messagebox.showerror("Error", "Failed")



    def __str__(self):
        return "table  name is ", self.__tablename


u=User()

