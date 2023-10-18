from main1 import logger

import types


@logger
def flat_generator(list_of_lists):
    for flat_list in list_of_lists:
        for elem in flat_list:
            yield elem

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    print('Генератор')
    for item in flat_generator(list_of_lists_1):
        print(item)


    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()

