from flask import Flask, render_template, request, redirect, url_for, send_file
import os
from database import init_db
from cleaner_logic import clean_data

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs('static', exist_ok=True)

init_db()

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_csv():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)
            clean_data(file_path)
            return redirect(url_for('catalog'))
    return render_template('upload_csv.html')

@app.route('/catalog')
def catalog():
    return render_template('view_catalog.html')

@app.route('/dropshippers')
def dropshippers():
    return render_template('dropshippers.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

if __name__ == '__main__':
    app.run(debug=True)