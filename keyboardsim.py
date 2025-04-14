import random
import time
import os
import sys
import select

def clear_screen():
    """Очищает экран консоли."""
    os.system('cls' if os.name == 'nt' else 'clear')

def input_with_timeout(timeout):
    """Получает ввод пользователя с таймаутом."""
    start_time = time.time()
    input_data = ""
    while True:
        if time.time() - start_time >= timeout:
            return ""  # Время вышло
        try:
            # Используем select для проверки доступности ввода
            if select.select([sys.stdin], [], [], 0)[0]:
                input_data = sys.stdin.readline().rstrip()  # Считываем ввод
                return input_data
        except KeyboardInterrupt:  # Обрабатываем Ctrl+C
            return ""
        time.sleep(0.01)  # Небольшая задержка, чтобы не занимать процессор

def choose_attempts():
    """Позволяет пользователю выбрать количество попыток."""
    print("Выберите уровень сложности:")
    print("1 - 50 попыток")
    print("2 - 100 попыток")
    print("3 - 150 попыток")

    while True:
        choice = input("Введите номер варианта (1-3): ")
        if choice in ("1", "2", "3"):
            if choice == "1":
                return 50
            elif choice == "2":
                return 100
            else:
                return 150
        else:
            print("Неверный ввод. Пожалуйста, выберите вариант от 1 до 3.")

def choose_alphabet():
    """Позволяет пользователю выбрать алфавит."""
    while True:
        alphabet_choice = input("Выберите алфавит (r - русский, e - английский): ").lower()
        if alphabet_choice == "r":
            return [chr(i) for i in range(ord('а'), ord('я') + 1)]
        elif alphabet_choice == "e":
            return [chr(i) for i in range(ord('a'), ord('z') + 1)]
        else:
            print("Неверный ввод. Пожалуйста, выберите 'r' или 'e'.")

def main():
    """Основная функция тренажера."""
    print("Клавиатурный тренажер!")

    alphabet = choose_alphabet()  # Получаем выбранный алфавит
    attempts = choose_attempts()  # Получаем количество попыток
    time_limit = 4  # Фиксированное время на ответ в секундах

    print(f"Вы выбрали {attempts} попыток, время на ответ: {time_limit} сек")
    print("Введите 'exit' в любой момент игры для выхода.")  # Добавляем подсказку
    input("Нажмите Enter, чтобы начать...")

    score = 0
    total_attempts = 0

    while total_attempts < attempts:
        clear_screen()
        letter = random.choice(alphabet)
        print(f"Введите букву: {letter} (время: {time_limit} сек)")

        user_input = input_with_timeout(time_limit)
        total_attempts += 1

        if user_input.lower() == "exit":
            print("Игра завершена.")
            break

        if user_input == letter:
            score += 1
            print("Верно!")
        elif user_input == "":  # Время вышло
            print(f"Время вышло! Правильный ответ: {letter}")
        else:
            print(f"Неверно! Правильный ответ: {letter}")

        print(f"Ваш счет: {score}/{total_attempts}")
        time.sleep(1)  # Пауза в 1 секунду перед следующим раундом

    print(f"Игра завершена. Ваш итоговый счет: {score}/{total_attempts}")  # Выводим финальный счет

if __name__ == "__main__":
    main()
