import tkinter as tk
from tkinter import messagebox

# Cardápio com nome e preço dos itens
menu = {
    "Pizza de Calabresa": 35.00,
    "Hamburguer": 20.00,
    "Suco Natural": 8.00,
    "Salada": 15.00,
    "Coca-Cola": 5.00
}

# Carrinho de compras, inicialmente vazio
cart = {}

# Função para adicionar um item ao carrinho
def add_to_cart(item, price):
    if item in cart:
        cart[item] += 1  # Se o item já estiver no carrinho, aumenta a quantidade
    else:
        cart[item] = 1  # Caso contrário, adicionar o item ao carrinho com quantidade 1
    update_cart_display()

# Função para atualizar a exibição do carrinho
def update_cart_display():
    cart_display.delete(1.0, tk.END)  # Limpa a tela antes de atualizar
    total = 0
    for item, quantity in cart.items():
        total += menu[item] * quantity
        cart_display.insert(tk.END, f"{item} x{quantity} - R$ {menu[item] * quantity:.2f}\n")
    cart_display.insert(tk.END, f"\nTotal: R$ {total:.2f}")

# Função para finalizar a compra
def checkout():
    if not cart:
        messagebox.showwarning("Carrinho Vazio", "Adicione itens ao carrinho antes de finalizar.")
        return
    total = sum(menu[item] * quantity for item, quantity in cart.items())
    messagebox.showinfo("Compra Finalizada", f"Compra realizada com sucesso!\nTotal: R$ {total:.2f}")
    cart.clear()  # Limpa o carrinho após finalizar
    update_cart_display()  # Atualiza a exibição do carrinho

# Função para remover um item do carrinho
def remove_from_cart(item):
    if item in cart:
        del cart[item]
        update_cart_display()

# Função para criar os botões de adicionar ao carrinho para cada item
def create_menu_buttons(frame):
    for item, price in menu.items():
        button = tk.Button(frame, text=f"Adicionar {item} - R$ {price:.2f}",
                           command=lambda item=item, price=price: add_to_cart(item, price))
        button.pack(fill=tk.X, padx=5, pady=5)

# Configuração da interface gráfica (GUI)
root = tk.Tk()
root.title("Sistema de Vendas - Restaurante/Lanchonete")
root.geometry("500x500")

# Frame para o cardápio
menu_frame = tk.Frame(root)
menu_frame.pack(pady=10)

# Frame para o carrinho
cart_frame = tk.Frame(root)
cart_frame.pack(pady=10)

cart_label = tk.Label(cart_frame, text="Carrinho de Compras", font=("Arial", 14))
cart_label.pack()

# Exibição do carrinho
cart_display = tk.Text(cart_frame, height=10, width=40)
cart_display.pack()

# Botões de finalizar a compra e remover itens
checkout_button = tk.Button(root, text="Finalizar Compra", command=checkout)
checkout_button.pack(pady=10)

# Criação dos botões do cardápio
create_menu_buttons(menu_frame)

root.mainloop()