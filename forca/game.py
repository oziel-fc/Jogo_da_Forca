import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk
import webbrowser
import json
import random

path = Path(__file__).parent

class GameScreen:
    # Iniciando um frame principal para adicionar elementos nele
    def __init__(self, window):
        # Pertence a função return_json
        self.only_once_json = True

        self.window = window
        self.color_bg = "#F2ECCE"
        self.frame = tk.Frame(self.window, bg=self.color_bg)
        self.frame.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.hangman()
        self.show_tip()
        self.show_word()
        self.first_layer()
        self.second_layer()
        self.thirty_layer()
        self.fails_counter = 0
    
    
    # Função que carrega a imagem principal da tela
    def hangman(self, img_path=path / "imgs" / "hangman.png"):
        self.img_h = Image.open(img_path).resize((250, 250))
        self.img_tk = ImageTk.PhotoImage(self.img_h)

        # Verifica se existe uma label, se não existir é criado, se já existe é atualizado
        if not hasattr(self, "hangman_img"):
            self.hangman_img = tk.Label(self.window, image=self.img_tk, bg=self.color_bg)
            self.hangman_img.image = self.img_tk
            self.hangman_img.pack(pady=160)
        else:
            self.hangman_img.config(image=self.img_tk)
            self.hangman_img.image = self.img_tk

    
    # Acessa o arquivo JSON e escolhe um dict aleatório com uma palavra e uma dica e retorna
    def return_json(self):
        self.path_json = path / "files" / "words.json"
        if self.only_once_json:
            with open(self.path_json, encoding="utf-8") as self.json_file:
                self.data_json = json.load(self.json_file)

            self.word_tip = random.choice(self.data_json)
            self.only_once_json = False
        
        return self.word_tip

    # Carrega dicas aleatórias e mostra na tela
    def show_tip(self):        
        self.tip = self.return_json()
        self.tip = self.tip["tip"]
        self.text_tip = tk.Label(self.window, text=self.tip, font=("Comic Sans MS", 28), background="#F2ECCE")
        self.text_tip.place(rely=0.075, relx=0.5, anchor="center")

    # Mostra tamanho da palavra e as letras na tela em caso de acerto
    def show_word(self):
        self.word_tip = self.return_json()
        self.word = self.word_tip["word"]
        
        # Imprimir underline na tela
        self.len_word = len(self.word)
        self.underline = self.len_word * "_ "
        self.label_underline = tk.Label(self.window, text=self.underline, font=("Comic Sans MS", 28), background="#F2ECCE")
        self.label_underline.place(rely=0.53, relx=0.5, anchor="center")

    # Atualiza a palavra conforme for acertando as letras
    def update_word(self, word, letter):
        underline_chars = list(self.underline)
        for pos_lttr, l in enumerate(word):
            if l == letter:
                underline_chars[pos_lttr * 2] = letter
        self.new_word = ''.join(underline_chars)
        self.underline = self.new_word  # atualiza o underline para refletir a nova palavra
        print(self.new_word)

    # Função que verifica se a letra existe na palavra
    def verify_letter(self, letter, button):
        button.config(state="disabled", cursor="arrow")

        self.word_tip = self.return_json()
        self.word = self.word_tip["word"]
        if letter in self.word:
            button.config(background="#A6E07F")
            self.update_word(self.word, letter=letter)
            print("Hit")
        else:
            self.fails_counter += 1
            self.hangman(img_path=path / "imgs" / f"fail_{self.fails_counter}.png")
            button.config(background="#E07F7F")
            print(f"Fail n{self.fails_counter}")
    
    
    # Primeira camadas de letras
    def first_layer(self):
        self.letters = "QWERTYUIOP"
        self.size_btn = 0.0667
        self.padding_axisX = 0.0417
        self.between_btn = 0.0279
        for l in self.letters:
            self.btn_letter = tk.Button(self.window, text=l, font=("Comic Sans MS", 20), cursor="hand2")
            self.btn_letter.config(command=lambda l_=l, btn=self.btn_letter: self.verify_letter(l_, btn))
            self.btn_letter.place(relx=self.padding_axisX, y=550, height=80, width=80)
            self.padding_axisX += self.size_btn + self.between_btn
    
    
    # Segunda camadas de letras
    def second_layer(self):
        self.letters = "ASDFGHJKL"
        self.size_btn = 0.0667
        self.padding_axisX = 0.049833
        self.between_btn = 0.038541
        for l in self.letters:
            self.btn_letter = tk.Button(self.window, text=l, font=("Comic Sans MS", 20), cursor="hand2")
            self.btn_letter.config(command=lambda l_=l, btn=self.btn_letter: self.verify_letter(l_, btn))
            self.btn_letter.place(relx=self.padding_axisX, y=663, height=80, width=80)
            self.padding_axisX += self.size_btn + self.between_btn
    
    
    # Terceira camadas de letras
    def thirty_layer(self):
        self.letters = "ZXCVBNM"
        self.size_btn = 0.0667
        self.padding_axisX = 0.0750
        self.between_btn = 0.0639
        for l in self.letters:
            self.btn_letter = tk.Button(self.window, text=l, font=("Comic Sans MS", 20), cursor="hand2")
            self.btn_letter.config(command=lambda l_=l, btn=self.btn_letter: self.verify_letter(l_, btn))
            self.btn_letter.place(relx=self.padding_axisX, y=776, height=80, width=80)
            self.padding_axisX += self.size_btn + self.between_btn


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
        self.window.maxsize(width=1200, height=900)

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
                                   activeforeground="#163600", cursor="hand2", command=self.open_game)
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

    def open_game(self):
        self.clear_page()
        GameScreen(self.window)

    def run(self):
        # Inicia o loop principal
        self.window.mainloop()


if __name__ == "__main__":

    app = HomePage()
    app.run()
