from src.counter import count_ocurrences


def test_counter():
    'Para a palavra work deve retornar 14174 instancias'
    assert count_ocurrences('src/jobs.csv', 'work') == 14174
