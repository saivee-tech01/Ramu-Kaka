from guizero import App,PushButton,Text
import csv

# Container
app = App("CSV-File-Viewer")
app.geometry=200*400
app.bg="#A3D4E9 "

# Function for viewing .csv file called when button is clicked.
def get_file():
    x = app.select_file(filetypes=[["All files", "*.*"], ["CSV documents", "*.csv"]])
    with open(x,'r') as csv_file:
        csvr=csv.reader(csv_file)
        line_count=0
        for row in csvr:
            file_name=Text(app)
            if line_count==0:
                file_name.value=f'{" ".join(row)}'
                line_count+=1
            else:
                file_name.value=f'{row[0]} {row[1]}'
                line_count+=1
                
        
# Text
csv_text= Text(app, text="Please select csv file from below:",size=28,font="Times New Roman")

# PushButton
PushButton(app,text="Select from here.",command=get_file)



app.display()
