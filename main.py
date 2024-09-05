import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

window = tk.Tk()
window.title('GUI for Photo Watermarker')
window.config(padx=32, pady=32)

img_path = ''


def browsefunc():
    filename = filedialog.askopenfilename(filetypes=(("TIFF files", "*.tiff;*.tif"), ("All files", "*.*")))
    img_entry.insert(tk.END, filename)

    global img_path
    img_path = img_entry.get()


def apply_watermark():
    watermark_text = watermark_entry.get()
    font = ImageFont.truetype('arial.ttf', 24)
    with Image.open(img_path) as img:
        w, h = img.size
        x, y = int(w / 2), int(h / 2)
        draw = ImageDraw.Draw(img)
        draw.text((x, y), watermark_text, fill=(0, 0, 0), font=font, align='left')
        img.save(img_path)


canvas = tk.Canvas(width=300, height=220, highlightthickness=0)
mark_logo = tk.PhotoImage(file='watermark.png')
canvas.create_image(150, 110, image=mark_logo)
canvas.grid(column=0, row=0, columnspan=3)

img_label = tk.Label(text="Image file: ")
img_label.grid(column=0, row=1)

img_entry = tk.Entry(width=35)
img_entry.grid(column=1, row=1)

selectBtn = tk.Button(text='Select Image', padx=6, pady=3, command=browsefunc)
selectBtn.grid(column=2, row=1)

img_label = tk.Label(text="Watermark Text: ")
img_label.grid(column=0, row=2)

watermark_entry = tk.Entry(width=35)
watermark_entry.grid(column=1, row=2)

applyBtn = tk.Button(text='Apply Watermark', padx=6, pady=3, command=apply_watermark)
applyBtn.grid(column=2, row=2)


window.mainloop()
