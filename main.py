from tkinter import *
from tkinter import filedialog as fd, messagebox

from tkinter import simpledialog, Tk, font
from tkinter.messagebox import showinfo, askyesno
import tkinter.ttk as ttk
import tkinter as tk
from PIL import Image, ImageTk
import cv2
import numpy as np
import img_functions


class MyWindow:

    def __init__(self):
        self.win = Tk()
        self.win.title("Noa's photo editor")
        self.win.geometry('600x400')
        self.file_path = None
        self.draw_win = None
        self.img = None

        # Load and resize background image
        bg_image = Image.open("././images/bg.jpg")
        bg_image = bg_image.resize((600, 400), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        # Create a Label widget to display the background image
        self.bg_label = Label(self.win, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.label = tk.Label(self.win,
                              text="Noa's photo editor",
                              font=("Segoe Script", 35, "bold"),
                              fg="black",
                              bg='orange')
        self.label.place(x=70, y=50)

        style = ttk.Style()
        style.configure('W.TButton', font=('Segoe Script', 15, 'bold'), foreground='black', background="yellow")
        self.defaultFont = font.nametofont("TkDefaultFont")
        self.defaultFont.configure(family="Segoe Script")

        self.icon_select = self.icon_image("././images/select.png")
        self.icon_edit = self.icon_image("././images/edit.png")
        self.icon_save = self.icon_image("././images/save.png")
        self.icon_exit = self.icon_image("././images/exit.png")
        self.icon_blank = self.icon_image("././images/pencil.png")

        self.btn_add = Button(self.win, text="Selecting an image ", image=self.icon_select, compound=RIGHT, bg="orange",
                              font=('Segoe Script', 15, 'bold'), command=self.select_img)
        self.btn_edit_img = Button(self.win, text="Image editing ", image=self.icon_edit, compound=RIGHT, bg="orange",
                                   font=('Segoe Script', 15, 'bold'), command=self.open_edit_window)
        self.btn_save_changes = Button(self.win, text="Save changes ", image=self.icon_save, compound=RIGHT,
                                       bg="orange", font=('Segoe Script', 15, 'bold'), command=self.save_changes)
        self.btn_exit = Button(self.win, text="exit ", image=self.icon_exit, compound=RIGHT, bg="orange",
                               font=('Segoe Script', 15, 'bold'), command=self.exit)
        self.btn_blank = Button(self.win, text="free drawing ", image=self.icon_blank, compound=RIGHT, bg="orange",
                                font=('Segoe Script', 15, 'bold'), command=self.select_blank)

        self.positions_btn()
        self.win.mainloop()



    # חלון בחירת תמונה
    def select_img(self):
        filetypes = (('Image files', '*.png *.jpg *.jpeg *.tiff *.bmp *.gif'),)
        self.file_path = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
        if self.file_path:
            self.img = img_functions.MyImage(self.file_path, "Edit_img")
            print(self.file_path)

    def select_blank(self):
        blank_image_path = "././images/blank.png"
        self.img = img_functions.MyImage(blank_image_path, "Edit_img")
        self.img.image = cv2.resize(self.img.image, (600, 600))
        self.img.original_image = self.img.image.copy()
        self.img.show()


    def open_edit_window(self):
        if self.img is None:
            #  הקפצת חלון לא נבחרה תמונה
            messagebox.showerror("Error! No image selected", "Oh! You haven't chosen a picture yet🙄")
        else:
            self.draw_win = Toplevel(self.win)
            self.draw_win.title("Image editing")
            self.draw_win.geometry("700x500")

            # Load and resize the background image
            bg_image2 = Image.open("././images/bg.jpg")
            bg_image2 = bg_image2.resize((700, 500), Image.LANCZOS)
            bg_photo2 = ImageTk.PhotoImage(bg_image2)

            # Create a Label widget to display the background image
            bg_label = tk.Label(self.draw_win, image=bg_photo2)
            bg_label.image = bg_photo2  # Keep a reference to avoid garbage collection
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)

            self.icon_shapes = self.icon_image("././images/shapes.png")
            self.icon_cut = self.icon_image("././images/cut.png")
            self.icon_text = self.icon_image("././images/add-text.png")
            self.icon_color = self.icon_image("././images/change-color.png")

            self.btn_add_shape = Button(self.draw_win, text="Adding shapes ", image=self.icon_shapes, compound=RIGHT,
                                        bg="orange", font=('Segoe Script', 15, 'bold'),
                                        command=self.selection_draw_func)

            self.btn_cut = Button(self.draw_win, text="Picture cutting ", bg="orange",
                                  font=('Segoe Script', 15, 'bold'), image=self.icon_cut, compound=RIGHT,
                                  command=self.crop_img)

            self.btn_add_text = Button(self.draw_win, text="Adding text ", bg="orange",
                                       font=('Segoe Script', 15, 'bold'), image=self.icon_text, command=self.add_text,
                                       compound=RIGHT)

            self.btn_set_color = Button(self.draw_win, text="color choice ", bg="orange",
                                        font=('Segoe Script', 15, 'bold'), image=self.icon_color,
                                        command=self.set_color, compound=RIGHT)

            self.positions_edit_btn()
            self.add_image_buttons()

    def add_image_buttons(self):
        img_path = r"././images/exm_img1.jpg"
        pil_image = Image.open(img_path)
        pil_image = pil_image.resize((100, 100), Image.ANTIALIAS)
        self.opencv_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

        # set color of images btn:
        self.photoimage1 = self.image_btn(cv2.COLORMAP_JET)
        self.photoimage2 = self.image_btn(cv2.COLORMAP_BONE)
        self.photoimage3 = self.image_btn(cv2.COLOR_RGB2BGR)
        self.photoimage4 = self.image_btn(cv2.COLORMAP_AUTUMN)
        self.photoimage5 = self.image_btn(cv2.COLORMAP_HSV)

        # 5 sort of colors from cv2:
        self.btn_apply_colormap_jet = Button(self.draw_win, image=self.photoimage1, command=self.apply_colormap_jet)
        self.btn_apply_colormap_bone = Button(self.draw_win, image=self.photoimage2, command=self.apply_colormap_bone)
        self.btn_original = Button(self.draw_win, image=self.photoimage3, command=self.set_color_original)
        self.btn_apply_colormap_autumn = Button(self.draw_win, image=self.photoimage4, command=self.apply_colormap_autumn)
        self.btn_apply_colormap_hsv = Button(self.draw_win, image=self.photoimage5, command=self.apply_colormap_hsv)

        self.position_images_btn()

    def selection_draw_func(self):
        self.shape_win = Toplevel(self.draw_win, bg="orange")
        self.shape_win.title("Draw")
        self.shape_win.geometry("250x250")

        self.icon_circle = self.icon_image("././images/circle.png")
        self.icon_triangle = self.icon_image("././images/triangle.png")
        self.icon_rectangle = self.icon_image("././images/rectangle.png")
        self.icon_line = self.icon_image("././images/line.png")

        btn_draw_circle = ttk.Button(self.shape_win, text=" circle ", style='W.TButton', image=self.icon_circle,
                                     compound=RIGHT, command=self.draw_circle)
        btn_draw_circle.grid(row=1, column=0, padx=20, pady=10)
        btn_draw_triangle = ttk.Button(self.shape_win, text=" triangle ", style='W.TButton', image=self.icon_triangle,
                                       compound=RIGHT, command=self.draw_triangle)
        btn_draw_triangle.grid(row=2, column=0, padx=20, pady=10)
        btn_draw_rectangle = ttk.Button(self.shape_win, text=" rectangle ", style='W.TButton',
                                        image=self.icon_rectangle, compound=RIGHT, command=self.draw_rectangle)
        btn_draw_rectangle.grid(row=3, column=0, padx=20, pady=10)
        btn_draw_rectangle = ttk.Button(self.shape_win, text=" Line ", style='W.TButton', image=self.icon_line,
                                        compound=RIGHT, command=self.draw_line)
        btn_draw_rectangle.grid(row=4, column=0, padx=20, pady=10)

    def icon_image(self, path):
        icon_image = Image.open(path)
        icon_image = icon_image.resize((24, 24), Image.LANCZOS)
        return ImageTk.PhotoImage(icon_image)

    def image_btn(self,name):
        jet_image = cv2.applyColorMap(self.opencv_image, name)
        pil_jet_image = Image.fromarray(jet_image)
        return ImageTk.PhotoImage(pil_jet_image)

    # הגדרת מיקומי הכפתורים
    def positions_btn(self):
        self.btn_add.place(x=60, y=230)
        self.btn_edit_img.place(x=30, y=320)
        self.btn_save_changes.place(x=350, y=230)
        self.btn_exit.place(x=260, y=320)
        self.btn_blank.place(x=390, y=320)

    def positions_edit_btn(self):
        self.btn_add_shape.place(x=100, y=70)
        self.btn_cut.place(x=400, y=70)
        self.btn_add_text.place(x=115, y=170)
        self.btn_set_color.place(x=415, y=170)

    def position_images_btn(self):
        self.btn_apply_colormap_jet.place(x=40, y=300)
        self.btn_apply_colormap_bone.place(x=170, y=300)
        self.btn_original.place(x=300, y=300)
        self.btn_apply_colormap_autumn.place(x=430, y=300)
        self.btn_apply_colormap_hsv.place(x=560, y=300)

    def add_text(self):
        input_text = simpledialog.askstring(title="add text", prompt="your text:")
        if input_text:
            print(input_text)
            self.img.add_text(input_text)


    def draw_rectangle(self):
        self.img.draw_rectangle()
        self.shape_win.destroy()


    def draw_circle(self):
        self.img.draw_circle()
        self.shape_win.destroy()

    def draw_triangle(self):
        self.img.draw_triangle()
        self.shape_win.destroy()

    def draw_line(self):
        self.img.draw_line()
        self.shape_win.destroy()

    def crop_img(self):
        self.img.crop_img()

    def set_color(self):
        self.img.set_color()

    def apply_colormap_jet(self):
        self.img.apply_colormap_jet()

    def apply_colormap_autumn(self):
        self.img.apply_colormap_autumn()

    def set_color_original(self):
        self.img.reset_to_original()

    def apply_colormap_bone(self):
        self.img.apply_colormap_bone()

    def apply_colormap_hsv(self):
        self.img.apply_colormap_hsv()

    def save_changes(self):
        if self.img is None:
            messagebox.showerror("Error! No image selected", "Oh! You haven't chosen a picture yet🙄")
        else:
            save_path = fd.asksaveasfilename(defaultextension=".jpg",
                                             filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")])
            if save_path:
                self.img.save_change(save_path)

    def exit(self):
        answer = askyesno(title='Exit', message='Are you sure you want to Exit?')
        if answer:
            self.win.destroy()


m = MyWindow()


