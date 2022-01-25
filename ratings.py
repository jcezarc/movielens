from model import MovieModel


class Ratings(MovieModel):
    file_name = 'movielens/ratings.csv'
    display = 'movieId'

    def compare(self, search, row, key):
        value = float(row['rating'])
        if key == 'min':
            return value >= search
        elif key == 'max':
            return value <= search
        return False
