import pytest

from tests.data import BOOK, GENGRE
from helpers import generate_random_book


class TestBooksCollector:

    def test_add_new_book_with_name_less_41_symbol_book_added(self, collector):
        book = generate_random_book()
        collector.add_new_book(name=book)
        assert book in collector.get_books_genre()

    def test_add_new_book_with_name_more_41_symbol_book_not_added(self, collector):
        collector.add_new_book(name='Колобок и его друзья с кучей символов пришли сломать нам тест')
        assert collector.get_book_genre(name='Колобок и его друзья с кучей символов пришли сломать нам тест') is None

    def test_set_book_genre_book_available_genre_added(self, collector):
        collector.add_new_book(name=BOOK)
        collector.set_book_genre(name=BOOK, genre=GENGRE)
        assert collector.get_book_genre(name=BOOK) is GENGRE

    def test_set_book_genre_book_not_available_genre_not_added(self, collector):
        collector.set_book_genre(name=BOOK, genre=GENGRE)
        assert collector.get_book_genre(name=BOOK) is not GENGRE

    @pytest.mark.parametrize(
        'books, books_count',
        [
            (['Американский пирог', 'Американский пирог 2', 'Американский пирог 3'], 3),
            (['Американский пирог', 'Американский пирог 2'], 2),
        ]
    )
    def test_get_books_with_specific_genre_return_filtered_books(self, collector, books, books_count):
        for book in books:
            collector.add_new_book(book)
            collector.set_book_genre(name=book, genre='Комедии')
        assert len(collector.get_books_with_specific_genre(genre='Комедии')) == books_count

    def test_get_books_for_children_return_filtered_books_for_children(self, collector):
        collector.add_new_book(name=BOOK)
        collector.set_book_genre(name=BOOK, genre=GENGRE)
        collector.add_new_book(name='Улица Вязова')
        collector.set_book_genre(name='Улица Вязова', genre='Ужасы')
        assert BOOK in collector.get_books_for_children() and 'Улица Вязова' not in collector.get_books_for_children()

    def test_add_book_in_favorites_available_book_added_in_favorites(self, collector):
        book = generate_random_book()
        collector.add_new_book(name=book)
        collector.add_book_in_favorites(name=book)
        assert book in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_not_available_book_not_added_in_favorites(self, collector):
        book = generate_random_book()
        collector.add_new_book(name=book)
        assert book not in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize(
        'books, deleted_book, count_remained',
        [
            (['Американский пирог', 'Американский пирог 2', 'Американский пирог 3'], 'Американский пирог', 2),
            (['Американский пирог', 'Американский пирог 2'], 'Американский пирог 2', 1)
        ]
    )
    def test_delete_book_from_favorites_success_deleted_book(self, collector, books, deleted_book, count_remained):
        for book in books:
            collector.add_new_book(book)
            collector.add_book_in_favorites(name=book)
        collector.delete_book_from_favorites(name=deleted_book)
        assert len(collector.get_list_of_favorites_books()) == count_remained





