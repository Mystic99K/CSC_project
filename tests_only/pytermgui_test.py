import py_cui

class SimpleTodoList:

    def __init__(self, master):

        self.master = master

        # The scrolled list cells that will contain our tasks in each of the three categories
        self.todo_scroll_cell =         self.master.add_scroll_menu('TODO',         0, 0, row_span=6, column_span=2)
        self.in_progress_scroll_cell =  self.master.add_scroll_menu('In Progress',  0, 2, row_span=7, column_span=2)
        self.done_scroll_cell =         self.master.add_scroll_menu('Done',         0, 4, row_span=7, column_span=2)

        # Textbox for entering new items
        self.new_todo_textbox = self.master.add_text_box('TODO Item', 6, 0, column_span=2)

        # Keybindings for controlling our CUI.
        # We bind the enter key for each of the widgets
        self.new_todo_textbox.add_key_command(          py_cui.keys.KEY_ENTER, self.add_item)
        self.todo_scroll_cell.add_key_command(          py_cui.keys.KEY_ENTER, self.mark_as_in_progress)
        self.in_progress_scroll_cell.add_key_command(   py_cui.keys.KEY_ENTER, self.mark_as_done)
        self.done_scroll_cell.add_key_command(          py_cui.keys.KEY_ENTER, self.remove_item)

    def add_item(self):
        """ Add a todo item """

        self.todo_scroll_cell.add_item(f'{self.new_todo_textbox.get()}')
        self.new_todo_textbox.clear()

    def mark_as_in_progress(self):
        """ Mark a todo item as inprogress. Remove it from todo scroll list, add it to in progress list, or show error popup if no tasks """

        in_prog = self.todo_scroll_cell.get()
        if in_prog is None:
            self.master.show_error_popup('No Item', 'There is no item in the list to mark as in progress')
            return
        self.todo_scroll_cell.remove_selected_item()
        self.in_progress_scroll_cell.add_item(in_prog)

    def mark_as_done(self):
        """ Mark a inprogress item as done. Remove it from inprogress scroll list, add it to done list, or show error popup if no tasks """

        done = self.in_progress_scroll_cell.get()
        if done is None:
            self.master.show_error_popup('No Item', 'There is no item in the list to mark as done')
            return
        self.in_progress_scroll_cell.remove_selected_item()
        self.done_scroll_cell.add_item(done)

    def remove_item(self):
        """ Remove a todo item """

        self.done_scroll_cell.remove_selected_item()

# Create the CUI with 7 rows 6 columns, pass it to the wrapper object, and start it
root = py_cui.PyCUI(7, 6)
root.set_title('CUI TODO List')
s = SimpleTodoList(root)
root.start()