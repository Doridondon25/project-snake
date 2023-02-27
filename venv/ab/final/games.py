import sqlite3
import  tkinter.messagebox
import hashlib

class Game(object):
    def __init__(self, tablename = "Games", Game_id = "Game_id", user_id1 = "user_id1", user_id2 = "user_id2", score_1 = "score_1", score_2 = "score_2"):
        self.__tablename = tablename
        self.__Game_id = Game_id
        self.__user_id1 = user_id1
        self.__user_id2 = user_id2
        self.__score_1 = score_1
        self.__score_2 = score_2
        conn = sqlite3.connect('magar.db')
        print ("Opened database successfully")
        str = "CREATE TABLE IF NOT EXISTS " + self.__tablename + "(" + self.__Game_id + " " + "INTEGER PRIMARY KEY AUTOINCREMENT ,"
        str += " " + self.__user_id1 + " INTEGER     NOT NULL ,"
        str += " " + self.__user_id2 + " INTEGER     NOT NULL, "
        str += " " + self.__score_1 + " INTEGER     NOT NULL, "
        str += " " + self.__score_2 + " INTEGER     NOT NULL )"
        conn.execute(str)
        print("Table created successfully");
        conn.commit()
        conn.close()
    def get_table_name(self):
        return self.__tablename
    def select_all_users(self):
        try:
            conn = sqlite3.connect('magar.db')
            print("Opened database successfully");
            str1 = "select*from " + self.__tablename
            print(str1)
            cursor = conn.execute(str1)
            rows = cursor.fetchall()
            arr_games = []
            for row in rows:
                str_rows = str(row[0]) + " " + row[1] + " " + str(row[2])
                arr_games.append(str_rows)
            print(arr_games)
            return arr_games
        except:
            return False

    def insert_game(self, user_id1, user_id2, score_1, score_2):
        try:
            conn = sqlite3.connect('magar.db')
            str_insert = "INSERT INTO " + self.__tablename + " (" + self.__user_id1 + "," + self.__user_id2 + "," + self.__score_1 + "," + self.__score_2+ ") VALUES (" + "'" + str(user_id1) + "'" + "," + "'" + str(user_id2) + "'" + "," + "'" + str(score_1) + "'" + "," + "'" + str(score_2) + "'" + ");"
            print(str_insert)
            conn.execute(str_insert)
            conn.commit()
            conn.close()
            print("Record created successfully");
        except:
            print("Failed to insert game")


    def delete_by_id(self, id):
        try:
            conn = sqlite3.connect('magar.db')
            str_delete = "DELETE  from " + self.__tablename + " where " + self.__Game_id + "=" + "'"+str(id)+"'"
            print(str_delete)
            conn.execute(str_delete)
            conn.commit()
            conn.close()
            print("Record deleted successfully")
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

    def __str__(self):
        return "table  name is ", self.__tablename

u=Game()
#u.insert_game(12,109,123,122)
#u.insert_game(12,109,123,12234)
#u.delete_by_id(3)