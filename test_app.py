import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie
import datetime

EXECUTIVE_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxoS25HVkNDWlZNdHlySmpjZEJ3NSJ9.eyJpc3MiOiJodHRwczovL2Rldml6LmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZTk3MWNjYWQ5ODVlYjBjN2RkYTYyYzMiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTg3OTE5ODEyLCJleHAiOjE1ODc5MjcwMTIsImF6cCI6IjM1dXlsUnhHR2tmMEpKNDFiWGpVYXdqMjVkQU42azM0Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.dAHJO0_LDoWiTcCpv9XXOYy9Al0JMTB9fNqMehJNaI1Jt-tIV10v_8clfPl9HcB7IIixS_C5R3V9ZRLecgLtpyOSZ5ncAtT5WbhELDq4JdiEupPSL3_8jvhkUlYOuzMV0cuWIpHWiCtJhaxJdHXAAAzDfqPiDYEYbVkTtT1z2AA5A8BHvBJ4qiEpAanDz8n89NRUuQFKuv0VpA07wqDwxQBb0-U8jMv4X6pcc69k3-teiFGsX3RxW_NYXhBN05btKT8UNAisEnBG_RrgqxrdfSydFkITdKDD8nazbo-C_DfxuM5c6R7_DqxnsoW6wsIj7KfhSeu_l4YpzmKCo7HfSQ'

class CastingTestCase(unittest.TestCase):
	def setUp(self):
		self.app = create_app()
		self.client = self.app.test_client
		self.headers = {'Content-Type': 'application/json'}
		setup_db(self.app)
		db.create_all()

		self.test_movie = {
			'title': 'New Movie',
			'release_date': datetime.date(2020, 4, 27)
		}

		self.test_actor = {
			'name': 'John Doe',
			'age': 22,
			'gender': 'Male'
		}

		with self.app.app_context():
			self.db = SQLAlchemy()
			self.db.init_app(self.app)
			self.db.create_all()

	def tearDown(self):
		pass

	def test_get_movies(self):
		self.headers.update({'Authorization': 'Bearer ' + EXECUTIVE_TOKEN})
		res = self.client().get('/movies', headers=self.headers)
		data = json.loads(res.data)
		self.assertEqual(data['success'],True)
		self.assertEqual(res.status_code,200)

	def test_get_movies_404(self):
		self.headers.update({'Authorization': 'Bearer ' + EXECUTIVE_TOKEN})
		res = self.client().get('/movie', headers=self.headers)
		data = json.loads(res.data)
		self.assertEqual(res.status_code,404)
		self.assertEqual(data['success'],False)
		self.assertEqual(data['message'],'not found')

	def test_get_actors(self):
		self.headers.update({'Authorization': 'Bearer ' + EXECUTIVE_TOKEN})
		res = self.client().get('/actors', headers=self.headers)
		data = json.loads(res.data)
		self.assertEqual(data['success'],True)
		self.assertEqual(res.status_code,200)

	def test_get_actors(self):
		self.headers.update({'Authorization': 'Bearer ' + EXECUTIVE_TOKEN})
		res = self.client().get('/actor', headers=self.headers)
		data = json.loads(res.data)
		self.assertEqual(res.status_code,404)
		self.assertEqual(data['success'],False)
		self.assertEqual(data['message'],'not found')

	def test_add_actor(self):
		self.headers.update({'Authorization': 'Bearer ' + EXECUTIVE_TOKEN})
		res = self.client().post('/actors/create', json=self.test_actor, headers=self.headers)
		data = json.loads(res.data)
		self.assertEqual(data['success'],True)
		self.assertEqual(res.status_code,200)

	def test_add_actor_422(self):
		infor={'name': 'Joe'}
		res = self.client().post('/actors/create', json=infor, headers=self.headers)
		data = json.loads(res.data)
		self.assertEqual(res.status_code,422)
		self.assertEqual(data['success'],False)
		self.assertEqual(data['message'],'unprocessable')

	def test_add_movie(self):
		self.headers.update({'Authorization': 'Bearer ' + EXECUTIVE_TOKEN})
		res = self.client().post('/movies/create', json=self.test_movie, headers=self.headers)
		data = json.loads(res.data)
		self.assertEqual(data['success'],True)
		self.assertEqual(res.status_code,200)

	def test_add_movie_422(self):
		self.headers.update({'Authorization': 'Bearer ' + EXECUTIVE_TOKEN})
		infor = {'title': 'New'}
		res = self.client().post('/movies/create', json=infor, headers=self.headers)
		data = json.loads(res.data)
		self.assertEqual(res.status_code,422)
		self.assertEqual(data['success'],False)
		self.assertEqual(data['message'],'unprocessable')

	def test_edit_actor(self):
		self.headers.update({'Authorization': 'Bearer ' + EXECUTIVE_TOKEN})
		res = self.client().patch('/actors/patch/2', json=test_actor, headers=self.headers)
		data = json.loads(res.data)
		self.assertEqual(data['success'],True)
		self.assertEqual(res.status_code,200)

	def test_edit_actor_404(self):
		self.headers.update({'Authorization': 'Bearer ' + EXECUTIVE_TOKEN})
		res = self.client().patch('/actors/patch/999', json=test_actor, headers=self.headers)
		data = json.loads(res.data)
		self.assertEqual(res.status_code,404)
		self.assertEqual(data['success'],False)
		self.assertEqual(data['message'],'not found')

	def test_edit_movie(self):
		self.headers.update({'Authorization': 'Bearer ' + EXECUTIVE_TOKEN})
		res = self.client().patch('/movies/patch/1', json=test_movie, headers=self.headers)
		data = json.loads(res.data)
		self.assertEqual(data['success'],True)
		self.assertEqual(res.status_code,200)

	def test_edit_movie_404(self):
		self.headers.update({'Authorization': 'Bearer ' + EXECUTIVE_TOKEN})
		res = self.client().patch('/movies/patch/999', json=test_movie, headers=self.headers)
		data = json.loads(res.data)
		self.assertEqual(res.status_code,404)
		self.assertEqual(data['success'],False)
		self.assertEqual(data['message'],'not found')

	def test_delete_actor(self):
		self.headers.update({'Authorization': 'Bearer ' + EXECUTIVE_TOKEN})
		res = self.client().delete('/actors/delete/1')
		data = json.loads(res.data)
		self.assertEqual(data['success'],True)
		self.assertEqual(res.status_code,200)

	def test_delete_actor_404(self):
		self.headers.update({'Authorization': 'Bearer ' + EXECUTIVE_TOKEN})
		res = self.client().delete('/actors/delete/333')
		data = json.loads(res.data)
		self.assertEqual(res.status_code,404)
		self.assertEqual(data['success'],False)
		self.assertEqual(data['message'],'not found')


	def test_delete_movie(self):
		self.headers.update({'Authorization': 'Bearer ' + EXECUTIVE_TOKEN})
		res = self.client().delete('/movies/delete/1')
		data = json.loads(res.data)
		self.assertEqual(data['success'],True)
		self.assertEqual(res.status_code,200)

	def test_delete_movie_404(self):
		self.headers.update({'Authorization': 'Bearer ' + EXECUTIVE_TOKEN})
		res = self.client().delete('/movies/delete/999')
		data = json.loads(res.data)
		self.assertEqual(res.status_code,404)
		self.assertEqual(data['success'],False)
		self.assertEqual(data['message'],'not found')



