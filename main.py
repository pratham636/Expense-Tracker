from queries import insert,delete,update,select_all,group_up,sumary
def show():
    print("Enter your number from the given choices:\n" \
                "Insert the product, choose 1\n" \
                "Delete the product, choose 2\n" \
                "Update the product, choose 3\n" \
                "See all the product, choose 4\n" \
                "See all the product with respect to catagory, choose 5\n" \
                "See summary , choose 6\n" \
                "Choose 7 for Exit \n")
def main():   
    try:
        choose=input("Enter your choose = ")
        if choose=="1":
            result=insert()
            print(result)
        elif choose=="2":
            result=delete()
            print(result)
        elif choose=="3":
            result=update()
            print(result)
        elif choose=="4":
            result=select_all()
            for i in result:
                print(i)
        elif choose=="5":
            result=group_up()
            for i in result:
                print(i)
        elif choose=="6":
            result=sumary()
            for i in result:
                print(i)
        elif choose=="7":
            print("Exiting program")
            exit()
        else:
            print("You select wrong number.")
    except Exception as e:
        print(f"The error is = {e}")

while True:
    show()
    main()
