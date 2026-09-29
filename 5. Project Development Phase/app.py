from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

farms = [
    {"id": 1, "name": "Green Acres", "crop": "Wheat", "acres": 50},
    {"id": 2, "name": "Sunny Valley", "crop": "Corn", "acres": 75}
]

@app.route('/')
def index():
    return render_template('index.html', farms=farms)

@app.route('/add', methods=['POST'])
def add_farm():
    name = request.form.get('name')
    crop = request.form.get('crop')
    acres = int(request.form.get('acres', 0))
    farms.append({"id": len(farms) + 1, "name": name, "crop": crop, "acres": acres})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
