import csv
import re
from collections import Counter, OrderedDict

class Movies:

    def __init__(self, path_to_the_file):

        self.path = path_to_the_file
        self.movies = []           
        self.by_id = {}            

        with open(path_to_the_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                movie_id = int(row['movieId'])
                title = row['title']
                genres = row['genres'].split('|') if row['genres'] != '(no genres listed)' else []

                entry = {
                    "movieId": movie_id,
                    "title": title,
                    "genres": genres
                }
                self.movies.append(entry)
                self.by_id[movie_id] = entry


    def dist_by_release(self):
        
        counter = Counter()

        for m in self.movies:
            title = m["title"]
            match = re.search(r"\((\d{4})\)", title)
            if match:
                year = int(match.group(1))
                counter[year] += 1

        sorted_items = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        return OrderedDict(sorted_items)
    

    def dist_by_genres(self):

        counter = Counter()

        for m in self.movies:
            for g in m["genres"]:
                counter[g] += 1

        sorted_items = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        return OrderedDict(sorted_items)


    def most_genres(self, n):
        """
        Топ-n фильмов по количеству жанров: {title: число_жанров}.
        Сортировка по убыванию.
        """
        data = []

        for m in self.movies:
            title = m["title"]
            count = len(m["genres"])
            data.append((title, count))


        data.sort(key=lambda x: x[1], reverse=True)

        top = data[:n]
        return OrderedDict(top)
