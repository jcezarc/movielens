from movies import Movies
from tags import Tags
from ratings import Ratings


def run_tests():
    print('-' * 40)
    print('genres=Comedy, rating >= 3.5, tag="Disney"')
    print('-' * 40)
    best_disney_comedies = Movies(
        genres='Comedy',
        ratings=Ratings(min=3.5),
        tags=Tags(tag='Disney')
    ).data
    for comedy in best_disney_comedies:
        print(comedy)
    print('-' * 40)


run_tests()
