import json
import os

class TodoApp:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Завантажує завдання з JSON файлу."""
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []

    def save_tasks(self):
        """Зберігає поточні завдання у JSON файл."""
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.tasks, file, ensure_ascii=False, indent=4)

    def add_task(self, title):
        """Додає нове завдання."""
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "completed": False
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✅ Завдання '{title}' успішно додано!")

    def view_tasks(self):
        """Виводить список усіх завдань."""
        if not self.tasks:
            print("📭 Ваш список справ порожній.")
            return

        print("\n📋 ВАШ СПИСОК СПРАВ:")
        for task in self.tasks:
            status = "🟢 [Виконано]" if task["completed"] else "❌ [Не виконано]"
            print(f"{task['id']}. {status} {task['title']}")
        print()

    def complete_task(self, task_id):
        """Відзначає завдання як виконане."""
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.save_tasks()
                print(f"🎉 Завдання №{task_id} виконано!")
                return
        print("⚠️ Завдання з таким ID не знайдено.")

    def delete_task(self, task_id):
        """Видаляє завдання та перераховує ID."""
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                # Оновлюємо ID для решти завдань, щоб вони йшли по порядку
                for index, remaining_task in enumerate(self.tasks):
                    remaining_task["id"] = index + 1
                self.save_tasks()
                print(f"🗑️ Завдання №{task_id} видалено.")
                return
        print("⚠️ Завдання з таким ID не знайдено.")

def main():
    app = TodoApp()
    
    while True:
        print("\n--- ToDo CLI Меню ---")
        print("1. Переглянути завдання")
        print("2. Додати завдання")
        print("3. Позначити як виконане")
        print("4. Видалити завдання")
        print("5. Вийти")
        
        choice = input("Оберіть дію (1-5): ").strip()
        
        if choice == "1":
            app.view_tasks()
        elif choice == "2":
            title = input("Введіть текст завдання: ").strip()
            if title:
                app.add_task(title)
            else:
                print("⚠️ Текст завдання не може бути порожнім.")
        elif choice == "3":
            try:
                task_id = int(input("Введіть ID завдання: "))
                app.complete_task(task_id)
            except ValueError:
                print("⚠️ Будь ласка, введіть коректне число.")
        elif choice == "4":
            try:
                task_id = int(input("Введіть ID завдання для видалення: "))
                app.delete_task(task_id)
            except ValueError:
                print("⚠️ Будь ласка, введіть коректне число.")
        elif choice == "5":
            print("👋 До побачення!")
            break
        else:
            print("⚠️ Некоректний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
