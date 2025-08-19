# 🕹️ Jogo da Forca feito em Python

Um projeto de jogo da forca interativo desenvolvido com a biblioteca **Tkinter** do Python e compilado para um executável com **PyInstaller**. Inclui interface gráfica amigável, sistema de dicas e contagem de erros com atualizações visuais. Projeto idealizado visando mostrar competências com **Python** em um portfólio para o **GitHub**.

## Características

* Interface gráfica com **Tkinter**
* **Dicas e palavras**, organizadas em um arquivo `.json`
* Tela inicial com botão de **Start** e link para **GitHub**
* Sistema visual com imagens da forca em estágios (`imgs/fail_0.png` até `fail_6.png`)
* Botões funcionais e com atualizações visuais
* Tela de vitória e derrota com botão de reinício
* Arquitetura organizada em classes
* Código compilado em executável usando a biblioteca **PyInstaller**

## Como jogar
O jogo pode ser executado diretamente via Python pelo arquivo `game.py` ou pelo executável `forca.exe`
1. Executando em Python

    Certique-se que o Python esteja instalado e execute: 

    ```
    python forca/game.py
    ```
    
2. Utilizando o executável:
    * Realizar o [`Download`](https://github.com/oziel-fc/Jogo_da_Forca/releases/download/v1.0/jogo_da_forca.zip)
    * Descompactar arquivo ZIP.
    * Senha: `forca`
    * Executar arquivo `forca.exe`

## Dependências

Este projeto utiliza as seguintes bibliotecas:

### Bibliotecas padrão (incluídas com o Python)

- `tkinter` — Interface gráfica
- `pathlib` — Manipulação de caminhos e arquivos
- `webbrowser` — Abertura de links no navegador
- `json` — Leitura de dicas e palavras
- `random` — Seleção aleatória de palavras
- `time` — Controle de tempo e delays

### Bibliotecas externas

- `Pillow (PIL)` — Manipulação e exibição de imagens
- `unidecode` — Remoção de acentuação das palavras

### Instalação das dependências externas

Use o comando abaixo para instalar apenas as bibliotecas que não fazem parte da instalação padrão do Python:

```
pip install pillow unidecode
```

## Autor
Desenvolvido por [oziel-fc](https://github.com/oziel-fc)

Este projeto faz parte do meu portfólio pessoal. Sinta-se à vontade para explorar, sugerir melhorias ou contribuir!
