"""1. Не используя библиотеки для парсинга, распарсить (получить определённые данные)
файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера."""

info = []
with open("nginx_logs.txt", "r") as f:
    line = f.readline()
    while line:
        # Делим строку по символам пробела
        data = line.split()
        # Находим необходивые нам элементы (используем индексы, так как формат данных изместен и неизменен)
        info += [(data[0], data[5][1:], data[6])]
        line = f.readline()
# Выводим часть массива кортежей
print(f"Список кортежей: {info[:3]}")
