class Box:
    def __init__(self):
        self.boxes = []

    def push(self, number):
        self.boxes.append(number)
        print(f"Поклали коробку {number}")

    def peek(self):
        if self.boxes == []:
            print("Склад порожній")
            return None
        return self.boxes[-1]

    def pop(self):
        if self.boxes == []:
            print("Склад порожній, нічого знімати")
            return None
        number = self.boxes.pop()
        print(f"Зняли коробку {number}")
        return number

    def show(self):
        if self.boxes == []:
            print("Склад порожній")
            return None
        print("Коробки (зверху вниз):")
        for number in reversed(self.boxes):
            print(number)


stack = Box()
stack.show()

print()
stack.push(101)
stack.push(102)
stack.push(103)
stack.push(104)
stack.push(105)

print()
print("Верхня коробка:", stack.peek())

print()
stack.pop()
stack.pop()

print()
stack.show()