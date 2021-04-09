"""2. * (вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) для получения
информации вида:
(<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>),
например:

raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-"
"Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки?
Можно ли для них уточнить регулярное выражение?
"""
import re
# Для создания регулярки в данном случае достаточно знать ограничивающие значения (скобки, ковычки или пробелы)
reg = re.compile(r'(?P<remote_addr>\S+?)\s[^\[]+\['
                 r'(?P<request_datetime>[^\]]+?)\][^\"]+\"'
                 r'(?P<request_type>\S+?)\s'
                 r'(?P<requested_resource>\S+?)\s\S+\s'
                 r'(?P<response_code>\S+?)\s'
                 r'(?P<response_size>\S+?)\s')


def read_log(file_name):
    with open(file_name) as f:
        line = f.readline()
        while line:
            try:
                sear = reg.search(line).groups()
                yield sear
            except AttributeError:
                # В случае некорректного парсинга функция search вернет None и у None нет функции group(),
                # поэтому будет ошибка AttributeError
                # При выполнении кода ни одной "особенной" строки не найдено
                print(f'Некорректный парсинг строки: {line}')
            line = f.readline()


gen = read_log('../06/nginx_logs.txt')
for _ in range(5):
    print(next(gen))
