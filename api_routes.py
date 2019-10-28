from app import app
from flask import render_template, jsonify, request,abort
from database import *
from flask import url_for

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/api/user/<int:userid>')
def api_user(userid:int):
    resp = get_user_info(userid)
    if resp == None:
        return jsonify([])
    else:
        return jsonify(resp)

@app.route('/api/article/<int:articleid>')
def api_article(articleid:int):
    resp = get_article_info(articleid)
    if resp == None:
        return jsonify([])
    else:
        return jsonify(resp)

@app.route('/api/article/<int:articleid>/comments/')
def api_comments_of_article(articleid:int):
    resp = get_comments_of_article(articleid)
    if resp == None:
        return jsonify([])
    else:
        return jsonify(resp)

@app.route('/api/register_user',methods=['GET','POST'])
def api_register_user():
    return render_template('base.html')

@app.route('/api/user/<int:userid>/articles')
def api_user_articles(userid:int):
    resp = get_user_articles(userid)
    if resp == None:
        return jsonify([])
    else:
        return jsonify(resp)