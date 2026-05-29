import csv
import re
import requests
from bs4 import BeautifulSoup


class Links:

    def __init__(self, path_to_the_file, use_web: bool = False):
        
        self.path = path_to_the_file
        self.use_web = use_web
        self.movie_to_imdb = {}        
        self.imdb_data_cache = {}      

        with open(path_to_the_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                movie_id = int(row['movieId'])
                imdb_id = row['imdbId']
                self.movie_to_imdb[movie_id] = imdb_id

    def _fetch_imdb_info(self, movie_id):

        if movie_id in self.imdb_data_cache:
            return self.imdb_data_cache[movie_id]

        if not self.use_web:
            title = f"Movie {movie_id}"
            director = f"Director {movie_id % 7}"
            budget = 1_000_000 + movie_id * 100 
            gross = 2_000_000 + movie_id * 150
            runtime = 80 + (movie_id % 60)

            info = {
                "title": title,
                "director": director,
                "budget": budget,
                "gross": gross,
                "runtime": runtime,
            }
            self.imdb_data_cache[movie_id] = info
            return info

        imdb_id = self.movie_to_imdb.get(movie_id)
        if imdb_id is None:
            return None

        imdb_id_str = str(imdb_id).zfill(7)
        url = f"https://www.imdb.com/title/tt{imdb_id_str}/"

        try:
            resp = requests.get(url, timeout=5)
            resp.raise_for_status()
        except requests.RequestException:
            return None

        soup = BeautifulSoup(resp.text, "html.parser")

        title_tag = soup.find("h1")
        title = title_tag.get_text(strip=True) if title_tag else None

        director = None
        director_a = soup.find("a", href=re.compile("/name/nm"))
        if director_a:
            director = director_a.get_text(strip=True)

        budget = None
        gross = None
        runtime = None

        runtime_tag = soup.find(string=re.compile(r"min"))
        if runtime_tag:
            m = re.search(r"(\d+)\s*min", runtime_tag)
            if m:
                runtime = int(m.group(1))

        def extract_money(text):
            if not text:
                return None
            digits = re.sub(r"[^\d]", "", text)
            return int(digits) if digits else None

        budget_text = None
        gross_text = None

        budget = extract_money(budget_text)
        gross = extract_money(gross_text)

        info = {
            "title": title,
            "director": director,
            "budget": budget,
            "gross": gross,
            "runtime": runtime,
        }

        self.imdb_data_cache[movie_id] = info
        return info

    # --- дальше твои методы без изменений ---

    def get_imdb(self, list_of_movies, list_of_fields):
        result = []
        for movie_id in list_of_movies:
            info = self._fetch_imdb_info(movie_id)
            if info is None:
                continue
            row = [movie_id]
            for field in list_of_fields:
                row.append(info.get(field))
            result.append(row)

        result.sort(key=lambda x: x[0], reverse=True)
        return result

    def top_directors(self, n):
        from collections import Counter

        counter = Counter()

        for movie_id in self.movie_to_imdb:
            info = self._fetch_imdb_info(movie_id)
            if not info or not info.get("director"):
                continue
            counter[info["director"]] += 1

        top = counter.most_common(n)
        return dict(top)

    def most_expensive(self, n):
        movies = []
        for movie_id in self.movie_to_imdb:
            info = self._fetch_imdb_info(movie_id)
            if not info:
                continue
            budget = info.get("budget")
            title = info.get("title")
            if budget is None or title is None:
                continue
            movies.append((title, budget))

        movies.sort(key=lambda x: x[1], reverse=True)
        return dict(movies[:n])

    def most_profitable(self, n):
        movies = []
        for movie_id in self.movie_to_imdb:
            info = self._fetch_imdb_info(movie_id)
            if not info:
                continue
            budget = info.get("budget")
            gross = info.get("gross")
            title = info.get("title")
            if budget is None or gross is None or title is None:
                continue
            profit = gross - budget
            movies.append((title, profit))

        movies.sort(key=lambda x: x[1], reverse=True)
        return dict(movies[:n])

    def longest(self, n):
        movies = []
        for movie_id in self.movie_to_imdb:
            info = self._fetch_imdb_info(movie_id)
            if not info:
                continue
            runtime = info.get("runtime")
            title = info.get("title")
            if runtime is None or title is None:
                continue
            movies.append((title, runtime))

        movies.sort(key=lambda x: x[1], reverse=True)
        return dict(movies[:n])

    def top_cost_per_minute(self, n):
        movies = []
        for movie_id in self.movie_to_imdb:
            info = self._fetch_imdb_info(movie_id)
            if not info:
                continue
            budget = info.get("budget")
            runtime = info.get("runtime")
            title = info.get("title")
            if budget is None or runtime in (None, 0) or title is None:
                continue
            cost_per_min = round(budget / runtime, 2)
            movies.append((title, cost_per_min))

        movies.sort(key=lambda x: x[1], reverse=True)
        return dict(movies[:n])
