from guizero import *
def draw_meme():
    meme.clear()
    meme.image(0,0,"cat.png")
    meme.text(20,20,top_text_box.value,color=color.value,size=size.value,font=font.value)
    meme.text(20,320,bottom_text_box.value,color=color.value,size=size.value,font=font.value)

app=App("Meme-Generator")

top_text_box=TextBox(app,text="top text",command=draw_meme)
bottom_text_box=TextBox(app,text="bottom text",command=draw_meme)
color=Combo(app,options=["blue","black","green","yellow","red"],selected="black")
font=Combo(app,options=["times new roman", "verdana", "courier", "impact"],selected="verdana")
size=Slider(app,start=20,end=60,command=draw_meme)
meme=Drawing(app,width="fill",height="fill")


draw_meme()
app.display()