from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sql
import data_analytics as da

root = Tk()
root.title('Adult Income Dataset')
root.geometry('1040x500')
root['background'] = '#404258'
# connect to database
db = sql.Database("adult_income.db")

# Treeview
style = ttk.Style()
style.theme_use('default')
style.configure("Treeview", background="#262729", foreground="black", rowheight=25, fieldbackground="#262729")
style.map('Treeview', background=[('selected', "#252626")])

tree_frame = Frame(root)
tree_frame.pack(pady=10)

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

tree_scroll1 = Scrollbar(tree_frame, orient='horizontal')
tree_scroll1.pack(side=BOTTOM, fill=X)

my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree = ttk.Treeview(tree_frame, xscrollcommand=tree_scroll1.set, selectmode="extended")
my_tree.pack()

tree_scroll.config(command=my_tree.yview)
tree_scroll1.config(command=my_tree.xview)


my_tree['columns'] = ("age", "workclass", "education", "occupation", "race", "gender", "hours-per-week", "native-country", "income")


my_tree.column("#0", width=0, stretch=NO)
my_tree.column("age", anchor=CENTER, width=140)
my_tree.column("workclass", anchor=CENTER, width=140)
my_tree.column("education", anchor=CENTER, width=100)
my_tree.column("occupation", anchor=CENTER, width=140)
my_tree.column("race", anchor=CENTER, width=140)
my_tree.column("gender", anchor=CENTER, width=140)
my_tree.column("hours-per-week", anchor=CENTER, width=140)
my_tree.column("native-country", anchor=CENTER, width=140)
my_tree.column("income", anchor=CENTER, width=140)


my_tree.heading("#0", text="", anchor=W)
my_tree.heading("age", text="Age", anchor=CENTER)
my_tree.heading("workclass", text="Workclass", anchor=CENTER)
my_tree.heading("education", text="Education", anchor=CENTER)
my_tree.heading("occupation", text="Occupation", anchor=CENTER)
my_tree.heading("race", text="Race", anchor=CENTER)
my_tree.heading("gender", text="Gender", anchor=CENTER)
my_tree.heading("hours-per-week", text="Hours per Week", anchor=CENTER)
my_tree.heading("native-country", text="Native Country", anchor=CENTER)
my_tree.heading("income", text="Income", anchor=CENTER)

# rows
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="#95969c")



# entry boxes
data_frame = LabelFrame(root, text="", background="#474E68")
data_frame.pack(fill="x", expand="yes", padx=20)

age_label = Label(data_frame, text="Age", bd=1, justify="left", bg='#474E68', fg='white', font='Helvetica 10 bold')
age_label.grid(row=0, column=0, padx=10, pady=10)
age_entry = Spinbox(data_frame, from_=1, to=120, width=18)
age_entry.delete(0, "end")
age_entry.grid(row=0, column=1, padx=10, pady=10)

work_label = Label(data_frame, text="Workclass", justify="left", bg='#474E68', fg='white', font='Helvetica 10 bold')
work_label.grid(row=0, column=2, padx=10, pady=10)
work_entry = ttk.Combobox(data_frame, values=["Private", "Public", "Local-gov", "Federal-gov", "State-gov", "Self-emp-inc", "Self-emp-not-inc", "Without Pay", "Never Worked"],width=18)
work_entry.grid(row=0, column=3, padx=10, pady=10)

educ_label = Label(data_frame, text="Education", justify="left", bg='#474E68', fg='white', font='Helvetica 10 bold')
educ_label.grid(row=0, column=4, padx=10, pady=10)
educ_entry = Entry(data_frame)
educ_entry.grid(row=0, column=5, padx=10, pady=10)

occu_label = Label(data_frame, text="Occupation", justify="left", bg='#474E68', fg='white', font='Helvetica 10 bold')
occu_label.grid(row=1, column=0, padx=20, pady=10)
occu_entry = Entry(data_frame)
occu_entry.grid(row=1, column=1, padx=20, pady=10)

race_label = Label(data_frame, text="Race", justify="left", bg='#474E68', fg='white', font='Helvetica 10 bold')
race_label.grid(row=1, column=2, padx=20, pady=10)
race_entry = Entry(data_frame)
race_entry.grid(row=1, column=3, padx=20, pady=10)

gender_label = Label(data_frame, text="Gender", justify="left", bg='#474E68', fg='white', font='Helvetica 10 bold')
gender_label.grid(row=1, column=4, padx=20, pady=10)
gender_entry = ttk.Combobox(data_frame, values=["Female", "Male"],width=18)
gender_entry.grid(row=1, column=5, padx=20, pady=10)

hpr_label = Label(data_frame, text="Hours per Week", justify="left", bg='#474E68', fg='white', font='Helvetica 10 bold')
hpr_label.grid(row=2, column=0, padx=30, pady=10)
hpr_entry = Entry(data_frame)
hpr_entry.grid(row=2, column=1, padx=30, pady=10)

nc_label = Label(data_frame, text="Native Country", justify="left", bg='#474E68', fg='white', font='Helvetica 10 bold')
nc_label.grid(row=2, column=2, padx=30, pady=10)
nc_entry = Entry(data_frame)
nc_entry.grid(row=2, column=3, padx=30, pady=10)

income_label = Label(data_frame, text="Income", justify="left", bg='#474E68', fg='white', font='Helvetica 10 bold')
income_label.grid(row=2, column=4, padx=30, pady=10)
income_entry = ttk.Combobox(data_frame, values=[">50K", "<=50K"],width=18)
income_entry.grid(row=2, column=5, padx=30, pady=10)


# database
def query_database():
    records = db.fetch()

    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[1:]), tags=('evenrow', record[0]))

        else:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[1:]), tags=('oddrow', record[0]))
        count += 1

# clear boxes
def clear_entries():
    age_entry.delete(0, END)
    work_entry.delete(0, END)
    educ_entry.delete(0, END)
    occu_entry.delete(0, END)
    race_entry.delete(0, END)
    gender_entry.delete(0, END)
    hpr_entry.delete(0, END)
    nc_entry.delete(0, END)
    income_entry.delete(0, END)

# select Record
def select_record(e):
    # Clear
    age_entry.delete(0, END)
    work_entry.delete(0, END)
    educ_entry.delete(0, END)
    occu_entry.delete(0, END)
    race_entry.delete(0, END)
    gender_entry.delete(0, END)
    hpr_entry.delete(0, END)
    nc_entry.delete(0, END)
    income_entry.delete(0, END)

    # grab record number
    selected = my_tree.focus()
    # grab values
    values = my_tree.item(selected, 'values')
    primary_key = my_tree.item(selected, 'tags')[1]

    # output
    age_entry.insert(0, values[0])
    work_entry.insert(0, values[1])
    educ_entry.insert(0, values[2])
    occu_entry.insert(0, values[3])
    race_entry.insert(0, values[4])
    gender_entry.insert(0, values[5])
    hpr_entry.insert(0, values[6])
    nc_entry.insert(0, values[7])
    income_entry.insert(0, values[8])

# delete record
def delete_record():
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="#95969c")

    ans = messagebox.askyesno("", "Are you sure you want to delete this record?")
    if ans:
        selected = my_tree.focus()
        primary_key = int(my_tree.item(selected, 'tags')[1])
        db.remove(primary_key)
        my_tree.delete(*my_tree.get_children())
        query_database()
        messagebox.showinfo("", "Record Deleted")
        
            


# update record
def update_record():
    # grab record number
    selected = my_tree.focus()
    primary_key = int(my_tree.item(selected, 'tags')[1])
    # update record
    db.update(primary_key, age_entry.get(), work_entry.get(), educ_entry.get(), occu_entry.get(), race_entry.get(), gender_entry.get(), hpr_entry.get(),nc_entry.get(), income_entry.get())
    my_tree.item(selected, text="", values=(age_entry.get(), work_entry.get(), educ_entry.get(), occu_entry.get(), race_entry.get(), gender_entry.get(), hpr_entry.get(),nc_entry.get(), income_entry.get(),))
    messagebox.showinfo("", "Record Updated")
    # Clear
    age_entry.delete(0, END)
    work_entry.delete(0, END)
    educ_entry.delete(0, END)
    occu_entry.delete(0, END)
    race_entry.delete(0, END)
    gender_entry.delete(0, END)
    hpr_entry.delete(0, END)
    nc_entry.delete(0, END)
    income_entry.delete(0, END)

# insert record
def insert_record():
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="#95969c")

    db.insert(age_entry.get(), work_entry.get(), educ_entry.get(), occu_entry.get(), race_entry.get(), gender_entry.get(), hpr_entry.get(),nc_entry.get(), income_entry.get())

    messagebox.showinfo("", "Record Added")
    my_tree.delete(*my_tree.get_children())
    query_database()

# view data
def view_data():
    df = da.pd.DataFrame(db.fetch(), columns=["primary_key", "age", "workclass", "education", "occupation", "race", "gender", "hours_per_week", "native_country", "income"])
    da.plot_agerace(df)

#buttons

button_frame = LabelFrame(root, text="", background="#474E68")
button_frame.pack(fill="x", expand="yes", padx=20)

add_button = Button(button_frame, text="Add", command=insert_record, width=15, background='#F0EEED')
add_button.grid(row=0, column=0, padx=30, pady=10)

update_button = Button(button_frame, text="Update", command=update_record, width=15, background='#F0EEED')
update_button.grid(row=0, column=1, padx=45, pady=10)

delete_button = Button(button_frame, text="Delete", command=delete_record, width=15, background='#F0EEED')
delete_button.grid(row=0, column=2, padx=45, pady=10)

clear_button = Button(button_frame, text="Clear", command=clear_entries, width=15, background='#F0EEED')
clear_button.grid(row=0, column=4, padx=45, pady=10)

view_button = Button(button_frame, text="View", command=view_data, width=15, background='#F0EEED')
view_button.grid(row=0, column=5, padx=20, pady=10)

# bind treeview
my_tree.bind("<ButtonRelease-1>", select_record)

if __name__ == "__main__":
    query_database()
    root.mainloop()
