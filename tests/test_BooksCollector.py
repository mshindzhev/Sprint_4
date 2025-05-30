import pytest


class TestBooksCollector:

    def test_add_new_book_with_name_less_41_symbol_book_added(self, collector):
        collector.add_new_book(name='Колобок')
        assert collector.get_book_genre(name='Колобок') is not None

    def test_add_new_book_with_name_more_41_symbol_book_not_added(self, collector):
        collector.add_new_book(name='Колобок и его друзья с кучей символов пришли сломать нам тест')
        assert collector.get_book_genre(name='Колобок и его друзья с кучей символов пришли сломать нам тест') is None

    def test_set_book_genre_book_available_genre_added(self, collector):
        collector.add_new_book(name='Колобок')
        collector.set_book_genre(name='Колобок', genre='Мультфильмы')
        assert collector.get_book_genre(name='Колобок') is 'Мультфильмы'

    def test_set_book_genre_book_not_available_genre_not_added(self, collector):
        collector.set_book_genre(name='Колобок', genre='Мультфильмы')
        assert collector.get_book_genre(name='Колобок') is not 'Мультфильмы'

    @pytest.mark.parametrize(
        'books, count',
        [
            (['Американский пирог', 'Американский пирог 2', 'Американский пирог 3'], 3),
            (['Американский пирог', 'Американский пирог 2'], 2),
        ]
    )
    def test_get_books_with_specific_genre_return_count_books(self, collector, books, count):
        for book in books:
            collector.add_new_book(book)
        for book in books:
            collector.set_book_genre(name=book, genre='Комедии')
        assert len(collector.get_books_with_specific_genre(genre='Комедии')) == count




