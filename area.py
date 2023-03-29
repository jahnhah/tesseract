import tkinter as tk
from tkinter import filedialog
import pytesseract
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Image to Text")
        self.frame = tk.Frame(self.master)
        self.frame.pack(fill=tk.BOTH, expand=1)
        self.panel_left = tk.Label(self.frame)
        self.panel_left.pack(side=tk.LEFT, padx=10, pady=10)
        self.panel_right = tk.Text(self.frame, wrap=tk.WORD, state=tk.DISABLED)
        self.panel_right.pack(side=tk.RIGHT, padx=10, pady=10)
        self.btn_open = tk.Button(self.frame, text="Open Image", command=self.open_image)
        self.btn_open.pack(side=tk.TOP, pady=10)
        self.btn_reload = tk.Button(self.frame, text="Reload", command=self.reload_image, state=tk.DISABLED)
        self.btn_reload.pack(side=tk.TOP, pady=10)
        self.progressbar = tk.ttk.Progressbar(self.frame, orient='horizontal', mode='indeterminate')
        self.progressbar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        self.progressbar_running = False

    def open_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            img = Image.open(file_path)
            img = img.convert('L')
            self.img_path = file_path
            self.display_image_left(img)
            self.extract_text()

    def reload_image(self):
        img = Image.open(self.img_path)
        img = img.convert('L')
        self.display_image_left(img)
        self.extract_text()

    def extract_text(self):
        self.progressbar_running = True
        self.progressbar.start()
        self.btn_reload.config(state=tk.DISABLED)
        self.panel_right.config(state=tk.NORMAL)
        self.panel_right.delete('1.0', tk.END)
        self.panel_right.insert(tk.END, "Extracting text...")
        self.panel_right.update()
        text = pytesseract.image_to_string(Image.open(self.img_path),config='--psm 6')
        self.panel_right.delete('1.0', tk.END)
        self.panel_right.insert(tk.END, text)
        self.btn_reload.config(state=tk.NORMAL)
        self.progressbar_running = False
        self.progressbar.stop()

    def display_image_left(self, img):
        img = img.resize((400, 400))
        photo = ImageTk.PhotoImage(img)
        self.panel_left.config(image=photo)
        self.panel_left.image = photo
        self.btn_reload.config(state=tk.NORMAL)

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
