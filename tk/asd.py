from tkinter import *
import tkinter as tk
from tkinter import ttk
from models.client import client
import cfg

root = tk.Tk()
tabControl = ttk.Notebook(root)
tab1 = tk.Frame(tabControl,)
tab2 = tk.Frame(tabControl,)
tabControl.add(tab1, text='User')
tabControl.add(tab2, text='Auth')
tabControl.grid(column=0)


cfg.init()

# Clear Text Fields
def clear_fields():
	accountid_box.delete(0, END)
	email_box.delete(0, END)
	password_box.delete(0, END)
	isocode_box.delete(0, END)
	
def create_user():
	if isocode_box.get() and fr_box.get() and client_id_box.get() and client_sc_box.get()  :
		cfg.myList = {'basic':frtoken.get(),'client_id':client_id.get(),'client_secret':client_secret.get()}
		try:
			text_box.insert(tk.END, "\n"+str(client(email.get(),isocode.get(),accid.get(),passs.get()).create()))
		except Exception as e:
			text_box.insert(tk.END, "\n"+str(e))
	else:
		text_box.insert(tk.END, "\nSe debe completar con el AccountId, isocode, FR token, Client id, Client secret")
	
	
    

email = tk.StringVar()
passs= tk.StringVar()
accid = tk.StringVar()
isocode = tk.StringVar()
frtoken = tk.StringVar()
client_id = tk.StringVar()
client_secret = tk.StringVar()



#Create Main Form To Enter Customer Data
account_label = Label(tab1, text="Accountid").grid(row=1, column=0, sticky=W, padx=10)
accountid_box = Entry(tab1, textvariable=accid)
accountid_box.grid(row=1, column=0, pady=5)

email_label = Label(tab1, text="Email").grid(row=2, column=0, sticky=W, padx=10)
email_box = Entry(tab1, textvariable=email)
email_box.grid(row=2, column=0, pady=5)

password_label = Label(tab1, text="Password").grid(row=3, column=0, sticky=W, padx=10)
password_box = Entry(tab1, textvariable=passs)
password_box.grid(row=3, column=0, pady=5)

isocode_label = Label(tab1, text="Iso2Code").grid(row=4, column=0, sticky=W, padx=10)
isocode_box = Entry(tab1, textvariable=isocode)
isocode_box.grid(row=4, column=0, pady=5)

fr_label = Label(tab2, text="FR token").grid(row=1, column=0, sticky=W, padx=10)
fr_box = Entry(tab2, textvariable=frtoken,width= 50)
fr_box.grid(row=1, column=1, pady=5)

clientid_label = Label(tab2, text="Client id").grid(row=2, column=0, sticky=W, padx=10)
client_id_box = Entry(tab2, textvariable=client_id,width= 50)
client_id_box.grid(row=2, column=1, pady=5,padx=5)

clientsc_label = Label(tab2, text="Client secret").grid(row=3, column=0, sticky=W, padx=10)
client_sc_box = Entry(tab2, textvariable=client_secret,width= 50)
client_sc_box.grid(row=3, column=1, pady=5,padx=5)

#Create a textBox
text_box = tk.Text(tab1, height=10, width= 100)
text_box.grid(row=22, column=0, pady=15,padx=30)


# Create Buttons

clear_fields_button = Button(tab1, text="Clear Fields", command=clear_fields)
clear_fields_button.grid(row=15, column=0,sticky=W, padx=10, pady=10)

# Search Customers
create_user_button = Button(tab1, text="Create user", command=create_user)
create_user_button.grid(row=19, column=0, sticky=W, padx=10, pady=10)




root.mainloop()

