
class TestBooksCollector:

    def test_add_new_book(self, collector):
        collector.add_new_book(name='Колобок')
        assert collector.get_book_genre(name='Колобок') is not None



