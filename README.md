Full Stack Casting Agency API Backend

This project simulates a casting agency. 
The above code only consists of a backend for a frontend which will be available soon.
The casting agency consists of actors and movies. This project has two models used, which are the actors and movies table. The movies table contains all the information about the movies and the actors contain information related to the actors.
The link for the API is :

https://fsnd-capstone-casting.herokuapp.com/


To login and set up an account, you can access the following URL:

https://deviz.eu.auth0.com/authorize?audience=casting&scope=SCOPE&response_type=token&client_id=35uylRxGGkf0JJ41bXjUawj25dAN6k34&redirect_uri=https://fsnd-capstone-casting.herokuapp.com/login-results

The API consists of three roles, Casting Assistant, Casting Director and Executive Producer.
The Casting Assistant, can only view movies and actors.
The Casting Director, can not only view movies and actors, but also add and remove actors.
The Executive Producer, has the same roles as the Casting Director but can also add and remove movies.

The Tokens for each of the roles are available in the setup file to use.

The endpoints for the API are:

GET '/movies'
GET '/actors'
POST '/movies/create'
POST '/actors/create'
PATCH '/movies/patch/<int:movie_id>'
PATCH '/actors/patch/<int:actor_id>'
DELETE '/movies/delete/<int:movie_id>'
DELETE '/actors/delete/<int:actor_id>'

GET '/movies'
This endpoint returns all the available movies in a json format.

GET '/actors'
This endpoint returns all the available actos in a json format.

POST '/movies/create'
This endpoint allows us to create new movie. Since the code is just on backend for now, we have added the /create section in order to make it clearer. However, this endpoint will create movie based on the data given to the page.

POST '/actors/create'
This endpoint allows us to create new actor. Since the code is just on backend for now, we have added the /create section in order to make it clearer. However, this endpoint will create actor based on the data given to the page.

PATCH '/movies/patch/<int:movie_id>'
This endpoint allows us to modify movie in a given database.It will search for the movie based on the id. Since the code is just on backend for now, we have added the /patch section in order to make it clearer. However, this endpoint will edit movie based on the data given to the page.

PATCH '/actors/patch/<int:actor_id>'
This endpoint allows us to modify actor in a given database.It will search for the actor based on the id Since the code is just on backend for now, we have added the /patch section in order to make it clearer. However, this endpoint will edit actor information based on the data given to the page.

DELETE '/movies/delete/<int:movie_id>'
This endpoint allows us to delete movie. Since the code is just on backend for now, we have added the /delete section in order to make it clearer. However, this endpoint will delete movie based on the movie_id given to the endpoint.

DELETE '/actors/delete/<int:actor_id>'
This endpoint allows us to delete actor. Since the code is just on backend for now, we have added the /delete section in order to make it clearer. However, this endpoint will delete actor based on the actor_id given to the endpoint.
