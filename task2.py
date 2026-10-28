class Hist:
    def __init__(self):
        self.actions = []

    def push(self, action):
        self.actions.append(action)
        print(f"Виконано: {action}")

    def peek(self):
        if self.actions == []:
            print("Історія порожня")
            return None
        return self.actions[-1]

    def pop(self):
        if self.actions == []:
            print("Немає дій для скасування")
            return None
        action = self.actions.pop()
        print(f"Скасовано: {action}")
        return action

    def show(self):
        if self.actions == []:
            print("Історія порожня")
            return None
        print("Дії в історії (від останньої до першої):")
        for action in reversed(self.actions):
            print(action)


history = Hist()

history.push("Додано заголовок")
history.push("Вставлено абзац")
history.push("Змінено шрифт на жирний")
history.push("Додано список")

print()
print("Остання дія:", history.peek())

print()
history.pop()
history.pop()

print()
history.show()