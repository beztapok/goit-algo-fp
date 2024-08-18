import heapq  # Імпортуємо модуль для роботи з бінарною купою
import networkx as nx  # Імпортуємо модуль для роботи з графами
import matplotlib.pyplot as plt  # Імпортуємо модуль для візуалізації графа

# Створення власного вагового графа
G = nx.Graph()
G.add_edge("A", "B", weight=1)
G.add_edge("A", "C", weight=4)
G.add_edge("B", "C", weight=2)
G.add_edge("B", "D", weight=5)
G.add_edge("C", "D", weight=1)
G.add_edge("C", "E", weight=3)
G.add_edge("D", "E", weight=2)

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    # Ініціалізація відстаней до всіх вершин як нескінченність, крім початкової вершини
    shortest_paths = {vertex: float('infinity') for vertex in graph.nodes()}
    shortest_paths[start] = 0

    # Бінарна купа для відбору вершини з мінімальною вагою
    priority_queue = [(0, start)]  # Початкова вершина має вагу 0

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Пропускаємо обробку, якщо ми вже знайшли коротший шлях
        if current_distance > shortest_paths[current_vertex]:
            continue

        # Перевіряємо всі сусідні вершини
        for neighbor, attributes in graph[current_vertex].items():
            distance = attributes['weight']
            new_distance = current_distance + distance

            # Якщо знайдено коротший шлях до сусідньої вершини
            if new_distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return shortest_paths

# Використання алгоритму Дейкстри для знаходження найкоротших шляхів від вершини "A"
shortest_paths = dijkstra(G, "A")
print("Найкоротші шляхи від вершини A до всіх інших вершин:")
for vertex, distance in shortest_paths.items():
    print(f"Відстань до {vertex}: {distance}")

# Візуалізація графа
pos = nx.spring_layout(G)  # Визначаємо позиції для всіх вузлів
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, width=2)
edge_labels = nx.get_edge_attributes(G, 'weight')  # Отримуємо ваги ребер
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

plt.axis("off")  # Вимикаємо осі для чистішого вигляду
plt.show()  # Показуємо граф
