from flask import Flask, render_template, request
from database_manager import Mosque

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/add_mosque', methods=['GET', 'POST'])
def add_mosque():
    if request.method == 'POST':
        name = request.form.get('name')
        address = request.form.get('address')
        altitude = request.form.get('altitude')
        longitude = request.form.get('longitude')
        Mosque().add_mosque(name, address, altitude, longitude)
        return "added successfully"
    else:
        return render_template('add_mosque.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        name = request.form.get('name')
        result = Mosque().search(name)
        return str(object=result)
    else:
        return render_template('search.html')


if __name__ == '__main__':
    app.run()
