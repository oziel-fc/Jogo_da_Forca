import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk
import webbrowser
import json
import random
import time
from unidecode import unidecode

path = Path(__file__).parent

class Game:
    # Iniciando um frame principal para adicionar elementos nele
    def __init__(self, window):
        # Váriaveis de acesso
        self.only_once_json = True
        self.hits_counter = 0
        self.fails_counter = 0
        self.score_text = str()
        self.height_button = 0.0889
        self.width_button = 0.0667

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
    

    # Função que carrega a imagem principal da tela
    def hangman(self, img_path=path / "imgs" / "hangman.png"):
        self.img_h = Image.open(img_path).resize((250, 250))
        self.img_tk = ImageTk.PhotoImage(self.img_h)

        # Verifica se existe uma label, se não existir é criado, se já existe é atualizado
        if not hasattr(self, "hangman_img"):
            self.hangman_img = tk.Label(self.window, image=self.img_tk, bg=self.color_bg)
            self.hangman_img.image = self.img_tk
            self.hangman_img.place(rely=0.3, relx=0.5, anchor="center")
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

    # Mostra tamanho da palavra e mostra as letras na tela em caso de acerto
    def show_word(self):
        self.word_tip = self.return_json()
        self.word = self.word_tip["word"]
        
        # Imprime na tela os underlines com a mesma quantidade de letras da palavra
        self.len_word = len(self.word)
        self.underline = self.len_word * "_ "
        self.label_underline = tk.Label(self.window, text=self.underline, font=("Comic Sans MS", 28), background="#F2ECCE")
        self.label_underline.place(rely=0.53, relx=0.5, anchor="center")
        

    # Atualiza a palavra conforme for acertando as letras
    def update_word(self, word, letter):
        underline_chars = list(self.underline) # transforma a var self.underline em uma lista 
        for pos_lttr, l in enumerate(word): # pos_lttr = position letter
            if l == letter:
                underline_chars[pos_lttr * 2] = letter
                self.hits_counter += 1 # contador de acertos

        self.new_word = ''.join(underline_chars) # junta novamente a lista em uma string
        self.underline = self.new_word  # atualiza o underline para refletir a nova palavra
        self.label_underline.config(text=self.underline) # atualiza na tela a letra acertada


    # Função que verifica se a letra existe na palavra
    def verify_letter(self, letter, button):
        button.config(state="disabled", cursor="arrow")

        self.word_tip = self.return_json()
        self.brute_word = self.word_tip["word"] # palavra com acentuações
        self.word = unidecode(self.brute_word) # palavra formatada
        if letter in self.word:
            button.config(background="#A6E07F")
            self.update_word(self.word, letter=letter)
            if self.hits_counter == len(self.word):
                self.window.after(1500, self.clear_frame)
                self.window.after(2500, self.victory_screen)

                # Classificações de acordo com pontuação
                if self.fails_counter == 0:
                    self.score_text = "Lendário"
                elif self.fails_counter == 1:
                    self.score_text = "Excepcional"
                elif self.fails_counter == 2:
                    self.score_text = "Ótimo"
                elif self.fails_counter == 3:
                    self.score_text = "Regular"
                elif self.fails_counter == 4:
                    self.score_text = "Iniciante"
                else:
                    self.score_text = "Ufa! Por pouco!"

        else:
            self.hangman(img_path=path / "imgs" / f"fail_{self.fails_counter}.png")
            button.config(background="#E07F7F")
            if self.fails_counter == 5:
            # Espera um tempo antes de limpar a tela
                self.window.after(1500, self.clear_frame)
                self.score_text = "Mais sorte da próxima vez"
                self.window.after(2500, self.defeat_screen)
            self.fails_counter += 1
    
    
    # Primeira camadas de letras
    def first_layer(self):
        self.letters = "QWERTYUIOP"
        self.size_btn = 0.0667
        self.padding_axisX = 0.0417
        self.between_btn = 0.0279
        for l in self.letters:
            self.btn_letter = tk.Button(self.window, text=l, font=("Comic Sans MS", 20), cursor="hand2")
            self.btn_letter.config(command=lambda l_=l, btn=self.btn_letter: self.verify_letter(l_, btn))
            self.btn_letter.place(relx=self.padding_axisX, rely=0.62, relheight=self.height_button, relwidth=self.width_button)
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
            self.btn_letter.place(relx=self.padding_axisX, rely=0.74, relheight=self.height_button, relwidth=self.width_button)
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
            self.btn_letter.place(relx=self.padding_axisX, rely=0.86, relheight=self.height_button, relwidth=self.width_button)
            self.padding_axisX += self.size_btn + self.between_btn

    
    # Limpa a tela
    def clear_frame(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    # Tela de fim de jogo
    def show_ends_screen(self, title, title_color):
        self.frame_root = tk.Frame(self.window, bg="#FFFFFF")
        self.frame_root.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)
        self.victory_text = tk.Label(self.frame_root, text=title, bg="#FFFFFF", font=("Comic Sans MS", 36), fg=title_color)
        self.victory_text.place(rely=0.07, relx=0.5, anchor="center", relheight=0.1)

        self.score = tk.Label(self.frame_root, text=self.score_text, bg="#FFFFFF", font=("Comic Sans MS", 20))
        self.score.place(rely=0.145, relx=0.5, anchor="center", relheight=0.066)

        self.fails = tk.Label(self.frame_root, text=f"Erros: {self.fails_counter}", bg="#FFFFFF", font=("Comic Sans MS", 20))
        self.fails.place(rely=0.21, relx=0.5, anchor="center", relheight=0.06)

        self.restart_btn = tk.Button(self.frame_root, text="Restart", font=("Comic Sans MS", 20), background="#A6E07F", activebackground="#6FAD45", fg="#163600", 
                                activeforeground="#163600", cursor="hand2", command=lambda: (self.clear_frame, time.sleep(1), Game(window=self.window)))
        self.restart_btn.place(relx=0.5, rely=0.5, width=200, height=80, anchor="center")

        self.reveal_word = tk.Label(self.frame_root, text=f"Palavra: {self.brute_word}", bg="#FFFFFF", font=("Comic Sans MS", 20))
        self.reveal_word.place(rely=0.8, relx=0.5, anchor="center")

    def victory_screen(self):
        self.show_ends_screen(title="Vitória", title_color="#2E7201")

    def defeat_screen(self):
        self.show_ends_screen(title="Derrota", title_color="#720101")


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
        self.window.minsize(width=798, height=600)
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
        Game(self.window)

    def run(self):
        # Inicia o loop principal
        self.window.mainloop()


if __name__ == "__main__":
    app = HomePage()
    app.run()
