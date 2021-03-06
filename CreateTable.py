import sqlite3 as sql

def main():
    try: 
        db = sql.connect('BukuTelepon.db')
        cur = db.cursor()
        tablequery = "CREATE TABLE PENGGUNA (id INT, Nama TEXT, Marga TEXT, Kota TEXT, Telepon TEXT, Email TEXT)"

        cur.execute(tablequery)
        print("Table Created Succesfully")

    except sql.Error as e:
        print("There is a table or an error has occurred")

    finally:
        db.close()
        
if __name__ == "__main__":
    main()