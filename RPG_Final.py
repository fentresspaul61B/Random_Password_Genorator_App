# to start the code, run:
# Final.py in the terminal
# Tests are included in
# The Final_Test.py file

import random
import string
import datetime
from tkinter import *
import csv

# bellow are all of the functions used throughout the program. The functions
# with Button in the label are called when buttons in the user interface are
# pressed, and the other functions are used for the backend of the program.

def Label_Button():
    global myLabel1
    myLabel1.destroy()
    LABEL.clear()
    myLabel1 = Label(root, text = e.get())
    myLabel1.grid(row=2, column=3)
    LABEL.insert(0, e.get())
    print(LABEL)
    e.delete(0, END)

def Username_Button():
    global myLabel2
    USERNAME.clear()
    myLabel2.destroy()
    myLabel2 = Label(root, text = e.get())
    myLabel2.grid(row=3, column=3)
    USERNAME.insert(1, e.get())
    print(USERNAME)
    e.delete(0, END)

def myDelete():
    myLabel3.grid_forget()

def Password_Button():
    global myLabel3
    myLabel3.destroy()
    global COUNT
    PASSWORD.clear()
    characters = '!@#$%^&*()_+{}:"<>?|'
    Upper_Case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    low2 = 18; high2 = 26
    s = random.uniform(low2, high2) // 2
    A = random.choice(characters)
    B = random.choice(Upper_Case)
    Code = str(random_pw_generator(str(A), str(B)))
    # Code = str(random_pw_generator(0, int(s) , str(A), str(B)))
    PASSWORD.insert(0, Code)
    myLabel3 = Label(root, text = Code)
    if COUNT < 1:
        myDelete()
        COUNT = 1 + COUNT
        myLabel3.grid(row=4, column=3)

        # PASSWORD.insert(0, Code)
    else:
        myDelete()
        # myLabel3.destroy()
        # myLabel3 = Label(root, text = Code)
        COUNT = 1 + COUNT
        # Code = str(random_pw_generator(0, int(s) , str(A), str(B)))

        # myLabel3.grid(row=4, column=3)
        # PASSWORD.insert(0, Code)
        print(PASSWORD)
    # PASSWORD.insert(0, Code)
    myLabel3.grid(row=4, column=3)
    # myButton3['state'] = DISABLED
    print(PASSWORD)
    e.delete(0, END)

# The save function is used to add items to the running global list called
# LIST_OF_ACCOUNTS. This is the main list used in order to display items on
# the user interface, and to save them as data. Each item in the list is a
# dictionary.

def Save_Button():
    new_dict = {}
    new_dict = {'Updated in': str(date_time.strftime("%A, %B, %d, %Y")), 'Account Name': str(LABEL[0]), "Username" : str(USERNAME[0]), 'Password': str(PASSWORD[0])}
    MY_KEYS.append(LABEL[0])
    LIST_OF_ACCOUNTS.append(new_dict)
    e.delete(0, END)
    COUNT = 0
    myButton3['state'] = NORMAL
    myButton2['state'] = NORMAL
    myButton['state'] = NORMAL

def Clear_Button1():
    myLabel1.destroy()
    error.destroy()
def Clear_Button2():
    myLabel2.destroy()
    error.destroy()
def Clear_Button3():
    myLabel3.destroy()
    error.destroy()
def Clear_Button():
    Clear_Button1()
    Clear_Button2()
    Clear_Button3()

# The random_pw_generator function bellow is the main function
# used to create the random passwords. It utilizes the random
# module. The length can be specified by the user. This function
# is tested.

def random_pw_generator(must_include1, must_include2):
    global scale_widget
    max_length = scale_widget.get()
    min_length = max_length/2
    characters = '!@#$%^&*()_+{}:"<>?|'
    low = 4; high = 365
    low2 = 0; high2 = 2
    small_ran_number = random.uniform(low2, high2) // 2
    ran_number1 = random.uniform(min_length, max_length)
    ran_number2 = random.uniform(low // ran_number1, high // ran_number1)
    ran_number3 = (ran_number1 // ran_number2)
    ran_letters1 = random.choice(string.ascii_letters)
    ran_characters = random.choice(characters)
    for i in range(int(min_length) , int(max_length)):
        passcode = str(ran_number3) + str(ran_number1) + str(ran_characters) + (str(ran_letters1) * 10) + must_include1 + must_include2

    l = list(passcode)
    random.shuffle(l)
    result = ''.join(l)
    result = result.replace(".", "")
    if max_length <= 3:
        return print("The length of your password must be greater than 3.")
    if len(result) > max_length:
        L2 = list(result)[:max_length - 2]
        L2.insert(0, must_include1)
        L2.insert(1, must_include2)
        random.shuffle(L2)
        pw = ''.join(L2)
    return pw

# the split function is used to break down a string in a list of all of its
# characters. This is a helper function used within the search functions.

def split(word):
    return [char for char in word]

# The search_func3 function is a function used to check if a keyword exists
# inside of a dictionary. The reason we use this function rather than the
# built in dictionary class, is because we were only able to display a single
# value per key, so this was a way to return multiple values if we had
# multiple accounts under the same label, like multiple Google accounts for
# example.
# If the keyword is contained in the dictionary that means we have hit
# our search result. And report true.

def search_func3(keyword, dct):
    # keyword = keyword.lower()
    # dct = str(dct).lower()
    split_lst = split(dct["Account Name"] + dct["Username"]).lower()
    split_key = split(keyword).lower()
    check =  all(item in split_lst for item in split_key)
    if len(keyword) < 1:
        return False
    elif check == True:
        return True
    else:
        return False

# Using list comprehension, the keep_search function utilizes the split and
# search_func3 functions.
# by applying the search_func3 to every item in the LIST_OF_ACCOUNTS.
# we keep the items from the list that contain the search word.

def keep_search(keyword, lst_of_dictionaries):
    L = [x for x in lst_of_dictionaries if search_func3(keyword,x)]
    # myButton10['state'] = DISABLED
    return L

def search_func_Button():
    global Search_Label
    Search_Label.destroy()
    Search_Label = Label(root)
    Clear_Button()
    key = e.get()
    SEARCHLST = keep_search(key, LIST_OF_ACCOUNTS)
    myButton['state'] = DISABLED
    myButton2['state'] = DISABLED
    myButton3['state'] = DISABLED
    myButton7['state'] = DISABLED
    global Display_Lst
    Search_Label.destroy()
    Display_Lst = []
    for i in range(len(SEARCHLST)):
        Search_Label = Label(root, text = SEARCHLST[i])
        Display_Lst.append(Search_Label)
        Search_Label.grid(row= i + 2, column=3)
    myButton10['state'] = DISABLED


# Here is one of the main features, which is the ability to upload your current
# accounts to a csv file in the same folder as the python program. In order to
# see how this works, you must create your own csv file titled "userhistory.csv"
# Then, when you hit the save CSV button, when you open your csv file, it will
# contain all of your accounts.

def save_csvfile():
    csv_column = ['Updated in','Account Name','Username','Password']
    new_list = []
    for x in range(0,len(LIST_OF_ACCOUNTS)):
        new_list.append(LIST_OF_ACCOUNTS[x])
    filename = 'userhistory.csv'
    with open(filename,'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = csv_column)
            writer.writeheader()
            writer.writerows(new_list)

def display_my_lsts_func():
    Clear_Button()
    myButton['state'] = DISABLED
    myButton2['state'] = DISABLED
    myButton3['state'] = DISABLED
    myButton10['state'] = DISABLED
    global Display_Lst
    Display_Lst = []
    print(LIST_OF_ACCOUNTS)
    for i in range(len(LIST_OF_ACCOUNTS)):
        Lst_Label = Label(root, text = LIST_OF_ACCOUNTS[i])
        Display_Lst.append(Lst_Label)
        Lst_Label.grid(row= i + 2, column=3)
        print(Lst_Label)

# Another list we use is called Display_Lst, and it is used to keep track of all the items from
# list of accounts, so we can add and remove them in an iterative manner.
# LIST_OF_ACCOUNTS is global, and is constantly getting mutated as we use the
# the program so we needed a permanent record of each item of LIST_OF_ACCOUNTS
# in order to display items on the screen, and remove them without bugs.

def hide_my_lsts_func():
    myButton['state'] = NORMAL
    myButton2['state'] = NORMAL
    myButton3['state'] = NORMAL
    myButton7['state'] = NORMAL
    myButton10['state'] = NORMAL
    global Display_Lst
    for i in range(len(LIST_OF_ACCOUNTS)):
        print("entering for loop")
        Lst_Label = Display_Lst[i]
        Lst_Label.destroy()
        Search_Label = Display_Lst[i]
        Search_Label.destroy()

"""USER INTERFACE BELLOW"""
#user interface module is called tkinter and everything bellow
# is how we create buttons, and data entry boxes

from tkinter import *
root = Tk()
root.title("Random Password")
root.geometry("1000x300")
e = Entry(root)
e.grid(row=1, column= 0)
e.get()

# we have multple global lists that keep track of items like the curent USERNAME
# and a list of the items to display to the screen. We had to utizile many lists
# because in order to display something onto the screen, it must be done in an
# iterative order, otherwise the last item on the screen would be displayed
# ontop of the previous item, which caused bugs.
# We used global lists to update the Label, Username, and Password. This
# means the item 0 of these lists, is always the current account information.
# This is how new accounts are created, and then stored.

input_lst = []
LABEL = []
USERNAME = []
PASSWORD = []
SEARCH = ""
LIST_OF_ACCOUNTS = []
COUNT = 0
myLabel1 = Label(root)
myLabel2 = Label(root)
myLabel3 = Label(root)
error = Label(root, text = "Needs more account information")
Lst_Label = Label(root)
Search_Label = Label(root)
MY_KEYS = []
new_dict2 = {}
date_time = datetime.datetime.now()

# All of the buttons are bellow:

myButton = Button(root, text = "Account Name", padx = 25, command = Label_Button)
myButton.grid(row= 2, column= 0)

myButton2 = Button(root, text = "Username", padx = 25, command = Username_Button)
myButton2.grid(row= 3, column= 0)

myButton3 = Button(root, text = "Password", padx = 25, command = Password_Button)
myButton3.grid(row= 4, column= 0)


scale_widget = Scale(root, orient="horizontal", resolution=1,
                        from_=10, to=20)
label_1 = Label(root, text="Set Password Length")
label_1.grid(row=5, column=0)
scale_widget.grid(row=6, column=0)

myButton4 = Button(root, text = "Save", padx = 25, command = Save_Button)
myButton4.grid(row= 1, column= 1)

myButton5 = Button(root, text = "Clear", padx = 25, command = Clear_Button1)
myButton5.grid(row= 2, column= 1)

myButton5 = Button(root, text = "Clear", padx = 25, command = Clear_Button2)
myButton5.grid(row= 3, column= 1)

myButton5 = Button(root, text = "Clear", padx = 25, command = Clear_Button3)
myButton5.grid(row= 4, column= 1)

myButton5 = Button(root, text = "Clear All", padx = 25, command = Clear_Button)
myButton5.grid(row= 10, column= 0)

myButton7 = Button(root, text = "Show My Accounts", padx = 25, command = display_my_lsts_func)
myButton7.grid(row= 11, column= 0)

myButton8 = Button(root, text = "Hide My Accounts", padx = 25, command = hide_my_lsts_func)
myButton8.grid(row= 12, column= 0)

myButton9 = Button(root, text = "Save CSV File", padx = 25, command = save_csvfile)
myButton9.grid(row= 13, column= 0)

myButton10 = Button(root, text = "Search", padx = 25, command = search_func_Button)
myButton10.grid(row= 14, column= 0)

def myDelete():
    myLabel3.grid_forget()

# def search_func_2(keyword, lst):
#     global Display_Lst
#     Display_Lst = []
#     print(len(lst))
#     count = 0
#     # key = e.get()
#     search_lst = split(keyword)
#     print(search_lst)
#     for i in range(len(lst)):
#         print(lst[i])
#         split_account = (lst[i][keyword])
#         print(split_account)
#         # print("hello")
#         for x in range(len(split_account)):
#             # print(split(split_account))
#             if split_account[x] in search_lst :
#                 print(split_account[x])
#                 # print(search_lst)
#                 count += 1
#                 print(count)
#                 if count >= len(search_lst):
#                     Lst_Label = Label(root, text = lst[i])
#                     Display_Lst.append(Lst_Label)
#                     Lst_Label.grid(row= i + 2, column=3)
#                     return True

root.mainloop()

# the root.mainloop ends the user interface. So everything that we want to to
# within the user interface must be above this line, and bellow
# the root = TK further up
