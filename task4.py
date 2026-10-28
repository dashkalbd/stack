class Closed:
    def __init__(self):
        self.files = []

    def push(self, file):
        self.files.append(file)
        print(f"Закрито файл: {file}")

    def pop(self):
        if self.files == []:
            print("Немає закритих файлів для відновлення")
            return None
        file = self.files.pop()
        print(f"Відновлено файл: {file}")
        return file

    def show(self):
        if self.files == []:
            print("Список закритих файлів порожній")
            return
        print("Закриті файли (від останнього до першого):")
        for file in reversed(self.files):
            print(file)


closed = Closed()

closed.push("report.docx")
closed.push("notes.txt")
closed.push("budget.xlsx")
closed.push("main.py")
closed.push("photo.png")

print()
closed.pop()

print()
closed.show()

print()
closed.pop()
closed.pop()
closed.pop()
closed.pop()
closed.pop()
closed.pop()

print()
print("Перевірка порожнього стека")
closed.show()