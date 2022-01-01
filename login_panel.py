import tkinter as tkr
from tkinter import ttk
from tkinter import messagebox
from base64 import b64encode,b64decode
from PIL import Image,ImageTk
import os

root = tkr.Tk()
root.title("Login Panel") 
root.geometry("570x325")
filename = 'logindetail.txt'
global count
count=0

def create_file(filename) :
    # Create the file to store user details
    currentpath = os.path.abspath(os.curdir)
    isexist = os.path.isfile(currentpath+'\\'+filename)
    if isexist == False :
        with open(filename, 'w') as f:
            f.write('')
            f.close()

def login(uname,pword,filename) :
    # Checking if username and password matches
    global name
    login_state = False
    UnameMatch = ''
    with open(filename, 'r') as f:
        content = f.readlines()
        for l in content :
            l = l.replace('\n','')
            l = l.split(' | ')
            name,user,pasw = l[0],l[1],l[2]
            pasw = b64decode(pasw).decode('utf-8')
            if uname==user and pword==pasw :
                login_state = True
                messagebox.showinfo("Info", "Login Success !")
                logged_in_page()
            elif uname==user and pword!=pasw :
                login_state = False
                UnameMatch = uname

        if login_state == False and UnameMatch != '' :
            messagebox.showwarning("Error", f"Password entered for username \"{uname}\" is wrong !")
        elif login_state == False :
            messagebox.showwarning("Error", "Username & Password is wrong !")
    f.close()
    clear_login()

def sign_up(uname,pword,filename) :

    # Saving username & password in file
    writename = txt_name.get()
    writeuser = uname
    writepass = b64encode(bytes(pword,'utf-8')).decode('utf-8')
    data = str('{} | {} | {}\n'.format(writename,writeuser,writepass))

    valid = usernameUnique(uname,pword)
    valid_uname = validate_username(uname)
    valid_pword = validate_password(pword)

    if valid == True :
        if valid_uname == True and valid_pword == True :
            with open(filename, 'a') as f:
                f.write(data)
                if f.closed == False :
                    f.close()
            messagebox.showinfo("Info", "SignUp Success !")
            clear_signup()
        else :
            clear_signup()
    else :
        messagebox.showwarning("Error", "Username is already taken !")
        clear_signup()

def usernameUnique(uname,pword) :
    # Return True if username doesn't exist
    valid = True
    with open('logindetail.txt', 'r') as f:
       content = f.readlines()
       for l in content :
           l = l.replace('\n','')
           l = l.split(' | ')
           user= l[0]
           if uname == user :
               valid = False
    
    return valid

def validate_username(uname) :
    # Validate username field
    valid_uname = True
    symbols = ['&','=','-','<','>','+',',']
    if ' ' in uname :
        messagebox.showwarning("Validation", "Username cannot contain spaces !")
        valid_uname = False
    if uname.isdigit() :
        valid_uname = False
        messagebox.showwarning("Validation", "Username cannot be all numbers !")
    for i in symbols :
        if i in uname :
            valid_uname = False
            messagebox.showwarning("Validation", "Username cannot contain   &  =  _  -  <  >  +  ,  ")

    return valid_uname

def validate_password(pword) :
    # Validate password field
    valid_pword = True
    if pword.replace(' ','') == '' :
        valid_pword = False
        messagebox.showwarning("Validation", "Password cannot be all spaces !")
    return valid_pword

def clear_login() : # Clear text fields
    txt_User.delete(0, 'end')
    txt_Pass.delete(0, 'end')
def clear_signup() : # Clear text fields
    txt_User2.delete(0, 'end')
    txt_Pass2.delete(0, 'end')
    txt_name.delete(0, 'end')

def logged_in_page() :
    global tabControl,name
    tabControl.select(2) 
    canvas.itemconfig(nametext, text=f"Welcome {name} !")

def show_login() : # Select login tab 
    global tabControl
    tabControl.select(0) 
def show_signup() : # Select signup tab 
    global tabControl
    tabControl.select(1)
def logout() : # Select login tab when logouts
    global tabControl
    tabControl.select(0)
    canvas.itemconfig(nametext, text="Welcome User !")

def showpass():
    # Show password
    global tabControl,count
    cur = tabControl.index("current")
    count += 1

    if count%2==0 :
        char = '•'
        btn_eye['image'] = unhide_icon
    else :
        char = ''
        btn_eye['image'] = hide_icon

    if cur == 0 :
        txt_Pass.configure(show=char)
    elif cur == 1 : 
        txt_Pass2.configure(show=char)

#####################################################

style = ttk.Style()
style.layout('TNotebook.Tab', [])
global tabControl
tabControl = ttk.Notebook(root,width=631,height=384) 
tab1 = tkr.Frame(tabControl) # tab_index = 0
tab2 = tkr.Frame(tabControl) # tab_index = 1
tab3 = tkr.Frame(tabControl) # tab_index = 2
  
tabControl.add(tab1, text ='Login')
tabControl.add(tab2, text ='SignUp')
tabControl.add(tab3, text ='Profile')
tabControl.grid()

############## Canvas (tab1) ################
canvas = tkr.Canvas(tab1, width = 631, height = 384)
canvas.place(relx=.4, rely=.4,anchor='center')
img = ImageTk.PhotoImage(Image.open(r"green_3-wallpaper-1366x768.jpg"))
bgimg = canvas.create_image(20, 20, anchor='nw', image=img)

unhide_icon = Image.open(r"view.png")
unhide_icon = unhide_icon.resize((20, 20), Image.ANTIALIAS)
unhide_icon = ImageTk.PhotoImage(unhide_icon)

hide_icon = Image.open(r"hidden.png")
hide_icon = hide_icon.resize((20, 20), Image.ANTIALIAS)
hide_icon = ImageTk.PhotoImage(hide_icon)


canvas.create_text(354,90,fill="white",text="Login Form",font=("Helvetica 19 normal"))
canvas.create_text(225,162,fill="white",text="Username :",font=("Helvetica 16 normal"))
canvas.create_text(225,213,fill="white",text="Password :",font=("Helvetica 16 normal"))

############## Canvas (tab2) ################
canvas = tkr.Canvas(tab2, width = 631, height = 384)
canvas.place(relx=.4, rely=.4,anchor='center')
bgimg = canvas.create_image(20, 20, anchor='nw', image=img)

canvas.create_text(354,70,fill="white",text="SignUp Form",font=("Helvetica 19 normal"))
canvas.create_text(225,138,fill="white",text="Name       :",font=("Helvetica 16 normal"))
canvas.create_text(225,189,fill="white",text="Username :",font=("Helvetica 16 normal"))
canvas.create_text(225,240,fill="white",text="Password :",font=("Helvetica 16 normal"))

############## Canvas (tab3) ################
canvas = tkr.Canvas(tab3, width = 631, height = 384)
canvas.place(relx=.4, rely=.4,anchor='center')
bgimg = canvas.create_image(20, 20, anchor='nw', image=img)

nametext = canvas.create_text(354,110,fill="white",text='Welcome User !',font=("Helvetica 23 normal"))
canvas.create_text(354,210,fill="white",text='You are logged in.',font=("Helvetica 16 normal"))

# --------------- Tab1 Widgets (Login)---------------

txt_User = tkr.Entry(tab1,text='',font=("Helvetica 14 normal"))
txt_User.place(relx=.54,rely=.32,anchor='center')
txt_Pass = tkr.Entry(tab1,text='',show='•',font=("Helvetica 14 normal"))
txt_Pass.place(relx=.54,rely=.45,anchor='center')

btn_Login = tkr.Button(tab1,text='Login',font=("Helvetica 13 normal"),width=12,command=lambda:login(txt_User.get(),txt_Pass.get(),filename))
btn_Login.place(relx=.625,rely=.62,anchor='center')

btn_eye = tkr.Button(tab1,text='',font=("Helvetica 13 normal"),borderwidth=0,width=23,height=23,image=unhide_icon,command=lambda:showpass())
btn_eye.place(relx=.739,rely=.45,anchor='center')

switch_signup = tkr.Button(tab1,text='Don\'t have an account?',font=("Helvetica 13 normal"),width=20,command=lambda:show_signup())
switch_signup.place(relx=.34,rely=.62,anchor='center')

# --------------- Tab2 Widgets (SignUp)---------------

txt_name = tkr.Entry(tab2,text='',font=("Helvetica 14 normal"))
txt_name.place(relx=.54,rely=.26,anchor='center')
txt_User2 = tkr.Entry(tab2,text='',font=("Helvetica 14 normal"))
txt_User2.place(relx=.54,rely=.39,anchor='center')
txt_Pass2 = tkr.Entry(tab2,text='',show='•',font=("Helvetica 14 normal"))
txt_Pass2.place(relx=.54,rely=.52,anchor='center')

btn_Signup = tkr.Button(tab2,text='SignUp',font=("Helvetica 13 normal"),width=12,command=lambda:sign_up(txt_User2.get(),txt_Pass2.get(),filename))
btn_Signup.place(relx=.625,rely=.68,anchor='center')

btn_eye = tkr.Button(tab2,text='',font=("Helvetica 13 normal"),borderwidth=0,width=23,height=23,image=unhide_icon,command=lambda:showpass())
btn_eye.place(relx=.739,rely=.52,anchor='center')

switch_login = tkr.Button(tab2,text='Have an account?',font=("Helvetica 13 normal"),width=20,command=lambda:show_login())
switch_login.place(relx=.34,rely=.68,anchor='center')

# --------------- Tab3 Widgets (profile)---------------

btn_logout = tkr.Button(tab3,text='Logout',font=("Helvetica 13 normal"),width=10,command=lambda:logout())
btn_logout.place(relx=.47,rely=.68,anchor='center')

# ---------------------
create_file(filename)

root.mainloop()
