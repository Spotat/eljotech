import * from flask


app = Flask(__name__)
app.secret_key = 'secret_key'


@app.route('/')
def home():
    return rend
