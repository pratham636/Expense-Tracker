import mysql.connector
from database import connection
def insert():
    try:
        name=input("Enter the name of product = ")
        price=float(input("Enter the price of product = "))
        category=input("Enter the categoty of product = ")
        date=input("Enter the date of product buy = ")
        
        db=connection()
        mycursor=db.cursor()
        query="INSERT INTO expenses(name,price,category,date) VALUES (%s,%s,%s,%s);"
        value=mycursor.execute(query,(name,price,category,date))
        db.commit()
        mycursor.close()
        db.close()
        return ("Data insert successfully completed.")
    except Exception as e:
        return (f"The error is = {e}")

def delete():
    try:
        db=connection()
        mycursor=db.cursor()
        id=int(input("Enter the id : "))
        query="DELETE FROM expenses WHERE id=%s"
        value=mycursor.execute(query,(id,))
        db.commit()
        mycursor.close()
        db.close()
        return ("Data is successfully deleted.")
    except Exception as e:
        return (f"The error is = {e}")
def update():
    try:
        print("Enter your number from the given choices:\n" \
        "Change name of produce choose 1\n" \
        "Change price of produce choose 2\n" \
        "Change category of produce choose 3\n" \
        "Change date of produce choose 4\n")
        choice=input("Enter your choice = ")
        db=connection()
        mycursor=db.cursor()
        if choice=="1":
            id_p=int(input("Enter the id of product which want to change = "))
            change=input("Enter new name of product = ")
            query="UPDATE expenses SET name=%s WHERE id=%s;" 
            value=mycursor.execute(query,(change,id_p))
        elif choice=="2":    
            id_p=int(input("Enter the id of product which want to change = "))
            change=input("Enter new price of product = ")
            query="UPDATE expenses SET price=%s WHERE id=%s;" 
            value=mycursor.execute(query,(change,id_p))    
        elif choice=="3":    
            id_p=(input("Enter the id of product which want to change = "))
            change=input("Enter new categoty of product = ")
            query="UPDATE expenses SET category=%s WHERE id=%s;" 
            value=mycursor.execute(query,(change,id_p))    
        elif choice=="4":
            id_p=int(input("Enter the id of product which want to change = "))
            change=input("Enter new date price of product = ")
            query="UPDATE expenses SET date=%s WHERE id=%s;" 
            value=mycursor.execute(query,(change,id_p))    
        else:
            print("You choose wrong number")
        db.commit()
        mycursor.close()
        db.close()
        return ("Data is successfully updated.")
    except Exception as e:
        return (f"The error is = {e}")

def select_all():
    try:
        db=connection()
        mycursor=db.cursor()
        query="SELECT * FROM expenses"
        mycursor.execute(query)
        result=mycursor.fetchall()
        mycursor.close()
        db.close()
        return result

    except Exception as e:
        return [f"The error is = {e}"]

def group_up():
    try:
        db=connection()
        mycursor=db.cursor()
        query="SELECT category,sum(price) as 'Totle',AVG(price) as 'AVG' , COUNT(*) AS 'Count' FROM expenses GROUP BY catagory;"
        mycursor.execute(query)
        result=mycursor.fetchall()
        mycursor.close()
        db.close()
        return result
    except Exception as e:
        return [f"The error is = {e}"]
 
def sumary():
    try:
        db=connection()
        mycursor=db.cursor()
        query="SELECT sum(price) as 'Totle',AVG(price) as 'AVG' , COUNT(*) AS 'Count',max(price) as 'Highest expenses' FROM expenses;"
        mycursor.execute(query)
        result=mycursor.fetchall()
        mycursor.close()
        db.close()
        return result
    except Exception as e:
        return [f"The error is = {e}"]
        
        
