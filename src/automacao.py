import tkinter as tk
from tkinter import filedialog
import os
import sys

class ProdutoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de Produtos HTML")

        self.label_info = tk.Label(root, text="ATENÇÃO!!! Qualquer foto deve estar na pasta 'assets' dentro do diretório do código.", fg="blue")
        self.label_info.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.label_nome = tk.Label(root, text="Nome do Produto")
        self.label_nome.grid(row=1, column=0, padx=10, pady=10)
        self.entry_nome = tk.Entry(root, width=50)
        self.entry_nome.grid(row=1, column=1, padx=10, pady=10)

        self.label_foto = tk.Label(root, text="Foto do Produto")
        self.label_foto.grid(row=2, column=0, padx=10, pady=10)
        self.entry_foto = tk.Entry(root, width=50)
        self.entry_foto.grid(row=2, column=1, padx=10, pady=10)
        self.button_foto = tk.Button(root, text="Escolher Foto", command=self.escolher_foto)
        self.button_foto.grid(row=2, column=2, padx=10, pady=10)

        self.label_preco = tk.Label(root, text="Preço do Produto")
        self.label_preco.grid(row=3, column=0, padx=10, pady=10)
        self.entry_preco = tk.Entry(root, width=50)
        self.entry_preco.grid(row=3, column=1, padx=10, pady=10)

        self.label_categoria = tk.Label(root, text="Categoria do Produto")
        self.label_categoria.grid(row=5, column=0, padx=10, pady=10)
        self.categoria_var = tk.StringVar(root)
        self.categoria_var.set("vestidos.html")  # valor padrão
        self.option_categoria = tk.OptionMenu(root, self.categoria_var, "vestidos.html", "croped.html", "body.html", "shorts.html", "manga_longa.html", "t_shirts.html")
        self.option_categoria.grid(row=5, column=1, padx=10, pady=10)

        self.button_gerar = tk.Button(root, text="Adicionar Produto", command=self.gerar_html)
        self.button_gerar.grid(row=6, column=0, columnspan=3, pady=20)

        self.label_status = tk.Label(root, text="", fg="green")
        self.label_status.grid(row=7, column=0, columnspan=3)

    def escolher_foto(self):
        filepath = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpg *.jpeg *.png")])
        self.entry_foto.insert(0, filepath)

    def gerar_html(self):
        nome = self.entry_nome.get()
        foto = self.entry_foto.get()
        preco = self.entry_preco.get()
        categoria = self.categoria_var.get()

        # Log para verificar se os valores estão corretos
        print(f"Nome: {nome}, Foto: {foto}, Preço: {preco}, Categoria: {categoria}")

        # Obter o caminho do diretório do script/executável
        base_dir = os.path.dirname(sys.argv[0])
        categoria_path = os.path.join(base_dir, categoria)

        # Obter o nome do arquivo da imagem e garantir que esteja na pasta 'assets'
        foto_nome = os.path.basename(foto)
        foto_path = f"/assets/{foto_nome}"

        link_whatsapp = f"https://wa.me/?text=Olá!%20Gostaria%20de%20comprar%20o%20produto%20{nome}%20por%20R${preco}."

        html_produto = f"""
            <div class="product">
                <img src="{foto_path}" alt="{nome}">
                <h3>{nome}</h3>
                <p>R$ {preco}</p>
                <a href="{link_whatsapp}" target="_blank"><button class="buy-button">Comprar</button></a>
            </div>
            <!-- Adicionar mais proodutos aqui -->
        """

        # Verificar se o arquivo de categoria existe antes de abrir
        if not os.path.exists(categoria_path):
            self.label_status.config(text=f"Arquivo '{categoria}' não encontrado.", fg="red")
            print(f"Arquivo '{categoria}' não encontrado.")
            return

        try:
            with open(categoria_path, 'r+', encoding='utf-8') as file:
                content = file.read()
                index = content.find('<!-- Adicionar mais proodutos aqui -->')
                if index != -1:
                    new_content = content[:index] + html_produto + content[index:]
                    file.seek(0)
                    file.write(new_content)
                    file.truncate()
                    self.label_status.config(text="Produto adicionado com sucesso!", fg="green")
                    print("Produto adicionado com sucesso!")
                else:
                    self.label_status.config(text="Comentário 'Adicionar mais proodutos aqui' não encontrado.", fg="red")
                    print("Comentário 'Adicionar mais proodutos aqui' não encontrado.")
        except FileNotFoundError:
            self.label_status.config(text=f"Arquivo '{categoria}' não encontrado.", fg="red")
            print(f"Arquivo '{categoria}' não encontrado.")

        self.limpar_campos()

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_foto.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)
        self.entry_descricao.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ProdutoApp(root)
    root.mainloop()
