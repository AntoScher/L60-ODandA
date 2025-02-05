
class Node:
   def __init__(self, key):
       self.left = None
       self.right = None
       self.val = key

# Функция для добавления нового узла
def insert(root, key):
   if root is None:
       return Node(key)
   else:
       if root.val < key:
           root.right = insert(root.right, key)
       else:
           root.left = insert(root.left, key)
   return root

# Пример использования
root = Node(50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

