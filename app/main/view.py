from . import main
from flask import render_template
from app.models import *

@main.route('/')
@main.route('/index')
def index():
    categorys=News_Category.query.all()
    news= News.query.order_by(News.id.desc())
    return render_template('index.html',categorys=categorys,news=news)


@main.route('/news/<category>')
def news(category):
    categorys=News_Category.query.all()
    return render_template('index.html',category=category,categorys=categorys,title=category)


@main.app_errorhandler(404)
def page_not_found(e):
    return "this page is not found."
