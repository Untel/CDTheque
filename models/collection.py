from utils.database import *
from models.album import *
class Collection:
    def __init__(self, albums):
        self._albums = albums
        self.db = Database()

    def add(self, album):
        self._albums.append(album)

    def get(self):
        return self._albums

    def clear(self):
        self.db.query("""
            DELETE * FROM `album`;
            DELETE * FROM `author`;
            DELETE * FROM `interpreter`;
            DELETE * FROM `composer`;
        """)

    def save(self):
        try:
            query = self.db.query("""
                INSERT INTO `album` VALUES (2, "yo", "yo", "yo", 1, 2, 2, 2)
            """)
            self.db.conn.commit()
        except Exception as e:
            print('Err', e)

    def retrieve(self):
        try:
            albums = self.db.query("""
                SELECT * FROM `album`
            """)

            # interpreter = self.db.query("""
            #     SELECT * FROM `interpreter`
            # """)

            # author = self.db.query("""
            #     SELECT * FROM `author`
            # """)

            # composer = self.db.query("""
            #     SELECT * FROM `composer`
            # """)

            for album in albums:
                _album = Album( id = album[0], 
                                name = album[1], 
                                title = album[2],
                                cover = album[3],
                                track = album[4]
                                )
                self.add(_album)

            return self._albums
        except Exception as e:
            print('Err', e)
            return []