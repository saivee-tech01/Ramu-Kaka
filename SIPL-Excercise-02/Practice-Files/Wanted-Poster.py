from guizero import *

app=App("Wanted!",bg="#228185")

wanted_text = Text(app, text="WANTED!!!",size=50)
wanted_pic=Picture(app,image="cat.png")

app.display()