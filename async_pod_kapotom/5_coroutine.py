# корутины или сопрограммы по своей сути это генераторы, которые в процессе работы может принимать извне данные

def subgen():
    message = yield 'Ready to accept message'
    print(f'Subgen received - {message}')


def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner

@coroutine
def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('DOne')
            break
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)
    
    return average