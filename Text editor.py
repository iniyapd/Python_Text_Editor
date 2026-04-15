class HistoryItem:
    def __init__(self,operation,previous_text,affected_text):
        self.operation=operation
        self.previous_text=previous_text
        self.affected_text=affected_text
class Editor:
    def __init__(self):
        self.text=" "
        self.history=[]
editor=Editor()
while True:
    print("1.Insert\n 2.Delete\n 3.Undo\n 4.Display\n 5.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1: #insert
        inserted_text=input("Enter text to be inserted")
        previous_text=editor.text
        editor.text= editor.text+inserted_text
        item=HistoryItem("insert",previous_text,inserted_text)
        editor.history.append(item)
    elif ch==2: #delete
        num_chars=int(input("Enter number of characters to delete:"))
        if num_chars<=0 and num_chars>len(editor.text):
            print("Invalid input")
        else:
            affected_text=editor.text[-num_chars:]
            previous_text=editor.text
            editor.text=editor.text[:-num_chars]
            item=HistoryItem("delete",previous_text,affected_text)
            editor.history.append(item)
    elif ch==3: #undo
        if not editor.history:
            print("Nothing to undo")
        else:
            last_operation=editor.history.pop()
            if last_operation.operation=="insert":
                editor.text=last_operation.previous_text
            elif last_operation.operation=="delete":
                editor.text=last_operation.previous_text
    elif ch==4: #display
        print("Current text:", editor.text)
    elif ch==5:
        break
