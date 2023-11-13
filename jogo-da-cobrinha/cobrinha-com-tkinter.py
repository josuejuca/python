import tkinter as tk
import random

# Configurações do jogo
WIDTH = 600
HEIGHT = 400
DELAY = 100
DOT_SIZE = 20
SCORE_SIZE = 10
SCORE_X = 50
SCORE_Y = 20
SNAKE_COLOR = "green"
FOOD_COLOR = "red"

# Inicialização da janela
window = tk.Tk()
window.title("Jogo da Cobra")
window.resizable(False, False)

# Criação do canvas
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Classe da Cobra
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

        if self.segments[0] == self.food:
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

    def check_collision(self):
        head = self.segments[0]
        x, y = head

        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            return True

        for segment in self.segments[1:]:
            if segment == head:
                return True

        return False

    def draw(self):
        canvas.delete("all")

        for segment in self.segments:
            x, y = segment
            canvas.create_rectangle(x, y, x + DOT_SIZE, y + DOT_SIZE, fill=SNAKE_COLOR)

        x, y = self.food
        canvas.create_oval(x, y, x + DOT_SIZE, y + DOT_SIZE, fill=FOOD_COLOR)

        canvas.create_text(SCORE_X, SCORE_Y, text=f"Pontos: {self.score}", fill="white", font=("Arial", SCORE_SIZE))

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

# Configuração do evento de pressionar tecla
window.bind("<KeyPress>", on_key_press)
window.focus_set()

# Loop principal do jogo
def game_loop():
    if not snake.check_collision():
        snake.move()
        snake.draw()
        window.after(DELAY, game_loop)
    else:
        canvas.create_text(WIDTH / 2, HEIGHT / 2, text="Você perdeu!", fill="white", font=("Arial", 20))

# Início do jogo
game_loop()

# Execução da janela
window.mainloop()
