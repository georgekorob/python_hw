import utils
import sys

# Если вызов скрипта идет "без" аргументов (тестовый режим)
if len(sys.argv) < 2:
    print(utils.cr('USD'))
    print(utils.cr('eur'))
    print(utils.cr('sdd'))
else:
    val = utils.cr(sys.argv[1])
    if val:
        print(f"{val['exc']}, {val['date']}")
    else:
        print(val)
