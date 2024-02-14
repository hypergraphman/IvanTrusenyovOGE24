weather = input()
weather += ','
temp = input()
prec = input()
prec += '.'
if prec == 'да.':
    print('Сегодня', weather, temp, 'градусов, осадки')
else:
    print('Сегодня', weather, temp, 'градусов, осадков нет.')