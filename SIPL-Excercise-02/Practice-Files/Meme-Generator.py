from guizero import *

# Function for creating meme
def draw_meme():
    meme.clear()
    meme.image(0,0,"cat.png")
    meme.text(20,20,top_text_box.value,color=color.value,size=size.value,font=font.value)
    meme.text(20,320,bottom_text_box.value,color=color.value,size=size.value,font=font.value)

# Container
app=App("Meme-Generator")

# TextBox
top_text_box=TextBox(app,text="top text",command=draw_meme)
bottom_text_box=TextBox(app,text="bottom text",command=draw_meme)

# ComboBox
color=Combo(app,options=["blue","black","green","yellow","red"],selected="black")
font=Combo(app,options=["times new roman", "verdana", "courier", "impact"],selected="verdana")

# Slider
size=Slider(app,start=20,end=60,command=draw_meme)

# Drawing
meme=Drawing(app,width="fill",height="fill")


draw_meme()
app.display()