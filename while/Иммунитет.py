all = 0
yes = 0
while (s := input()) != '':
    all += 1
    if s == 'да':
        yes += 1
if yes / all >= 0.8:
    print('Достигли')
else:
    print('Пока нет')