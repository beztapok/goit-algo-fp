# Визначення страв з їхньою вартістю та калорійністю
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Жадібний алгоритм
def greedy_algorithm(items, budget):
    # Сортуємо страви за зменшенням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_calories = 0
    remaining_budget = budget
    chosen_items = []

    for item, details in sorted_items:
        if details['cost'] <= remaining_budget:
            chosen_items.append(item)
            remaining_budget -= details['cost']
            total_calories += details['calories']

    return total_calories, budget - remaining_budget, chosen_items

# Динамічне програмування
def dynamic_programming(items, budget):
    item_names = list(items.keys())

    # Створюємо таблицю DP, де рядки представляють предмети, а стовпці — бюджет
    dp_table = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]

    # Заповнюємо таблицю динамічного програмування
    for i in range(1, len(items) + 1):
        for w in range(1, budget + 1):
            if items[item_names[i-1]]['cost'] <= w:
                dp_table[i][w] = max(dp_table[i-1][w], dp_table[i-1][w - items[item_names[i-1]]['cost']] + items[item_names[i-1]]['calories'])
            else:
                dp_table[i][w] = dp_table[i-1][w]

    # Відновлення вибраних предметів
    chosen_items = []
    w = budget
    for i in range(len(items), 0, -1):
        if dp_table[i][w] != dp_table[i-1][w]:
            chosen_items.append(item_names[i-1])
            w -= items[item_names[i-1]]['cost']

    return dp_table[len(items)][budget], budget - w, chosen_items

if __name__ == '__main__':
    # Виконання обох алгоритмів
    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print("Greedy Algorithm Result: ", greedy_result)
    print("Dynamic Programming Result: ", dp_result)
