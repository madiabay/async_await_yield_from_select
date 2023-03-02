

def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


class BlaBlaExtention(Exception):
    pass


def sub_gen():
    while True:
        try:
            message = yield
        except StopIteration:
            # print('Ku-Ku!!!!')
            break
        else:
            print(f'.......... {message}')
    
    return 'Returned from sib_gen()'

@coroutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except StopIteration as e:
    #         g.throw(e)

    result = yield from g # with one code line

    print(result)
