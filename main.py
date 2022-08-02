from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image, ImageDraw, ImageFont
from image import ImageNeo


data_img = []


def load_img():
    ask = askopenfilename()
    return ask


def open_img():

    x = load_img()
    data = Image.open(x)
    size_label.config(text=f"x: {data.size[0]} y: {data.size[1]}")
    neo = ImageNeo(data)
    data_img.append(neo)
    data = data.resize((250, 250), Image.ANTIALIAS)
    data = ImageTk.PhotoImage(data)
    img_label.config(image=data)
    img_label.image = data


def watermark_text():
    data = data_img[0].image_data()
    draw_image = ImageDraw.Draw(data)
    text = text_entry.get()
    size = (int(entry_x.get()), int(entry_y.get()))
    font_size = int(font_entry.get())
    font = ImageFont.truetype("arial.ttf", size=font_size)
    draw_image.text(size, text, font=font)
    data.save('text_watermark.jpg')

    data = data.resize((250, 250), Image.ANTIALIAS)
    data = ImageTk.PhotoImage(data)
    img_label.config(image=data)
    img_label.image = data


def watermark_logo():
    data_logo = data_img[0].image_data()
    width, height = data_logo.size

    wmk_open = load_img()
    wmk_logo = Image.open(wmk_open)
    wmk_logo = wmk_logo.resize((125, 125), Image.ANTIALIAS)

    x = width - 125 - int(logo_entry_x.get())
    y = height - 125 - int(logo_entry_y.get())

    transparent = Image.new('RGB', (width, height), (0, 0, 0, 0))
    transparent.paste(data_logo, (0, 0))
    transparent.paste(wmk_logo, (x, y), mask=wmk_logo)
    transparent.save("watermark_logo_image.jpg")

    transparent = transparent.resize((250, 250), Image.ANTIALIAS)
    transparent = ImageTk.PhotoImage(image=transparent)
    img_label.config(image=transparent)
    img_label.image = transparent




window = Tk()
window.title("Image Watermaking TEXT/LOGO")
window.config(padx=50, pady=50)

img_label = Label()
img_label.grid(column=0, row=0, columnspan=3)

text_label = Label(text="Add Text:")
text_label.grid(column=0, row=3)

text_entry = Entry(width=28)
text_entry.grid(column=1, row=3, columnspan=2)

text_x = Label(text="Text x cor:")
text_x.grid(column=0, row=4)

entry_x = Entry(width=14)
entry_x.grid(column=1, row=4)

text_y = Label(text="Text y cor:")
text_y.grid(column=2, row=4)

entry_y = Entry(width=14)
entry_y.grid(column=3, row=4)

font_label = Label(text="Font Size:")
font_label.grid(column=0, row=5)

font_entry = Entry(width=14)
font_entry.grid(column=1, row=5)

label_x = Label(text="Logo xcor:")
label_x.grid(column=0, row=7)

logo_entry_x = Entry(width=14)
logo_entry_x.grid(column=1, row=7)

label_y = Label(text="Logo ycor:")
label_y.grid(column=2, row=7)

logo_entry_y = Entry(width=14)
logo_entry_y.grid(column=3, row=7)

size_label = Label(text="")
size_label.grid(column=1, row=1)

add_button = Button(text="Add", command=open_img)
add_button.grid(column=0, row=1)

logo_button = Button(text="Add Logo", command=watermark_logo)
logo_button.grid(column=0, row=8)

text_button = Button(text="Add Text", command=watermark_text)
text_button.grid(column=0, row=6)


window.mainloop()