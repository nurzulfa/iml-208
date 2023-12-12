import tkinter
from tkinter import ttk
from tkinter import messagebox

#initialize an empty list for pet owner data
pet_owner_data = []

global selected_index
selected_index = None  

#registration
def register():
    accepted = accept_var.get()

    if accepted == "Accepted":  
        # Pet owner
        name = name_textbox.get() 
        gender = gender_combobox.get() 
        age = age_spinbox.get() 
        email = email_textbox.get() 
        phone_number = phone_number_textbox.get() 
        address = address_textbox.get()

        if name and email and phone_number and address:
            # Pet info
            petname = pet_name_textbox.get() 
            pettype = pet_type_combobox.get() 
            petbreed = pet_breed_textbox.get() 

            print("Name:", name, "Gender:", gender, "Age:", age,)
            print("Email:", email, "Phone Number:", phone_number, "Address:", address)
            print("------------------------------------------")
            print("Pet Name:", petname, "Pet Type:", pettype, "Pet breeds:", petbreed)

            pet_owner_data.append({
                "Name": name,
                "Gender": gender,
                "Age": age,
                "Email Address": email,
                "Phone_Number": phone_number,
                "Address": address,
                "Pet Name": petname,
                "Pet Type": pettype,
                "Pet Breeds": petbreed
            })

            update_listbox_entry()  
            messagebox.showinfo(title="Success", message="You are successfully registered!")
        else:
            messagebox.showwarning(title="Warning", message="Please fill in the required fields")
    else:
        messagebox.showwarning(title="Warning", message="You should accept the terms") 

#delete registration operation        
def delete_registration(): 
    global selected_index
    if selected_index is not None and 0 <= selected_index < len(pet_owner_data): 
        del pet_owner_data[selected_index] 
        update_listbox_entry()  
        print("Record deleted successfully")
        selected_index = None  
    else:
        messagebox.showwarning(title="Warning", message="Please select a record for deletion")

#update registration in listbox
def update_listbox_entry():
    pet_owner_listbox.delete(0, tkinter.END)
    for i, owner in enumerate(pet_owner_data):
        info = (      
            f"Registration {i + 1}: "
            f"Name: {owner['Name']} | Gender: {owner ['Gender']} | Age: {owner['Age']} | "
            f"Email Address: {owner['Email Address']} | Phone Number: {owner['Phone_Number']} | Address: {owner['Address']} "
            f"Pet Name: {owner['Pet Name']} | Pet Type: {owner['Pet Type']}  | Pet Breeds: {owner['Pet Breeds']}" 
        )   
        pet_owner_listbox.insert(tkinter.END, info)

#edit registration operation
def edit_registration(): 
    global selected_index
    if selected_index is not None and 0 <= selected_index < len(pet_owner_data): 
        selected_data = pet_owner_data[selected_index]

        selected_data["Name"] = name_textbox.get()
        selected_data["Gender"] = gender_combobox.get()
        selected_data["Age"] = age_spinbox.get()
        selected_data["Email Address"] = email_textbox.get()
        selected_data["Phone Number"] = phone_number_textbox.get() 
        selected_data["Address"] = address_textbox.get()
        selected_data["Pet Name"] = pet_name_textbox.get()
        selected_data["Pet Type"] = pet_type_combobox.get()
        selected_data["Pet Breeds"] = pet_breed_textbox.get()

        update_listbox_entry()   
    else: 
        messagebox.showwarning(title="Warning", message="Please select a valid record for editing")

#select registration operation
def on_select(event):
    global selected_index
    widget = event.widget
    selected_indices = widget.curselection()

    if selected_indices:
        selected_index = selected_indices[0]
        display_selected_record(selected_index) 
    else: 
        selected_index = None

#display record
def display_selected_record(index): 
    if 0<= index < len(pet_owner_data):
        selected_data = pet_owner_data[index]

        name_textbox.delete(0, tkinter.END)
        name_textbox.insert(0, selected_data["Name"])

        gender_combobox.set(selected_data["Gender"])

        age_spinbox.delete(0, tkinter.END) 
        age_spinbox.insert(0, selected_data["Age"])
        email_textbox.delete(0, tkinter.END)
        email_textbox.insert(0, selected_data["Email Address"])

        phone_number_textbox.delete(0,tkinter.END) 
        phone_number_textbox.insert(0, selected_data["Phone_Number"])
        address_textbox.delete(0, tkinter.END)
        address_textbox.insert(0, selected_data["Address"])

        pet_name_textbox.delete(0, tkinter.END) 
        pet_name_textbox.insert(0, selected_data["Pet Name"])

        pet_type_combobox.set(selected_data["Pet Type"])

        pet_breed_textbox.delete(0, tkinter.END) 
        pet_breed_textbox.insert(0, selected_data["Pet Breeds"])

# create window application
root = tkinter.Tk()
root.title("Registration form")

frame = tkinter.Frame(root)
frame.pack()

#saving pet owner info
pet_owner_frame = tkinter.LabelFrame(frame, text="Pet Owner Registration", font="Cooper 10 bold")
pet_owner_frame.grid(row=0, column=0, padx=20, pady=20)

#widget for pet owner
name_label = tkinter.Label(pet_owner_frame, text="Name")
name_label.grid(row=0, column=0) 
name_textbox = tkinter.Entry(pet_owner_frame) 
name_textbox.grid(row=1, column=0) 

gender_label = tkinter.Label(pet_owner_frame, text="Gender")
gender_combobox = ttk.Combobox(pet_owner_frame, values=["Male", "Female"])
gender_label.grid(row=0, column=1)
gender_combobox.grid(row=1, column=1)

age_label = tkinter.Label(pet_owner_frame, text="Age") 
age_spinbox = tkinter.Spinbox(pet_owner_frame, from_=18, to=70)
age_label.grid(row=0, column=2)
age_spinbox.grid(row=1, column=2) 

email_label = tkinter.Label(pet_owner_frame, text="Email Address")
email_textbox = tkinter.Entry(pet_owner_frame)
email_label.grid(row=2, column=0)
email_textbox.grid(row=3, column=0)

phone_number_label = tkinter.Label(pet_owner_frame, text="Phone Number") 
phone_number_textbox = tkinter.Entry(pet_owner_frame) 
phone_number_label.grid(row=2, column=1)
phone_number_textbox.grid(row=3, column=1) 

address_label = tkinter.Label(pet_owner_frame, text="Address")
address_textbox = tkinter.Entry(pet_owner_frame)
address_label.grid(row=2, column=2)
address_textbox.grid(row=3, column=2) 

for widget in pet_owner_frame.winfo_children(): 
    widget.grid_configure(padx=10, pady=5)

#saving pet info 
pet_frame = tkinter.LabelFrame(frame, text="Pet Information", font="Cooper 10 bold") 
pet_frame.grid(row=1, column=0, sticky="news" , padx=20, pady=20)

#widget for pet info
pet_name_label = tkinter.Label(pet_frame, text="Pet Name") 
pet_name_textbox = tkinter.Entry(pet_frame) 
pet_name_label.grid(row=0, column=0)
pet_name_textbox.grid(row=1, column=0) 

pet_type_label = tkinter.Label(pet_frame, text="Pet Type") 
pet_type_combobox = ttk.Combobox(pet_frame, values=["Cat", "Dog"])
pet_type_label.grid(row=0, column=1) 
pet_type_combobox.grid(row=1, column=1) 

pet_breed_label = tkinter.Label(pet_frame, text="Pet Breeds")
pet_breed_textbox = tkinter.Entry(pet_frame)
pet_breed_label.grid(row=0, column=2)
pet_breed_textbox.grid(row=1, column=2) 

for widget in pet_frame.winfo_children(): 
    widget.grid_configure(padx=10, pady=5) 

#accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Condition", font="Cooper 10 bold")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=20) 

accept_var = tkinter.StringVar(value="Not Accepted") 
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not accepted") 
terms_check.grid(row=0, column=0) 

#buttons 
register_button = tkinter.Button(frame, text="Register", command=register) 
register_button.grid(row=3, column=0, sticky="news", padx=20, pady=20) 

edit_button = tkinter.Button(frame, text="Edit", command=edit_registration) 
edit_button.grid(row=3, column=3, sticky="N", padx=20, pady=20) 

delete_button = tkinter.Button(frame, text="Delete", command=delete_registration)  
delete_button.grid(row=3, column=1, sticky="N", padx=20, pady=20) 

#create listbox 
pet_owner_listbox = tkinter.Listbox(frame, selectmode=tkinter.SINGLE)
pet_owner_listbox.grid(row=0, column=1, padx=20, pady=20)
pet_owner_listbox.bind("<<ListboxSelect>>", on_select) 

update_listbox_entry() 

root.mainloop()