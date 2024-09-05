import os.path
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
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
    print(img_path)


def apply_watermark():
    watermark_text = watermark_entry.get()
    font = ImageFont.truetype('comic.ttf', 26)
    filename = os.path.basename(img_path)
    dir_path = os.path.dirname(img_path)
    sub_dir = 'watermarked'

    with Image.open(img_path) as img:
        w, h = img.size
        x, y = int(w / 2) + int(w / 8), int(h / 2) + int(h / 3)
        draw = ImageDraw.Draw(img)
        draw.text((x, y), watermark_text, fill=(0, 0, 0), font=font, align='left')
        new_dir = os.path.join(dir_path, sub_dir)
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)

        new_img_path = os.path.join(new_dir, filename)
        img.save(new_img_path)

        messagebox.showinfo(title="Watermark", message=f"Watermark has been successfully applied!")

        img_entry.delete(0, tk.END)
        watermark_entry.delete(0, tk.END)


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
