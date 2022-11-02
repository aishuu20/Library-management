import databaseofbook as bookdb

while True:
    print(''' ----------------------LIBRARY MANAGEMENT--------------------------------
     Choose the operation to be performed :
    1. Add Books
    2. Update Books 
    3. Delete Books
    4. Return Books
    5. Issue Books
    6. Show Books
    7. search book
    8. showissue book
    9. showreturn book
    10.Exit
    ''')

    choice = int(input("Enter Your Choice : ")) 

    if choice == 10:
        break
    elif choice == 1:
        ID = int(input('Enter Book ID : '))
        Name = input('Enter Name of the Book : ')
        Author_name = input("Enter Author of the book : ")
        Price = eval(input('Enter Price of the Book : '))
        Type = input('Enter Type of the book (Fictional,Non-Fictional,story,motivational) : ')
        result = bookdb.insertbook(ID,Name,Author_name,Price,Type)
        print(result)
    elif choice == 2:
        id = int(input("Enter ID of the book to be updated : "))
        data = list(bookdb.searchbook(id))
        #print(data)

        print(''' What do you want to update? 
        1. Name of the book
        2. Price of the book
        3. Author of the book 
        4. Type of the book ''')
        choose = int(input('Enter your choice : '))
        if choose==1:
            name = input("Enter new name of the book : ")
            data[1] = name
        elif choose==2:
            Price = eval(input("Enter new price of the book : "))
            data[3] = Price
        elif choose==3:
            author_name = input("Enter new name of the author : ")
            data[2] = author_name
        elif choose==4:
            type = input("Enter type of the book : ")
            data[4] = type
        result = bookdb.updatebook(data)
        print(result)
        print(data)
    elif choice == 3:
        id = int(input("Enter ID of the book to be deleted : "))
        result = bookdb.deletebook(id)
        print(result)
    elif choice == 4:
        stuid = int(input("Enter student id : "))
        ID = int(input("Enter Book id : "))
        name = input("Enter name of the book : ")
        issuedate = input("Enter issue date : ")
        returndate = input("Enter return date : ")
        result = bookdb.returnbook(stuid,ID,name,issuedate,returndate)
        print(result)
    elif choice == 5:
        stuid = int(input("Enter student id : "))
        stuname = input("Enter student name : ")
        ID = int(input("Enter book id : "))
        name = input("Enter name of the book : ")
        issuedate = input("Enter date : ")
        result = bookdb.issuebook(stuid,stuname,ID,name,issuedate)
        print(result)
    elif choice == 6:
        datalist = bookdb.showbook()
        for i in datalist:
            print(f'ID: {i[0]}\tName: {i[1]}\tAuthor_name: {i[2]}\tPrice: {i[3]}\tType: {i[4]}')
    elif choice == 7:
        id = int(input("Enter Id of the book : "))
        data = bookdb.searchbook(id)
        print(f'ID: {data[0]}\tName: {data[1]}\tAuthor: {data[2]}\tPrice: {data[3]}\tType: {data[4]}')

    elif choice == 8:
        datalist = bookdb.showissuebook()
        for i in datalist:
            print(f'stuid: {i[0]}\tstuname: {i[1]}\tID: {i[2]}\tBookname: {i[3]}\tissuedate: {i[4]}')

    elif choice == 9:
        datalist = bookdb.showreturnbook()
        for i in datalist:
            print(f'stuid: {i[0]}\tID: {i[1]}\tBookname: {i[2]}\tissuedate: {i[3]}\treturndate: {i[4]}')