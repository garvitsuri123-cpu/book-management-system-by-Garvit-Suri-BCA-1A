import pandas as pd
bookdf=pd.read_csv('books.csv',sep =",", header=0)

def add_delbook():#function to choose between adding or deleting a book
   
    def addbook():#function to add a book

        num=len(bookdf)#to get the number of rows in the dataframe
        book=(input("enter the name of the book you want to add: ")).upper()#to enter the book name in uppercase
        author=(input("enter the name of the book you want to add: ")).upper()#to enter the author name in uppercase

        bookdf.loc[num+1]=[book,author]#adding the book and author to the dataframe
        print(bookdf)
        print("book added successfully")

    def delbook():#function to delete a book

        bookD = input("enter the name of the book you want to delete: ").upper()#to enter the book name in uppercase
        result = bookdf[bookdf['book'] == bookD]#to check if the book is in the dataframe

        if not result.empty:
            sure=input("are you sure you want to delete this book? y/n: ")#to confirm deletion

            if sure.lower()=='y':
                bookdf.drop(result.index, inplace=True)#deleting the book from the dataframe
                print("Book deleted.")
        else:
            print("book is not available")
        print(bookdf)


    while True:    
        #sub menu for adding or deleting a book   
        print(
            "1: add a book \n" \
            "2: delete a book \n" \
            "3: go back to main menu \n"
        )
        b=int(input("enter your choice: "))
        if b==1:
            addbook()
        elif b==2:
            delbook()
        elif b==3:
            return
        else:
            print("invalid choice")

def search():#function to search for a book or author
    while True:
        #$sub menu for searching a book or author
        choice = int(input("do you want to search for a book or author?\n" \
        "1 for book\n" \
        "2 for author\n" \
        "3 to go back: " 
        ))

        if choice == 1:

            bookS = input("enter the name of the book you want to search: ").upper()#to enter the book name in uppercase
            result = bookdf[bookdf['book'] == bookS]#to check if the book is in the dataframe

            if not result.empty:
                print("Book found:")
                print(result[['book', 'author']])#displaying the book and author
            else:
                print("book is not available")


        elif choice == 2:

            authorS = input("enter the name of the author you want to search: ").upper()#to enter the author name in uppercase
            result = bookdf[bookdf['author'] == authorS]#to check if the author is in the dataframe

            if not result.empty:
                print("Author found:")
                print(result[['book', 'author']])#displaying the book and author
            else:
                print("author is not available")


        elif choice == 3:
            return 
        

        else:
            print("invalid choice")

def display():#function to display all books
    print(bookdf)#displaying the dataframe

def exit():#function to exit the program after saving changes

    sure=input("are you sure you want to exit? y/n: ")#to confirm deletion

    if sure.lower()=='y':
        bookdf.to_csv('books.csv', index=False)# Save changes to CSV before
        print("exiting the program")
        quit()#exit the program

    else:
        return

print("welcome to the book management system \n")
while True:
    #main menu
    a=int(input(
    "1: Add/delete a book \n" \
    "2: search for a book or author \n" \
    "3: display all books \n" \
    "4: exit \n"
    ))

    if a==1:
        add_delbook()
    elif a==2:
        search()
    elif a==3:
        display()
    elif a==4:
        exit()
    else:
        print("invalid choice")
        

#by Garvit Suri of BCA-1A

