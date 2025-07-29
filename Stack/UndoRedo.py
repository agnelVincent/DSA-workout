class UndoRedo:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def perform_action(self, action):
        self.undo_stack.append(action)
        self.redo_stack.clear()
        print(f"Performed: {action}")

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo")
            return
        action = self.undo_stack.pop()
        self.redo_stack.append(action)
        print(f"Undo: {action}")

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo")
            return
        action = self.redo_stack.pop()
        self.undo_stack.append(action)
        print(f"Redo: {action}")

    def show_stacks(self):
        print("Undo Stack:", self.undo_stack)
        print("Redo Stack:", self.redo_stack)


stack = UndoRedo()

for i in ['His', 'name', 'is', 'Tony', 'Montana']:
    stack.perform_action(i)

stack.show_stacks()

stack.undo()
stack.undo()

stack.show_stacks()

stack.redo()
stack.show_stacks()
