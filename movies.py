from model import MovieModel


class Movies(MovieModel):
    file_name = 'movielens/movies.csv'
    display = 'title'

    def compare(self, search, row, key):
        if key == 'genres':
            return search in row[key].split('|')
        elif key == 'title':
            return search in row[key]
        elif key in ['ratings', 'tags']:
            return row['movieId'] in search.data
        return False
