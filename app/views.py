from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # fake user
    posts = [ # fake array of posts
        {
                'author': { 'nickname': 'John'},
                'body': 'Beautiful day in Portland!'
        },
        {
                'author': { 'nickname': 'Suan'},
                'body': 'The Avengers movie was so cool!'
        }

    ]
    return render_template("index.html",
        title = 'Home',
        # 这里模块里的第一个user指的是html里面的变量user，而第二个user指的是函数index里面的变量user
        user = user,
        posts = posts)


