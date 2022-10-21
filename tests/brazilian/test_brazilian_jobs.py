from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    external_call = read_brazilian_file('tests/mocks/brazilians_jobs.csv')

    "Verifica que a chave 'title' esteja"
    assert external_call[0].get('title')
