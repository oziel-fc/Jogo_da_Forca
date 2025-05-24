import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk

path = Path(__file__).parent

class JogoForca:
    def __init__(self):
        self.window = tk.Tk()
        self.color_bg = "#F2ECCE"
        self.tab()
        self.home_screen()
    # Configurações da janela
    def tab(self):
        path_ico = path / "imgs" / "icon.ico"
        self.window.iconbitmap(path_ico)
        self.window.title("Forca")
        self.window.geometry("1200x900")
        self.window.configure(bg=self.color_bg)

    def home_screen(self):
        img_path = path / "imgs" / "title.png"
        self.img_ = Image.open(img_path)
        self.img_ = self.img_.resize((200, 50))
        self.img_tk = ImageTk.PhotoImage(self.img_)
        self.title_img = tk.Label(self.window, image=self.img_tk, bg=self.color_bg)

    def run(self):
        # Inicia o loop principal
        self.window.mainloop()


if __name__ == "__main__":
    app = JogoForca()
    app.run()
