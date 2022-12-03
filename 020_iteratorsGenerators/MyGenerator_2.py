def degree(next_num_quad=0):
    while True:
        yield next_num_quad**2
        next_num_quad += 1


for x in degree():
    print(x)
    if x >= 100:
        break

print('*'*50)

# передача значения в генератор
# yield всякий раз возвращает заданное выражение вызывающей программе
# Кроме того, если будет вызван метод send() генератора,
# то переданное значение будет принято функцией-генератором в качестве результата выражения yield.

def degree2(next_num_quad=0):
    while True:
        received = yield next_num_quad**2
        if received is None:
            next_num_quad += 1
        else:
            next_num_quad = received


generator = degree2()
while True:
    x1 = next(generator)
    if x1 == 4:
        x1 = generator.send(5)
    print(x1)
    if x1 >= 25:
        break

print('*'*50)

generator = degree2()
x1 = next(generator)
print(x1)
x1 = generator.send(3)
print(x1)

# import yfinance as yf
# tickers = ['LKOH.ME', 'GMKN.ME', 'DSKY.ME', 'NKNC.ME', 'MTSS.ME', 'IRAO.ME', 'SBER.ME', 'AFLT.ME', 'AAPL']
# df_stocks = yf.download(tickers, start='2021-01-01', end='2021-05-31')['Adj Close']
# df_stocks.head()
#
# aapl = yf.Ticker('AAPL')
# history = aapl.history(start="2010-01-01",  end="2021-07-21")
# history.head()
