import cv2
import imageio as imageio
from tkinter.colorchooser import askcolor
import numpy as np
from tkinter import Tk


class MyImage:
    #כאן נכתוב את כל הפונקציות שמטפלות בתמונה עצמה
    def __init__(self, path, window_name):
        self.window_name = window_name
        self.path = path
        self.original_image_data = imageio.imread(self.path)  # שמירת התמונה המקורית
        self.image = cv2.cvtColor(self.original_image_data, cv2.COLOR_RGB2BGR) #הגדרת הצבע של התמונה
        self.color = (255, 255, 255) #צבע ברירת מחדל - לבן
        self.image = cv2.resize(self.image, (int(self.image.shape[1] / 6), int(self.image.shape[0] / 6))) #הקטנת גודל המונה רספונסיבית
        self.original_image = self.image.copy()  # שמירת העותק המקורי של התמונה שעברה שינוי גודל
        self.clone = self.image.copy()
        self.cropping = False
        self.start_x, self.start_y = 0, 0
        self.ix, self.iy = -1, -1  # קואורדינטות התחלתיות של העכבר

        self.show()  # להראות את התמונה

    # מכאן הפונקציות

    # פונקציה להצגת התמונה
    def show(self):
        cv2.imshow(self.window_name, self.image)

    # פונקציה לציור מלבן
    def draw_rectangle(self):
        def draw_rect_event(event, x, y, flags, param):
            global ix, iy
            if event == cv2.EVENT_LBUTTONDOWN:
                # לחצנו על העכבר השמאלי
                # אנחנו רוצים להתחיל לצייר ריבוע
                ix = x
                iy = y

            elif event == cv2.EVENT_LBUTTONUP:
                # סיימנו לצייר
                cv2.rectangle(self.image, (ix, iy), (x, y), self.color, 6)
                self.show()

        cv2.setMouseCallback(self.window_name, draw_rect_event)

    # ציור משולש
    def draw_triangle(self):
        def draw_triangle_event(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                    self.ix, self.iy = x, y

            if event == cv2.EVENT_LBUTTONUP:
                    # חישוב נקודות המשולש
                    base_x, base_y = self.ix, self.iy
                    top_x, top_y = x, y

                    # נקודות המשולש
                    pts = np.array([[base_x, base_y], [top_x, top_y], [base_x + (top_x - base_x) * 2, base_y]],
                                   np.int32)
                    pts = pts.reshape((-1, 1, 2))
                    self.image = cv2.polylines(self.image, [pts], True, self.color,6)
                    self.show()
                    # self.drawing = False

        cv2.namedWindow(self.window_name)
        cv2.setMouseCallback(self.window_name, draw_triangle_event)

    # ציור עיגול
    def draw_circle(self):
        def draw_circle_event(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                    self.ix, self.iy = x, y
                    # חישוב מרכז וחצאי הצירים של האליפסה
            if event == cv2.EVENT_LBUTTONUP:
                    center_x = (self.ix + x) // 2
                    center_y = (self.iy + y) // 2
                    axes_length = (abs(x - self.ix) // 2, abs(y - self.iy) // 2)

                    # ציור האליפסה
                    self.image = cv2.ellipse(self.image, (center_x, center_y), axes_length, 0, 0, 360, self.color, 3)
                    self.show()

        cv2.setMouseCallback(self.window_name, draw_circle_event)
    # הוספת טקסט
    def add_text(self, text):
        def add_text_event(event, x, y, flags, param):
            # רק כשהכפתור בלחיצה -שים את הכיתוב
            if event == cv2.EVENT_LBUTTONDOWN:
                # for another fonts:
                # https://codeyarns.com/tech/2015-03-11-fonts-in-opencv.html#gsc.tab=0
                font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
                cv2.putText(self.image, text, (x, y), font, 3, self.color, 1, cv2.LINE_AA)
                self.show()

        cv2.setMouseCallback(self.window_name, add_text_event)

    # ציור פס
    def draw_line(self):
        def draw_line_event(event, x, y, flags, param):
            global ix, iy
            if event == cv2.EVENT_LBUTTONDOWN:
                ix = x
                iy = y
            elif event == cv2.EVENT_LBUTTONUP:
                cv2.line(self.image, (ix, iy), (x, y), self.color, 6)
                self.show()

        cv2.setMouseCallback(self.window_name, draw_line_event)


    # שינוי הצבע ע"י בחירת צבע מחלון הצבעים
    def set_color(self):
        try:
            color = askcolor()
            print(color)
            if color[0]:
                self.color = (color[0][2],color[0][1], color[0][0])
                print(self.color)
        except Exception as e:
            print(f"An error occurred: {e}")

    def crop_event(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            # Left mouse button pressed, start cropping
            self.start_x, self.start_y = x, y

        elif event == cv2.EVENT_LBUTTONUP:
            # Left mouse button released, finish cropping
            self.cropping = False
            end_x, end_y = x, y

            if end_x > self.start_x and end_y > self.start_y:
                self.image = self.image[self.start_y:end_y, self.start_x:end_x]
                self.show()

    def crop_img(self):
        cv2.setMouseCallback(self.window_name, self.crop_event)

    # איפוס התמונה למצב המקורי
    def reset_to_original(self):
        self.image = self.original_image.copy()  # חזרה לתמונה המקורית ששמרנו בעת האתחול
        self.clone = self.image.copy()
        self.show()
    # שינוי צבע תמונה 1
    def apply_colormap_autumn(self):
        self.image = cv2.applyColorMap(self.image, cv2.COLORMAP_AUTUMN)
        self.show()

    # שינוי צבע תמונה 2
    def apply_colormap_bone(self):
        self.image = cv2.applyColorMap(self.image, cv2.COLORMAP_BONE)
        self.show()

    # שינוי צבע תמונה 3
    def apply_colormap_jet(self):
        self.image = cv2.applyColorMap(self.image, cv2.COLORMAP_JET)
        self.show()

    # שינוי צבע תמונה 4
    def apply_colormap_hsv(self):
        self.image = cv2.applyColorMap(self.image, cv2.COLORMAP_HSV)
        self.show()

    # שמירת שינויים
    def save_change(self, save_path):
        if self.image is not None:
            cv2.imwrite(save_path, self.image)

