import matplotlib.pyplot as plt
import numpy as np

def draw_branch(x, y, angle, length, depth):
    # Якщо глибина дорівнює нулю, зупиняємо рекурсію
    if depth == 0:
        return
    
    # Обчислення нової координати (x, y) кінця гілки
    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)

    # Малювання гілки від поточної координати до кінцевої
    plt.plot([x, x_end], [y, y_end], color='brown')

    # Зменшуємо довжину гілки для наступного рівня рекурсії
    new_length = length * 0.7

    # Малюємо дві нові гілки під кутом 45 градусів вправо і вліво
    draw_branch(x_end, y_end, angle - np.pi / 4, new_length, depth - 1)
    draw_branch(x_end, y_end, angle + np.pi / 4, new_length, depth - 1)

# Налаштування вікна для малювання
plt.figure(figsize=(8, 8))
plt.axis('off')  # Вимкнути осі для чистішого вигляду

# Глибина рекурсії, яку може задати користувач
depth = int(input("Введіть рівень рекурсії (глибину): "))

# Запуск малювання з початковими параметрами
draw_branch(0, -1, np.pi / 2, 1, depth)

# Показуємо результат
plt.show()
