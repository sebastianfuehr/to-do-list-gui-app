import customtkinter as ctk


class TaskList(ctk.CTk):
    def __init__(self, tasks=None):
        super().__init__()
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        self.geometry('500x350')

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        self.title("Task List")

        instructions = ctk.CTkLabel(self, text='Add a new task:', anchor='w')
        self.tasks.append(instructions)

        for task in self.tasks:
            task.pack(fill='x', padx=10, pady=10)

        self.new_task = ctk.CTkEntry(self)
        self.new_task.pack(fill="x", padx=10)
        self.new_task.focus_set()

        self.bind('<Return>', self.add_task)

    def add_task(self, event=None):
        task_text = self.new_task.get()

        task_label = ctk.CTkLabel(self, text=task_text, anchor='w')
        task_label.pack(fill='x', padx=10, pady=10)
        self.tasks.append(task_label)

        self.new_task.delete(0, ctk.END)


if __name__ == "__main__":
    task_list = TaskList()
    task_list.mainloop()
