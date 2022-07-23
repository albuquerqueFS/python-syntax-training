def greeting():
    print('Hi')
    yield 1
    print('How are you?')
    yield 2
    print('Are you there?')
    yield 3

generator_f = greeting()

result_a = next(generator_f)
result_b = next(generator_f)
result_c = next(generator_f)
result_c = next(generator_f)
