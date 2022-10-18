from flask import *

app = Flask(__name__)

# @app.route('/')
# def index():
#     return "<h1>Welcome to Flask Web App</h1>"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/find_price', methods=['GET', 'POST'])
def find_price():
    x = int(request.form['area'])
    y = 4 * x + 3
    return "Price is : %d"%(y)

if __name__ == '__main__':
    app.run()