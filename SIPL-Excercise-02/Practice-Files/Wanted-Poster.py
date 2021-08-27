from guizero import *

# Container
app=App("Wanted!",bg="#228185")

# Text
wanted_text = Text(app, text="WANTED!!!",size=50)

# Picture
wanted_pic=Picture(app,image="cat.png")

app.display()