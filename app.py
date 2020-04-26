import os
from flask import Flask, request, abort, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from auth import AuthError, requires_auth
from models import db, Actor, Movie,setup_db

def create_app(test_config=None):
	# create and configure the app
	app = Flask(__name__)
	setup_db(app)
	CORS(app)

	@app.after_request
	def after_request(response):
		response.headers.add('Access-Control-Allow-Headers','Content-Type, Authorization, true')
		response.headers.add('Access-Control-Allow-Methods','GET, PATCH, POST, DELETE, OPTIONS')
		return response

	@app.route('/')
	def login_page():
		return jsonify({
			'message': 'Welcome to the casting agency'
		})

	#@app.route('/login-results')
	#def login_result():
	#	token=res.get('access_token')
	#	session['jwt_token'] = token
	#	return redirect('/home')

	#@app.route('/home')
	#def home():
	#	return 'HELLO'

	@app.route('/actors', methods=['GET'])
	@requires_auth('get:actors')
	def get_actors(jwt):
		actors = Actor.query.all()
		return jsonify({
			'success': True,
			'actors': [actor.format() for actor in actors]
		})

	@app.route('/movies', methods=['GET'])
	@requires_auth('get:movies')
	def get_movies(jwt):
		movies = Movie.query.all()
		return jsonify({
			'success': True,
			'movies': [movie.format() for movie in movies]
		})

	@app.route('/movies/create', methods=['POST'])
	@requires_auth('post:movies')
	def add_movie(jwt):
		body = request.get_json()
		title = body.get('title')
		release_date = body.get('release_date')
		if title:
			try:
				movie = Movie(title=title, release_date=release_date)
				movie.insert()
				return jsonify({
					'success': True,
					'movie': [movie.format()]
				})
			except Exception:
				abort(422)
		abort(404)

	@app.route('/actors/create', methods=['POST'])
	@requires_auth('post:actors')
	def add_actor(jwt):
		body = request.get_json()
		name = body.get('name')
		age = body.get('age')
		gender = body.get('gender')
		if name:
			try:
				actor = Actor(name=name, age=age, gender=gender)
				actor.insert()
				return jsonify({
					'success': True,
					'actor': [movie.format()]
				})
			except Exception:
				abort(422)
		abort(404)

	@app.route('/actors/patch/<int:actor_id>', methods=['PATCH'])
	@requires_auth('patch:actors')
	def patch_actor(jwt, actor_id):
		actor = Actor.query.get(actor_id)
		if actor:
			try:
				body = request.get_json()
				name = body.get('name')
				age = body.get('age')
				gender = body.get('gender')
				if name:
					actor.name = name
				if age:
					actor.age = age
				if gender:
					actor.gender = gender
				actor.update()
				return jsonify({
					'success': True,
					'actor': [actor.format()]
				})
			except Exception:
				abort(422)
		abort(404)

	@app.route('/movies/patch/<int:movie_id>', methods=['PATCH'])
	@requires_auth('patch:movies')
	def patch_movie(jwt, movie_id):
		movie = Movie.query.get(movie_id)
		if movie:
			try:
				body = request.get_json()
				title = body.get('title')
				release_date = body.get('release_date')
				if title:
					movie.title = title
				if release_date:
					movie.release_date = release_date
				movie.update()
				return jsonify({
					'success': True,
					'movie': [movie.format()]
				})
			except Exception:
				abort(422)
		abort(404)	

	@app.route('/actors/delete/<int:actor_id>', methods=['DELETE'])
	@requires_auth('delete:actors')
	def delete_actor(jwt, actor_id):
		actor = Actor.query.get(actor_id)
		if actor:
			try:
				actor.delete()
				return jsonify({
					'success': True,
					'deleted': actor_id
				})
			except Exception:
				abort(422)
		abort(404)

	@app.route('/movies/delete/<int:movie_id>', methods=['DELETE'])
	@requires_auth('delete:movies')
	def delete_movie(jwt, movie_id):
		movie = Movie.query.get(movie_id)
		if movie:
			try:
				movie.delete()
				return jsonify({
					'success': True,
					'deleted': movie_id
				})
			except Exception:
				abort(422)
		abort(404)

	@app.errorhandler(422)
	def unprocessable(error):
		return jsonify({
			"success": False,
			"error": 422,
			"message": "unprocessable"
		}), 422

	@app.errorhandler(404)
	def not_found(error):
		return jsonify({
			"success": False,
			"error": 404,
			"message": "resource not found"
		}), 404


	@app.errorhandler(AuthError)
	def handle_auth_error(ex):
		return jsonify({
			"success": False,
			"error": ex.status_code,
			"message": ex.error
		}), 401

	return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)