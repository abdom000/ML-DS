import os

from movies import Movies
from ratings import Ratings
from tags import Tags
from links import Links

BASE_DIR = os.path.dirname(__file__)

MOVIES_1000 = os.path.join(BASE_DIR, "movies_1000.csv")
RATINGS_1000 = os.path.join(BASE_DIR, "ratings_1000.csv")
TAGS_1000   = os.path.join(BASE_DIR, "tags_1000.csv")
LINKS_1000  = os.path.join(BASE_DIR, "links_1000.csv")


class Tests:

    @classmethod
    def setup_class(cls):
        """
        Создаём объекты один раз для всех тестов.
        """
        cls.movies = Movies(MOVIES_1000)
        cls.ratings = Ratings(RATINGS_1000)
        cls.tags = Tags(TAGS_1000)
        cls.links = Links(LINKS_1000)

    def test_movies_dist_by_release_type_and_sort(self):
        res = self.movies.dist_by_release()

        assert isinstance(res, dict)

        years = list(res.keys())
        counts = list(res.values())

        # типы элементов
        assert all(isinstance(y, int) for y in years)
        assert all(isinstance(c, int) for c in counts)

        # сортировка по значениям по убыванию
        sorted_counts = sorted(counts, reverse=True)
        assert counts == sorted_counts

    def test_movies_dist_by_genres_type_and_sort(self):
        res = self.movies.dist_by_genres()

        assert isinstance(res, dict)

        genres = list(res.keys())
        counts = list(res.values())

        assert all(isinstance(g, str) for g in genres)
        assert all(isinstance(c, int) for c in counts)

        sorted_counts = sorted(counts, reverse=True)
        assert counts == sorted_counts

    def test_movies_most_genres_type_and_sort(self):
        n = 10
        res = self.movies.most_genres(n)

        assert isinstance(res, dict)
        assert len(res) <= n

        titles = list(res.keys())
        nums = list(res.values())

        assert all(isinstance(t, str) for t in titles)
        assert all(isinstance(k, int) for k in nums)

        sorted_nums = sorted(nums, reverse=True)
        assert nums == sorted_nums

    def test_ratings_dist_by_year_type_and_sort(self):
        res = self.ratings.movies.dist_by_year()

        assert isinstance(res, dict)

        years = list(res.keys())
        counts = list(res.values())

        assert all(isinstance(y, int) for y in years)
        assert all(isinstance(c, int) for c in counts)

        sorted_years = sorted(years)
        assert years == sorted_years

    def test_ratings_dist_by_rating_type_and_sort(self):
        res = self.ratings.movies.dist_by_rating()

        assert isinstance(res, dict)

        ratings = list(res.keys())
        counts = list(res.values())

        assert all(isinstance(r, (int, float)) for r in ratings)
        assert all(isinstance(c, int) for c in counts)

        sorted_ratings = sorted(ratings)
        assert ratings == sorted_ratings


    def test_tags_most_words_type_and_sort(self):
        n = 10
        res = self.tags.most_words(n)

        assert isinstance(res, dict)
        assert len(res) <= n

        tags = list(res.keys())
        nums = list(res.values())

        assert all(isinstance(tag, str) for tag in tags)
        assert all(isinstance(num, int) for num in nums)

        sorted_nums = sorted(nums, reverse=True)
        assert nums == sorted_nums

    def test_tags_longest_type_and_sort(self):
        n = 10
        res = self.tags.longest(n)

        assert isinstance(res, list)
        assert len(res) <= n
        assert all(isinstance(tag, str) for tag in res)

        lengths = [len(tag) for tag in res]
        sorted_lengths = sorted(lengths, reverse=True)
        assert lengths == sorted_lengths

    def test_tags_most_popular_type_and_sort(self):
        n = 10
        res = self.tags.most_popular(n)

        assert isinstance(res, dict)
        assert len(res) <= n

        tags = list(res.keys())
        counts = list(res.values())

        assert all(isinstance(tag, str) for tag in tags)
        assert all(isinstance(c, int) for c in counts)

        sorted_counts = sorted(counts, reverse=True)
        assert counts == sorted_counts

    def test_links_top_directors_type_and_sort(self):
        n = 5
        res = self.links.top_directors(n)

        assert isinstance(res, dict)
        assert len(res) <= n

        directors = list(res.keys())
        counts = list(res.values())

        assert all(isinstance(d, str) for d in directors)
        assert all(isinstance(c, int) for c in counts)

        sorted_counts = sorted(counts, reverse=True)
        assert counts == sorted_counts

    def test_links_most_expensive_type_and_sort(self):
        n = 5
        res = self.links.most_expensive(n)

        assert isinstance(res, dict)
        assert len(res) <= n

        titles = list(res.keys())
        budgets = list(res.values())

        assert all(isinstance(t, str) for t in titles)
        assert all(isinstance(b, (int, float)) for b in budgets)

        sorted_budgets = sorted(budgets, reverse=True)
        assert budgets == sorted_budgets
        
if __name__ == '__main__':
    import pytest
    pytest.main([__file__])
