from csv import DictReader


class MovieModel:
    def __init__(self, **kwargs):
        csv_file = open(self.file_name, 'r', encoding='utf-8')
        reader = DictReader(csv_file, delimiter=',')
        self.data = set(
            row[self.display] for row in reader
            if all(
                self.compare(search, row, key)
                for key, search in kwargs.items()
            )
        )
        csv_file.close()
