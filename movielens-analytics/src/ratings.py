import csv
import os
from collections import Counter, OrderedDict, defaultdict
from datetime import datetime
import statistics


class Ratings:

    def __init__(self, path_to_the_file):

        self.path = path_to_the_file

        
        self.ratings = []  

        
        self.by_movie = defaultdict(list)  
        self.by_user = defaultdict(list)   

        with open(path_to_the_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                user_id = int(row['userId'])
                movie_id = int(row['movieId'])
                rating = float(row['rating'])
                ts = int(row['timestamp'])
                year = datetime.utcfromtimestamp(ts).year

                rec = {
                    "userId": user_id,
                    "movieId": movie_id,
                    "rating": rating,
                    "timestamp": ts,
                    "year": year,
                }

                self.ratings.append(rec)
                self.by_movie[movie_id].append(rec)
                self.by_user[user_id].append(rec)

        self.movie_titles = {}  
        dir_ = os.path.dirname(path_to_the_file)
        movies_path = os.path.join(dir_, "movies.csv")

        if os.path.exists(movies_path):
            with open(movies_path, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    mid = int(row['movieId'])
                    self.movie_titles[mid] = row['title']
        else:
            self.movie_titles = {}

        self.movies = self.Movies(self)
        self.users = self.Users(self)

    class Movies:
        def __init__(self, ratings_parent):
            self.ratings_parent = ratings_parent  

        def dist_by_year(self):

            counter = Counter()
            for rec in self.ratings_parent.ratings:
                year = rec["year"]
                counter[year] += 1

            sorted_items = sorted(counter.items(), key=lambda x: x[0])
            return OrderedDict(sorted_items)

        def dist_by_rating(self):

            counter = Counter()
            for rec in self.ratings_parent.ratings:
                r = rec["rating"]
                counter[r] += 1

            sorted_items = sorted(counter.items(), key=lambda x: x[0])
            return OrderedDict(sorted_items)

        def _movie_title(self, movie_id):
            titles = self.ratings_parent.movie_titles
            if movie_id in titles:
                return titles[movie_id]
            return f"movieId {movie_id}"

        def top_by_num_of_ratings(self, n):

            counts = {}
            for movie_id, recs in self.ratings_parent.by_movie.items():
                counts[movie_id] = len(recs)

            sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)

            result = OrderedDict()
            for movie_id, cnt in sorted_items[:n]:
                title = self._movie_title(movie_id)
                result[title] = cnt
            return result

        def top_by_ratings(self, n, metric="average"):

            metrics = {}

            for movie_id, recs in self.ratings_parent.by_movie.items():
                vals = [r["rating"] for r in recs]
                if not vals:
                    continue

                if metric == "median":
                    value = statistics.median(vals)
                else:  
                    value = sum(vals) / len(vals)

                metrics[movie_id] = round(value, 2)

            sorted_items = sorted(metrics.items(), key=lambda x: x[1], reverse=True)

            result = OrderedDict()
            for movie_id, val in sorted_items[:n]:
                title = self._movie_title(movie_id)
                result[title] = val
            return result

        def top_controversial(self, n):

            variances = {}

            for movie_id, recs in self.ratings_parent.by_movie.items():
                vals = [r["rating"] for r in recs]
                if len(vals) < 2:
                    continue  
                var = statistics.pvariance(vals)  
                variances[movie_id] = round(var, 2)

            sorted_items = sorted(variances.items(), key=lambda x: x[1], reverse=True)

            result = OrderedDict()
            for movie_id, var in sorted_items[:n]:
                title = self._movie_title(movie_id)
                result[title] = var
            return result

    class Users(Movies):

        def __init__(self, ratings_parent):
            super().__init__(ratings_parent)

        def dist_by_num_of_ratings(self):
           
            user_counts = {user_id: len(recs)
                           for user_id, recs in self.ratings_parent.by_user.items()}

            counter = Counter(user_counts.values())

            sorted_items = sorted(counter.items(), key=lambda x: x[0])
            return OrderedDict(sorted_items)

        def dist_by_user_metric(self, metric="average"):

            values = []

            for user_id, recs in self.ratings_parent.by_user.items():
                vals = [r["rating"] for r in recs]
                if not vals:
                    continue
                if metric == "median":
                    v = statistics.median(vals)
                else:
                    v = sum(vals) / len(vals)
                values.append(round(v, 2))

            counter = Counter(values)
            sorted_items = sorted(counter.items(), key=lambda x: x[0])
            return OrderedDict(sorted_items)

        def top_by_variance(self, n):

            variances = {}

            for user_id, recs in self.ratings_parent.by_user.items():
                vals = [r["rating"] for r in recs]
                if len(vals) < 2:
                    continue
                var = statistics.pvariance(vals)
                variances[user_id] = round(var, 2)

            sorted_items = sorted(variances.items(), key=lambda x: x[1], reverse=True)
            return OrderedDict(sorted_items[:n])
