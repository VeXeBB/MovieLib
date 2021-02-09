import tmdb_client
from unittest.mock import Mock

def test_get_poster_url_uses_default_size():
    # Wprowadzenie danych do appki
    poster_api_path = "/w342/e1mjopzAS2KNsvpbpahQ1a6SkSn.jpg"
    expected_default_size = 'w342'
    # Wywołanie kodu, który testujemy
    poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
    # Porównywanie
    assert expected_default_size in poster_url

def test_get_movies_list(monkeypatch):
    # Lista, którą będzie zwracać "ZAPYTANIE DO API
    mock_movies_list = ['Movie 1', 'Movie 2']

    requests_mock = Mock()
    # Wynik wywołania API
    response = requests_mock.return_value
    # Przysłoniecie zapytania json
    response.json.return_value = mock_movies_list
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movies_list = tmdb_client.get_movies_list(how_many=8, list_type="popular")
    assert movies_list == mock_movies_list

def test_get_single_movie(monkeypatch):
    mock_movie = ['Movie 1']
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_movie
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movie = tmdb_client.get_single_movie(movie_id=123)
    assert movie == mock_movie

def test_get_single_movie_cast(monkeypatch):
    mock_cast = ['Cast 1']
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_cast
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    cast = tmdb_client.get_single_movie_cast(movie_id=123)
    assert cast == mock_cast