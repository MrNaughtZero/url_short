from app import app
from app.models import Links
from flask import render_template, url_for, redirect, request, flash, get_flashed_messages

@app.route('/', methods=['GET'])
def index():
    return render_template('main.html', message=get_flashed_messages())

@app.route('/submit', methods=['POST'])
def add_link():
    old_link = request.form.get('old-link')
    new_link = Links.generateNewLink()

    Links(old_link=old_link, new_link=new_link).add()
    flash(new_link)
    return redirect(url_for('index'))

@app.route('/<link>', methods=['GET'])
def view_link(link):
    query = Links().query_link(link)
    if not query:
        return abort(404)
    else:
        return redirect(query, 302)