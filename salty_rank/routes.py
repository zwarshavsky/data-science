""" Main router for salty-rank app """
from flask import Flask, jsonify, render_template
from flask_json import FlaskJSON, json_response
from salty_rank import app, db
from salty_rank.models import Troll, Comments


# TODO ADD ROUTES
@app.route('/')
def base():
    """ Base view for API interface """
    return render_template('base.html')


@app.route('/api/trolls', methods=['GET'])
def trolls():
    """ API call for troll table """
    trolls_query = Troll.query.all()
    troll = [troll.serialize_troll() for troll in trolls_query]
    return jsonify(troll)


@app.route('/api/comments', methods=['GET'])
def comments():
    """ API call for comments table """
    comments_query = Comments.query.all()
    comments = [comment.serialize_comments() for comment in comments_query]
    return jsonify(comments)
