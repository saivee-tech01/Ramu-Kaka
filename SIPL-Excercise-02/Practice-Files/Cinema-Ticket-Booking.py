from guizero import *

# Container
app = App(title="My second GUI app",height=300,width=200,layout="grid")

# Text
film_description = Text(app, text="Which film?", grid=[0,0], align="left")

# ComboBox
film_choice = Combo(app, options=["Star Wars", "Frozen", "Lion King"], grid=[1,0],align="left")

film_description = Text(app, text="Seat type?", grid=[0,1], align="left")

# CheckBox
vip_seat = CheckBox(app, text="VIP seat?", grid=[1,1], align="left")
normal_seat = CheckBox(app, text="Normal seat?", grid=[1,2], align="left")

gender_choice = Text(app, text="Seat Location", grid=[0,3], align="left")

# ButtonGroup
row_choice = ButtonGroup(app, options=[ ["Front", "F"], ["Middle", "M"],["Back", "B"] ],
selected="M", horizontal=True, grid=[1,3], align="left")



def do_booking():
    info("Booking", "Thank you for booking")
    print( film_choice.value )
    print( vip_seat.value )
    print( row_choice.value )
    
# PushButton
button=PushButton(app,command=do_booking,text="Book seat",grid=[1,4],align="left")    

app.display()
