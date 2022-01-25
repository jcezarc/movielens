from model import MovieModel


class Tags(MovieModel):
    file_name = 'movielens/tags.csv'
    display = 'movieId'

    def compare(self, search, row, key):
        if key == 'tag':
            return search in row[key]
        return False
