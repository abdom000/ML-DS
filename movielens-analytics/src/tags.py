import csv
from collections import Counter, OrderedDict


class Tags:

    def __init__(self, path_to_the_file):

        self.path = path_to_the_file

        self.tags = []          
        self.unique_tags = set()  

        with open(path_to_the_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                tag = row["tag"].strip()
                if tag == "":
                    continue
                self.tags.append(tag)
                self.unique_tags.add(tag)


    def most_words(self, n):

        data = []
        for tag in self.unique_tags:
            num_words = len(tag.split())
            data.append((tag, num_words))

        data.sort(key=lambda x: (x[1], x[0]), reverse=True)

        top = data[:n]
        return OrderedDict(top)

    def longest(self, n):

        data = list(self.unique_tags)

        data.sort(key=lambda tag: len(tag), reverse=True)

        return data[:n]

    def most_words_and_longest(self, n):

        top_words_dict = self.most_words(n)  
        top_words = set(top_words_dict.keys())

        top_long = set(self.longest(n))

        inter = sorted(top_words & top_long)

        return inter

    def most_popular(self, n):

        counter = Counter(self.tags)

        sorted_items = sorted(counter.items(), key=lambda x: (x[1], x[0]), reverse=True)

        return OrderedDict(sorted_items[:n])

    def tags_with(self, word):

        word_lower = word.lower()

        result = []
        for tag in self.unique_tags:
            if word_lower in tag.lower():
                result.append(tag)

        result.sort()
        return result
