import mysql.connector
def connection():
    try:
        db=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=your_real_password,
            database="expenses_tracker"
        )
    except Exception as e:
        print(f"The error is : {e}")
        return None;
    return db;
# def change_table(db):
#     try:
#         mycursor=db.cursor()
#         # mycursor.execute("INSERT INTO expenses(name,price,catagory,date) VALUES ('apple',2.34,'food','2025-05-21');")
#         db.commit()
#     except Exception as e:
#         print(f"The error is : {e}")
#         return None;
#     return mycursor;
# def close(db,mycursor):
#     try:    
#         mycursor.close()
#         db.close()
#     except Exception as e:
#         print(f"The error is : {e}")
# #         return None
# db=connection()
# mycursor=change_table(db)
# close(db,mycursor)
