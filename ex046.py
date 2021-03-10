import time

for c in range(10, -1, -1):
    print('\033[1;97m{}'.format(c))
    time.sleep(1)
print('\033[1;31mKABUM')
time.sleep(0.5)
print('\033[1;32mKABUM')
time.sleep(0.5)
print('\033[1;33mKABUM')
time.sleep(0.5)
print('\033[1;97mKABUM')
time.sleep(0.5)
print('\033[1;36mKABUM')
time.sleep(0.5)


