from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3
from werkzeug.exceptions import abort


# доделать страницу ошибки если пользователь не ввёл какие-то данные

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/home')
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/thesaurus', methods=('GET', 'POST'))
def thesaurus():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    synonyms = conn.execute('SELECT * FROM synonyms').fetchall()
    antonyms = conn.execute('SELECT * FROM antonyms').fetchall()
    examples = conn.execute('SELECT * FROM examples').fetchall()
    conn.close()
    if request.method == 'POST':
        search = request.form['search']
        if not search:
            flash('Введите запрос!')
        else:
            fin_search = request.form['search']
            desc_base = fin_search[0].strip().upper() + fin_search[1:]
            post = get_post(desc_base)
            return render_template('search.html', posts=posts, post=post, synonyms=synonyms, antonyms=antonyms, examples=examples)
    return render_template("thesaurus.html", posts=posts, synonyms=synonyms, antonyms=antonyms, examples=examples)


@app.route('/texts')
def texts():
    conn = get_db_connection()
    texts = conn.execute('SELECT * FROM texts').fetchall()
    conn.close()
    return render_template("texts.html", texts=texts)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        link = request.form['link']
        date = request.form['date']
        content = request.form['content']
        if not link:
            return render_template('warn.html')
        elif not content:
            return render_template('warn.html')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO texts_from_users (title, link, date, content) VALUES (?, ?, ?, ?)', (title, link, date, content))
            conn.commit()
            conn.close()
            return render_template('thanks.html')
    return render_template('create.html')


def get_post(descriptor):
    conn = get_db_connection()
    desc_base = descriptor[0].strip().upper()+descriptor[1:]
    post = conn.execute('SELECT * FROM posts WHERE  descriptor = ?',
                        (desc_base,)).fetchone()
    if post:
        pass
    else:
        post = conn.execute('SELECT * FROM synonyms WHERE  ascriptor = ?',
                            (desc_base.lower(),)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


@app.route('/<string:desc_base>')
def post(desc_base):
    post = get_post(desc_base)
    return render_template('search.html', post=post)

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
