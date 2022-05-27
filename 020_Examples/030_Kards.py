import random


suits = [b'\xE2\x99\xA6', b'\xE2\x99\xA5', b'\xE2\x99\xA3', b'\xE2\x99\xA0']
values = [str(s) for s in (range(2, 11))] + ['J', 'Q', 'K', 'A']

deck = [
    {'value': v,
     'suit': s.decode(),
     'score': (lambda v: int(v) if v.isdigit() else (11 if v == 'A' else 10))(v)  # непосредственный вызов(!) лямбды
     } for s in suits for v in values
]
random.shuffle(deck)  # перемешать список

random3 = random.sample(deck, 3)
print('3 случайные карты: ', random3)
print('1 случайная карта из тех 3-х: ', random.choice(random3))

while len(deck) > 0:
    try:
        input()
        # если не перемешивать, то так можно выбрать случайную карту
        # card = deck.pop(random.randint(0, len(deck)-1))
        card = deck.pop(0)
        print(card, end='')
    except EOFError as error:
        break
