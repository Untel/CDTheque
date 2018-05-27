from flask import *
from models.collection import *
from models.album import *
from models.person import *


app = Flask(__name__)
col = Collection([])

@app.route('/')
def home():
    col.retrieve()    
    return render_template('home.html', albums=col.get())