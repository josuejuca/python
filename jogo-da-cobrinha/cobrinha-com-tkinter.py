import tkinter as tk
import random

# Configurações do jogo
WIDTH = 600
HEIGHT = 400
DELAY = 100
DOT_SIZE = 20
SCORE_SIZE = 40

# Inicialização da janela
window = tk.Tk()
window.title("Jogo da Cobra")
window.resizable(False, False)

# Criação do canvas
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Classe da cobra
class Snake:
    def __init__(self):
        self.segments = [(100, 100), (80, 100), (60, 100)]
        self.direction = "Right"
        self.score = 0
        self.food = self.create_food()

    def create_food(self):
        x = random.randint(1, (WIDTH - DOT_SIZE) / DOT_SIZE) * DOT_SIZE
        y = random.randint(1, (HEIGHT - DOT_SIZE) / DOT_SIZE) * DOT_SIZE
        return x, y

    def move(self):
        head = self.segments[0]
        x, y = head

        if self.direction == "Right":
            x += DOT_SIZE
        elif self.direction == "Left":
            x -= DOT_SIZE
        elif self.direction == "Up":
            y -= DOT_SIZE
        elif self.direction == "Down":
            y += DOT_SIZE

        self.segments.insert(0, (x, y))

        if head == self.food:
            self.score += 1
            self.food = self.create_food()
        else:
            self.segments.pop()

    def change_direction(self, direction):
        if direction == "Right" and self.direction != "Left":
            self.direction = direction
        elif direction == "Left" and self.direction != "Right":
            self.direction = direction
        elif direction == "Up" and self.direction != "Down":
            self.direction = direction
        elif direction == "Down" and self.direction != "Up":
            self.direction = direction

    def draw(self):
        canvas.delete("all")

        for segment in self.segments:
            x, y = segment
            canvas.create_rectangle(x, y, x + DOT_SIZE, y + DOT_SIZE, fill="white")

        canvas.create_text(SCORE_SIZE, SCORE_SIZE, text=f"Score: {self.score}", fill="white", font=("Arial", 14), anchor="nw")

        canvas.create_rectangle(self.food[0], self.food[1], self.food[0] + DOT_SIZE, self.food[1] + DOT_SIZE, fill="red")

# Funções de controle
def on_key_press(event):
    if event.keysym == "Right":
        snake.change_direction("Right")
    elif event.keysym == "Left":
        snake.change_direction("Left")
    elif event.keysym == "Up":
        snake.change_direction("Up")
    elif event.keysym == "Down":
        snake.change_direction("Down")

# Inicialização do jogo
snake = Snake()

# Eventos do teclado
window.bind("<KeyPress>", on_key_press)
window.focus_set()

# Loop principal do jogo
def game_loop():
    snake.move()
    snake.draw()
    window.after(DELAY, game_loop)

# Início do jogo
game_loop()

# Execução da janela
window.mainloop()
