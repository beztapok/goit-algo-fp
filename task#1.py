class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        # Вставляє новий вузол з даними на початок списку
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        # Вставляє новий вузол з даними в кінець списку
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        # Вставляє новий вузол після заданого попереднього вузла
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        # Видаляє вузол з заданими даними зі списку
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        # Пошук елемента за значенням у списку. Повертає вузол або None, якщо не знайдено
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        # Виводить усі елементи списку
        current = self.head
        while current:
            print(current.data, "-->", end="")
            current = current.next
        print('None')

    def reverse(self):
        # Реверсує однозв'язний список, змінюючи посилання між вузлами
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next  # Зберігаємо наступний вузол
            current.next = prev  # Міняємо напрямок посилання
            prev = current  # Рухаємо prev вперед
            current = next_node  # Рухаємо current вперед
        self.head = prev  # Змінюємо голову списку на останній оброблений вузол

    def merge_sort(self, head):
        # Реалізація сортування злиттям для однозв'язного списку
        if head is None or head.next is None:
            return head

        middle = self.get_middle(head)  # Отримуємо середній вузол
        next_to_middle = middle.next

        middle.next = None  # Розділяємо список на дві частини

        left = self.merge_sort(head)  # Рекурсивно сортуємо ліву частину
        right = self.merge_sort(next_to_middle)  # Рекурсивно сортуємо праву частину

        sorted_list = self.sorted_merge(left, right)  # Об'єднуємо відсортовані частини

        return sorted_list

    def get_middle(self, head):
        # Пошук середнього елемента в однозв'язному списку
        if head is None:
            return head

        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def sorted_merge(self, a, b):
        # Об'єднує два відсортованих списки в один відсортований список
        result = None

        if a is None:
            return b
        if b is None:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)

        return result

    def merge_sorted_lists(self, list1, list2):
        # Об'єднує два відсортованих однозв'язних списки в один відсортований список
        self.head = self.sorted_merge(list1.head, list2.head)

if __name__ == '__main__':

    first_list = LinkedList()

    first_list.insert_at_beginning(5)
    first_list.insert_at_beginning(10)
    first_list.insert_at_beginning(15)
    first_list.insert_at_end(20)
    first_list.insert_at_end(25)
    print("Зв'язний список:")
    first_list.print_list()

    first_list.reverse()
    print("Зв'язний список після реверсування :")
    first_list.print_list()

    first_list.head = first_list.merge_sort(first_list.head)
    print("Зв'язний список відсортовано:")
    first_list.print_list()

    second_list = LinkedList()
    second_list.insert_at_beginning(59)
    second_list.insert_at_beginning(20)
    second_list.insert_at_beginning(35)

    first_list.merge_sorted_lists(first_list, second_list)
    print("Зв'язний список відсортовано та замерджено:")
    first_list.print_list()
