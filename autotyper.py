import pyautogui
import time
import random
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import threading
import os
from pynput import keyboard

def human_like_delay(min_delay=0.01, max_delay=0.05):
    time.sleep(random.uniform(min_delay, max_delay))

def simulate_typing_error():
    if random.random() < 0.05:
        wrong_char = random.choice('abcdefghijklmnopqrstuvwxyz')
        pyautogui.typewrite(wrong_char)
        human_like_delay(0.1, 0.3)
        pyautogui.press('backspace')
        human_like_delay(0.05, 0.15)

def random_pause():
    if random.random() < 0.1:
        time.sleep(random.uniform(0.2, 0.8))

def move_mouse_slightly():
    current_x, current_y = pyautogui.position()
    offset_x = random.randint(-10, 10)
    offset_y = random.randint(-10, 10)
    pyautogui.moveTo(current_x + offset_x, current_y + offset_y, duration=random.uniform(0.1, 0.3))

def type_text_human_like(text, status_label, stop_flag):
    status_label.config(text="Digitando...")
    for char in text:
        if stop_flag():
            status_label.config(text="Digitação interrompida!")
            return
        simulate_typing_error()
        pyautogui.typewrite(char)
        human_like_delay()
        if random.random() < 0.1:
            random_pause()
        if random.random() < 0.05:
            move_mouse_slightly()
    status_label.config(text="Digitação concluída!")

class GhostTyperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GhostTyper - AutoTyper Indetectável")
        self.root.geometry("600x500")
        self.root.configure(bg='#333333')
        self.root.attributes('-alpha', 0.95)

        self.stop_flag = False

        style = ttk.Style()
        style.configure('TLabel', background='#333333', foreground='#CCCCCC')
        style.configure('TEntry', fieldbackground='#555555', foreground='#000000')
        style.configure('TButton', background='#666666', foreground='#000000')
        style.configure('TText', background='#555555', foreground='#000000')

        self.logo_label = ttk.Label(root)
        self.load_logo()

        ttk.Label(root, text="Delay inicial (segundos):").pack(pady=5)
        self.delay_entry = ttk.Entry(root, width=10)
        self.delay_entry.insert(0, "3")
        self.delay_entry.pack(pady=5)

        ttk.Label(root, text="Texto a digitar:").pack(pady=5)
        self.text_widget = tk.Text(root, height=8, width=60, bg='#555555', fg='#000000', insertbackground='#FFFFFF')
        self.text_widget.pack(pady=5)

        button_frame = tk.Frame(root, bg='#333333')
        button_frame.pack(pady=10)
        self.start_button = ttk.Button(button_frame, text="Iniciar Digitação (F9)", command=self.start_typing)
        self.start_button.pack(side=tk.LEFT, padx=10)
        self.stop_button = ttk.Button(button_frame, text="Parar Digitação (F10)", command=self.stop_typing, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.status_label = ttk.Label(root, text="Pronto")
        self.status_label.pack(pady=10)

        instructions = "Posicione o cursor no campo alvo e clique em 'Iniciar'. Atalhos: F9 para iniciar, F10 para parar."
        ttk.Label(root, text=instructions, wraplength=500).pack(pady=10)

        def on_press(key):
            try:
                if key == keyboard.Key.f9:
                    self.root.after(0, self.start_typing)
                elif key == keyboard.Key.f10:
                    self.root.after(0, self.stop_typing)
            except AttributeError:
                pass

        self.listener = keyboard.Listener(on_press=on_press)
        self.listener.start()

        self.root.focus_set()

    def load_logo(self):
        logo_path = "logo.png"
        if os.path.exists(logo_path):
            try:
                img = Image.open(logo_path)
                img = img.resize((200, 200), Image.Resampling.LANCZOS)
                self.logo_img = ImageTk.PhotoImage(img)
                self.logo_label.config(image=self.logo_img)
                self.logo_label.pack(pady=10)
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao carregar logo: {e}")
        else:
            self.logo_label.pack(pady=10)

    def start_typing(self):
        text = self.text_widget.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Aviso", "Digite um texto primeiro.")
            return

        try:
            delay = int(self.delay_entry.get())
        except ValueError:
            messagebox.showwarning("Aviso", "Delay deve ser um número inteiro.")
            return

        self.stop_flag = False
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        self.status_label.config(text=f"Iniciando em {delay} segundos...")
        def countdown(count):
            if count > 0 and not self.stop_flag:
                self.status_label.config(text=f"Iniciando em {count} segundos...")
                self.root.after(1000, countdown, count - 1)
            elif not self.stop_flag:
                self.run_typing(text)

        countdown(delay)

    def stop_typing(self):
        self.stop_flag = True
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.status_label.config(text="Parado")

    def run_typing(self, text):
        threading.Thread(target=type_text_human_like, args=(text, self.status_label, lambda: self.stop_flag)).start()

def main():
    root = tk.Tk()
    app = GhostTyperApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()