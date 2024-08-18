import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    # Ініціалізація лічильника для кожної можливої суми (від 2 до 12)
    sums_count = {i: 0 for i in range(2, 13)}
    
    # Симуляція кидків
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)  # Перший кубик
        die2 = random.randint(1, 6)  # Другий кубик
        result = die1 + die2
        sums_count[result] += 1  # Збільшення лічильника для відповідної суми
    
    # Обчислення ймовірності для кожної суми
    probabilities = {sum_: count / num_rolls for sum_, count in sums_count.items()}
    
    return probabilities

def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    
    # Створення графіка
    plt.bar(sums, probs, tick_label=sums, color='skyblue')
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірність суми чисел на двох кубиках')
    
    # Додавання відсотків випадання на графік
    for i, prob in enumerate(probs):
        plt.text(sums[i], prob, f"{prob*100:.2f}%", ha='center')
    
    plt.show()

if __name__ == "__main__":
    for accuracy in [100, 1000, 10000, 100000]:
        print(f"Симуляція для {accuracy} кидків:")
        
        # Симуляція кидків і обчислення ймовірностей
        probabilities = simulate_dice_rolls(accuracy)
        
        # Виведення результатів
        for sum_, prob in probabilities.items():
            print(f"Сума: {sum_}, Ймовірність: {prob*100:.2f}%")
        
        # Відображення ймовірностей на графіку
        plot_probabilities(probabilities)
