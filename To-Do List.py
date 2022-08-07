#import libraries
import tkinter
import tkinter.messagebox
import pickle

#create root window 
root = tkinter.Tk()
#give title 
root.title("TO-DO List ")
#give background color
root.config(bg="black")

#Create functions 
def add_task():
    task= entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message=" You must enter a task.")
    
def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
        tkinter.messagebox.showwarning(title="Delete", message=" Your selected task is DELETED.")
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")
    
def clear_all():
    listbox_tasks.delete(0, tkinter.END)
    tkinter.messagebox.showwarning(title="Clear all", message="All tasks are cleared.")

def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")

def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))
    
def clear_entry(event,entry_task):
    entry_task.delete(0,tkinter.END)
      
#Creation of GUI
#Create Frame
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

#Create a Listbox for displaying our tasks
listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50, fg="black", bg="grey", bd=4)
listbox_tasks.pack(side=tkinter.LEFT)

#Create scroll bar 
scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

#Create Entry field to enter our tasks
entry_task = tkinter.Entry(root, width=50)
entry_task.insert(0,"Enter Task Here...")
entry_task.bind("<Button-1>", lambda event: clear_entry(event, entry_task) )
entry_task.pack()


#Create Buttons and give commands
button_add_task = tkinter.Button(root, text="Add task", width=48, bg="grey",fg="black",bd=4, command=add_task)
button_add_task.pack()

button_save_tasks = tkinter.Button(root, text="Save tasks", width=48, bg="grey",fg="black",bd=4, command=save_tasks)
button_save_tasks.pack()

button_load_tasks = tkinter.Button(root, text="Load tasks", width=48, bg="grey",fg="black", bd=4, command=load_tasks)
button_load_tasks.pack()

button_delete_task = tkinter.Button(root, text="Delete task", width=48, bg="grey",fg="black",bd=4, command=delete_task)
button_delete_task.pack()

button_Clear_all_tasks = tkinter.Button(root, text="Clear all tasks", width=48, bg="grey",fg="black",bd=4, command=clear_all)
button_Clear_all_tasks.pack()

button_Exit = tkinter.Button(root, text="Exit", width=48, bg="grey",fg="red",bd=4, command=root.destroy)
button_Exit.pack()

root.mainloop()
