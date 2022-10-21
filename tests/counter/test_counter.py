from src.counter import count_ocurrences


def test_counter():
    'Para um número ímpar a função deve retornar o valor True'
    assert count_ocurrences('src/jobs.csv', 'work') == 14174
