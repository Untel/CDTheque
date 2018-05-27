from models.collection import *
from models.album import *
from utils.database import *
from ui.home import *


db = Database()

collection = Collection([])
collection.retrieve()
db.close()

if __name__ == '__main__':
	app = ApplicationBasic(collection)
        app.run()
