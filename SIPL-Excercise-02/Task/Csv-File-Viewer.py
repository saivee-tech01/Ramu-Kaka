from guizero import *


app = App("CSV-File-Viewer")
app.geometry=200*400
app.bg="#A3D4E9 "

def get_file():
    file_name.value = app.select_file(filetypes=[["All files", "*.*"], ["CSV documents", "*.csv"]])

csv_text= Text(app, text="Please select csv file from below:",size=28,font="Times New Roman")
PushButton(app,text="Select from here.",command=get_file)
file_name=Text(app)


app.display()
