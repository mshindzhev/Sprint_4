
class TestBooksCollector:

    def test_add_new_book_with_name_less_41_symbol_book_added(self, collector):
        collector.add_new_book(name='Колобок')
        assert collector.get_book_genre(name='Колобок') is not None

    def test_add_new_book_with_name_more_41_symbol_book_not_added(self, collector):
        collector.add_new_book(name='Колобок и его друзья с кучей символов пришли сломать нам тест')
        assert collector.get_book_genre(name='Колобок и его друзья с кучей символов пришли сломать нам тест') is None



