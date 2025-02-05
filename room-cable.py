import networkx as nx
import matplotlib.pyplot as plt

# Матрица смежности, описывающая расстояния между комнатами
adj_matrix = [
    [0, 4, float('inf'), 7, 9, float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],
    [4, 0, 8, 6, float('inf'), float('inf'), 7, float('inf'), float('inf'), float('inf')],
    [float('inf'), 8, 0, float('inf'), float('inf'), 6, float('inf'), 2, float('inf'), float('inf')],
    [7, 6, float('inf'), 0, 5, float('inf'), float('inf'), float('inf'), 4, float('inf')],
    [9, float('inf'), float('inf'), 5, 0, 3, float('inf'), float('inf'), float('inf'), 8],
    [float('inf'), float('inf'), 6, float('inf'), 3, 0, 2, float('inf'), float('inf'), float('inf')],
    [float('inf'), 7, float('inf'), float('inf'), float('inf'), 2, 0, float('inf'), 5, float('inf')],
    [float('inf'), float('inf'), 2, float('inf'), float('inf'), float('inf'), float('inf'), 0, 3, 7],
    [float('inf'), float('inf'), float('inf'), 4, float('inf'), float('inf'), 5, 3, 0, 2],
    [float('inf'), float('inf'), float('inf'), float('inf'), 8, float('inf'), float('inf'), 7, 2, 0]
]

# Создаем пустой граф
G = nx.Graph()

# Обозначаем комнаты
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

# Заполняем граф ребрами на основе матрицы смежности
for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        if adj_matrix[i][j] != float('inf'):
            G.add_edge(nodes[i], nodes[j], weight=adj_matrix[i][j])

# Применяем алгоритм Прима для нахождения минимального остовного дерева
mst = nx.minimum_spanning_tree(G, algorithm='prim')

# Устанавливаем расположение узлов графа для визуализации
pos = nx.spring_layout(G)  # Метод spring_layout определяет расположение узлов

plt.figure(figsize=(12, 8))  # Задаем размер рисунка

# Рисуем полный граф с весами ребер
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=15)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Подсвечиваем ребра остовного дерева (минимальные расстояния) красным цветом
nx.draw_networkx_edges(mst, pos, edge_color='r', width=2)

# Добавляем легенду к изображению
blue_patch = plt.Line2D([0], [0], color='lightblue', lw=4, label='Комнаты')
black_patch = plt.Line2D([0], [0], color='black', lw=2, label='Кабели')
red_patch = plt.Line2D([0], [0], color='r', lw=4, label='Остовное дерево (Spanning Tree)')
plt.legend(handles=[blue_patch, black_patch, red_patch], loc='upper right')

plt.title("Остовное дерево (Spanning Tree) и Полный Граф")
plt.show()

# Выводим матрицу смежности
print("Матрица смежности:")
for row in adj_matrix:
    print(row)

# Выводим схему разводки кабелей в остовном дереве
print("\nСхема разводки кабелей (Остовное дерево):")
for edge in mst.edges(data=True):
    print(f"{edge[0]} - {edge[1]}, Длина: {edge[2]['weight']}")
