import time
import os

def realtime_print(filename):
    last_position = 0
    while True:
        try:
            with open(filename, 'r') as file:
                file.seek(last_position)
                new_lines = file.readlines()
                for line in new_lines:
                    print(line.strip())
                last_position = file.tell()
        except FileNotFoundError:
            print(f"Файл не найден: {filename}")
            return
        except Exception as e:
            print(f"Произошла ошибка: {e}")

        time.sleep(0.1)

if __name__ == "__main__":
    file_path = "file.csv"
    realtime_print(file_path)