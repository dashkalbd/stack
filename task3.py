class Settings:
    def __init__(self):
        self.settings_changes = []

    def push(self, setting):
        self.settings_changes.append(setting)
        print(f"Виконано: {setting}")

    def peek(self):
        if self.settings_changes == []:
            print("Налаштування ще не були змінені")
            return None
        return self.settings_changes[-1]

    def pop(self):
        if self.settings_changes == []:
            print("Немає дій для скасування")
            return None
        setting = self.settings_changes.pop()
        print(f"Скасовано: {setting}")
        return setting

    def show(self):
        if self.settings_changes == []:
            print("Історія змін порожня")
            return
        print("Історія змін (від останньої до першої):")
        for setting in reversed(self.settings_changes):
            print(setting)


settings = Settings()

settings.push("Змінено мову на українську")
settings.push("Змінено тему на темну")
settings.push("Змінено розмір шрифту на 14")
settings.push("Змінено гучність на 70%")

print()
print("Остання зміна:", settings.peek())

print()
settings.pop()

print()
settings.show()