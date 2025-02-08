from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Cardápio com nome e preço dos items
menu = {
    "Sanduíches":{
        "Cachorro Quente": 12.00,
        "X-Burger": 15.00,
        "X-Salada": 17.00,
        "X-Bacon": 20.00,
        "X-Tudo": 25.00
    },
    "Acompanhamentos":{
        "Batata Frita (Pequena)": 8.00,
        "Batata Frita (Média)": 12.00,
        "Batata Frita (Grande)": 14.00
    },
    "Bebidas Geladas":{
        "Água Mineral (Sem Gás)": 3.00,
        "Água Mineral (Com Gás)": 3.50,
        "Refrigerante (Lata)": 5.00,
        "Refrigerante (600ml)": 9.00,
        "Suco Natural": 8.00,
        "Energético": 14.00,
        "Chá Gelado": 7.50
    },
    "Bebidas Quentes":{
        "Café Expresso": 5.00,
        "Chá Quente": 6.00,
        "Cappuccino": 9.00,
        "Chocolate Quente": 12.00
    },
    "Sobremesas":{
        "Casquinha de Soverte": 6.00,
        "Sundae": 12.00,
        "Milksake": 16.00,
        "Brownie com Sorvete": 18.00
    }
}

# Carrinho de compras, inicialmente vazio
cart = {}

# Função para adicionar um item ao carrinho
def add_to_cart(item, price):
    if item in cart:
        cart[item] += 1 # Se o item já estiver no carrinho, aumenta a quantidade
    else:
        cart[item] = 1 # Caso contrário, adicionar o item ao carrinho com quantidade 1
    update_cart_display()

# Função para atualizar a exibição do carrinho
def update_cart_display():
    cart_display.delete(1.0, END) # limpa a tela antes de atualizar
    total = 0

    # Comparação entre o conteúdo dos dicionários menu e cart para a identificação quais items do menu foram adicionados ao carrinho e sua quantidade:
    for item_type, item_option in menu.items(): # Separação dos dicionario principal e seus sub-dicionários
        for item, price in item_option.items(): # Separação do conteúdo dos sub-dicionários, definindo os items e seus preços
            for chosen_item, quantity in cart.items(): # Separação do conteúdo do diconário carrinho, definindo os items e sua quantidade
                if item == chosen_item: # Comparação ente itens do menu e itens no carrinho para identificação de preços
                    total += price * quantity
                    cart_display.insert(END, f"{item} x {quantity} - R$ {price * quantity:.2f}\n")

    cart_display.insert(END, f"\nTotal: R$ {total:.2f}")

# Função para finalizar a compra
def checkout():
    total = 0
    if not cart:
        messagebox.showwarning("Carrinho Vazio", "Adicione items ao carrinho antes de finalizar.")
        return
    
    # Comparação entre o conteúdo dos dicionários menu e cart de funçao similar a presente da função update_cart_display(), mas que é usada para definir o valor final da compra: 
    for item_type, item_option in menu.items():
        for item, price in item_option.items():
            for chosen_item, quantity in cart.items():
                if item == chosen_item:
                    total += price * quantity
    
    messagebox.showinfo("Compra finalizada", f"Compra realizada com sucesso!\nTotal: R$ {total:.2f}")
    cart.clear() # Limpa o carrinho após finalizar
    update_cart_display() # Atualiza a exibição do carrinho

# Função para cancelamento de compra, limpando todos os items adicionados ao carrinho
def remove_from_cart():
    cart.clear()
    update_cart_display()

# Função para retornar ao menu principal do cardápio
def return_to_main():
    if frame_sanduiches.winfo_viewable():
        frame_sanduiches.pack_forget()

    elif frame_acompanhamentos.winfo_viewable():
        frame_acompanhamentos.pack_forget()

    elif frame_bebidas_geladas.winfo_viewable():
        frame_bebidas_geladas.pack_forget()
    
    elif frame_bebidas_quentes.winfo_viewable():
        frame_bebidas_quentes.pack_forget()

    elif frame_sobremesas.winfo_viewable():
        frame_sobremesas.pack_forget()

    menu_frame.pack(pady=10, before=cart_frame)

# Função para acessar os submenus do cardápio
def acess_submenu_buttons(item_type, item_option):
    menu_frame.pack_forget()
    
    if item_type == "Sanduíches":
        frame_sanduiches.pack(pady=10, before=cart_frame)

    elif item_type == "Acompanhamentos":
        frame_acompanhamentos.pack(pady=10, before=cart_frame)

    elif item_type == "Bebidas Geladas":
        frame_bebidas_geladas.pack(pady=10, before=cart_frame)

    elif item_type == "Bebidas Quentes":
        frame_bebidas_quentes.pack(pady=10, before=cart_frame)

    elif item_type == "Sobremesas":
        frame_sobremesas.pack(pady=10, before=cart_frame)

# Função para criar os botões dos submenus do cardápio
def create_submenu_buttons(frame1, frame2, frame3, frame4, frame5):
    for item_type, item_option in menu.items():
        if item_type == "Sanduíches":
            for item, price in item_option.items():
                bt = ttk.Button(frame1, text=f"Adicionar {item} - R$ {price:.2f}", command=lambda item=item, price=price: add_to_cart(item, price))
                bt.pack(fill=X, padx=5, pady=5)

            return_bt = ttk.Button(frame1, text="Voltar", command=return_to_main)
            return_bt.pack(fill=X, padx=5, pady=5)
        
        elif item_type == "Acompanhamentos":
            for item, price in item_option.items():
                bt = ttk.Button(frame2, text=f"Adicionar {item} - R$ {price:.2f}", command=lambda item=item, price=price: add_to_cart(item, price))
                bt.pack(fill=X, padx=5, pady=5)

            return_bt = ttk.Button(frame2, text="Voltar", command=return_to_main)
            return_bt.pack(fill=X, padx=5, pady=5)

        elif item_type == "Bebidas Geladas":
            for item, price in item_option.items():
                bt = ttk.Button(frame3, text=f"Adicionar {item} - R$ {price:.2f}", command=lambda item=item, price=price: add_to_cart(item, price))
                bt.pack(fill=X, padx=5, pady=5)

            return_bt = ttk.Button(frame3, text="Voltar", command=return_to_main)
            return_bt.pack(fill=X, padx=5, pady=5)
        
        elif item_type == "Bebidas Quentes":
            for item, price in item_option.items():
                bt = ttk.Button(frame4, text=f"Adicionar {item} - R$ {price:.2f}", command=lambda item=item, price=price: add_to_cart(item, price))
                bt.pack(fill=X, padx=5, pady=5)

            return_bt = ttk.Button(frame4, text="Voltar", command=return_to_main)
            return_bt.pack(fill=X, padx=5, pady=5)

        elif item_type == "Sobremesas":
            for item, price in item_option.items():
                bt = ttk.Button(frame5, text=f"Adicionar {item} - R$ {price:.2f}", command=lambda item=item, price=price: add_to_cart(item, price))
                bt.pack(fill=X, padx=5, pady=5)

            return_bt = ttk.Button(frame5, text="Voltar", command=return_to_main)
            return_bt.pack(fill=X, padx=5, pady=5)

# Função para criar os botões e adicionar ao carrinho para cada item
def create_menu_buttons(frame):
    for item_type, item_option in menu.items():
        bt = ttk.Button(frame, text=f"Cardápio de {item_type}", command=lambda item_type=item_type, item_option=item_option: acess_submenu_buttons(item_type, item_option))
        bt.pack(fill=X, padx=5, pady=5)

# Configuração da interface gráfica (GUI)
root = Tk()
root.title("Sistema de Vendas - Restaurante/Lanchonete")
root.geometry("500x600+250+50")
root.resizable(False, False)

# Frame para o cardápio
menu_frame = Frame(root)
menu_frame.pack(padx= 10, pady=10)

# Frames para os submenus do cardápio
frame_sanduiches = Frame(root)
frame_acompanhamentos = Frame(root)
frame_bebidas_geladas = Frame(root)
frame_bebidas_quentes = Frame(root)
frame_sobremesas = Frame(root)

# Frame para o carrinho
cart_frame = Frame(root)
cart_frame.pack(pady=10)

cart_label = ttk.Label(cart_frame, text="Carrinho de Compras", font=("Arial", 14))
cart_label.pack()

# Exibição do carrinho
cart_display = Text(cart_frame, height=10, widt=40)
cart_display.pack()

# Botões de finalizar a compra e remover itens
checkout_button = ttk.Button(cart_frame, text="Finalizar Compra", command=checkout)
checkout_button.pack(pady=10)

# Botão para cancelamento de compra
cancel_button = ttk.Button(cart_frame, text="Cancelar Compra", command=remove_from_cart)
cancel_button.pack()

# Criação dos botões do cardápio
create_menu_buttons(menu_frame)

# Criação dos botões dos submenus do cardápio
create_submenu_buttons(frame_sanduiches, frame_acompanhamentos, frame_bebidas_geladas, frame_bebidas_quentes, frame_sobremesas)

root.mainloop()