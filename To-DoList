import tkinter as tk
from tkinter import messagebox

class ToDolist:
    def __init__(self, window):
        self.window = window
        self.window.title("To-Do List Application")
        self.window.geometry("400x500")
        self.tasks = []
        self.setup_ui()
        self.update_task_list()

    def setup_ui(self):
        self.task_input = tk.Entry(self.window)
        self.task_input.pack(pady=10, padx=10, fill=tk.X)

        add_button = tk.Button(self.window, text="➕ Add Task", command=self.add_task,
                               bg="#E26299", fg="white")
        add_button.pack(pady=5, padx=10, fill=tk.X)

        self.filter_var = tk.StringVar(value="All")
        filter_menu = tk.OptionMenu(self.window, self.filter_var, "All", "Completed", "Incomplete")
        
        self.task_box = tk.Listbox(self.window)
        self.task_box.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=5, padx=10, fill=tk.X)

        mark_button = tk.Button(button_frame, text="✅ Mark Complete", command=self.toggle_task_status,
                                bg="#0B14B3", fg="white", font=("Segoe UI", 10, "bold"))
        mark_button.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)

        delete_button = tk.Button(button_frame, text="🗑️ Delete Task", command=self.delete_task)
        delete_button.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)

    def add_task(self):
        new_task_text = self.task_input.get().strip()
        if not new_task_text:
            messagebox.showwarning("Wait a sec!", "You forgot to type something.")
            return
        self.tasks.append({"text": new_task_text, "completed": False})
        self.task_input.delete(0, tk.END)
        self.update_task_list()

    def toggle_task_status(self, event=None):
        selection = self.task_box.curselection()
        if not selection:
            messagebox.showinfo("Hey!", "Select a task to mark as done or not.")
            return
        index = selection[0]
        self.tasks[index]["completed"] = not self.tasks[index]["completed"]
        self.update_task_list()

    def delete_task(self):
        selection = self.task_box.curselection()
        if not selection:
            messagebox.showwarning("Oops!", "You need to select something first!")
            return
        confirm = messagebox.askyesno("Are you sure?", "Do you really want to delete this task?")
        if confirm:
            index = selection[0]
            del self.tasks[index]
            self.update_task_list()

    def update_task_list(self):
        self.task_box.delete(0, tk.END)
        filter_type = self.filter_var.get()
        for task in self.tasks:
            if (filter_type == "Completed" and not task["completed"]) or \
               (filter_type == "Incomplete" and task["completed"]):
                continue
            status = "✓ " if task["completed"] else "○ "
            self.task_box.insert(tk.END, f"{status}{task['text']}")
            if task["completed"]:
                self.task_box.itemconfig(tk.END, fg="gray")

def main():
    root = tk.Tk()
    app = ToDolist(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    
