import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk
import webbrowser

path = Path(__file__).parent


class HomePage:
    def __init__(self):
        self.window = tk.Tk()
        self.color_bg = "#F2ECCE"
        self.tab()
        self.home_screen()
        self.start_button()
        self.credits()

    # Configurações da janela
    def tab(self):
        path_ico = path / "imgs" / "icon.ico"
        self.window.iconbitmap(path_ico)
        self.window.title("Forca")
        self.window.geometry("1200x900")
        self.window.configure(bg=self.color_bg)
        self.window.minsize(width=1200, height=900)

    # Configuração tela inicial
    def home_screen(self):
        self.img_path_t = path / "imgs" / "title.png"
        self.img_t = Image.open(self.img_path_t)
        self.img_t = self.img_t.resize((800, 132))
        self.img_tk = ImageTk.PhotoImage(self.img_t)
        self.title_img = tk.Label(self.window, image=self.img_tk, bg=self.color_bg)
        self.title_img.pack(pady=80)

    # Configuração botão de start funcional
    def start_button(self):
        self.start_btn = tk.Button(self.window, text="Start", font=("Comic Sans MS", 20), background="#A6E07F", activebackground="#6FAD45", fg="#163600", 
                                   activeforeground="#163600", cursor="hand2", command=self.clear_page)
        self.start_btn.place(relx=0.44, rely=0.48, width=200, height=80)
    
    # Créditos
    def open_link(self, event=None):
        webbrowser.open("https://github.com/oziel-fc/Jogo_da_Forca")

    def credits(self):
        self.img_path_c = path / "imgs" / "credits.png"
        self.img_c = Image.open(self.img_path_c)
        self.img_c = self.img_c.resize((120, 120))
        self.img_c_tk = ImageTk.PhotoImage(self.img_c)
        self.credits_img = tk.Label(self.window, image=self.img_c_tk, bg=self.color_bg, cursor="hand2")
        self.credits_img.place(relx=0.85, rely=0.8)
        self.credits_img.bind('<Button-1>', self.open_link)

    # Limpar infomações da tela
    def clear_page(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def run(self):
        # Inicia o loop principal
        self.window.mainloop()


if __name__ == "__main__":

    app = HomePage()
    app.run()
