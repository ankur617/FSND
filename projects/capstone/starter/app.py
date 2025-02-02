import os
from platform import release
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from models import db_drop_and_create_all, setup_db, Actors, Movies
from auth import AuthError, requires_auth
from datetime import datetime 

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)


    #db_drop_and_create_all()

    # ROUTES
    '''
        GET /movies
        It would get all the movies and return a list
        The user to access this must have privilege 'get:movies'
    '''
    @app.route('/movies')
    @requires_auth('get:movies')
    def getMovies(payload):
        # Select all the movies
        movies = Movies.query.all()

        response = []

        #Iterate through the list of movies and append them into the list
        for movie in movies:
            response.append(movie.view())
        
        #Return the response
        return jsonify({
            "success": True,
            "movies": response
        })

    '''
        GET /actors
        It would get all the actors and return a list
        The user to access this must have privilege 'get:actors'
    '''
    @app.route('/actors')
    @requires_auth('get:actors')
    def getActors(payload):
        # Select all the actors
        actors = Actors.query.all()

        response = []

        #Iterate through the list of actors and append into the list
        for actor in actors:
            response.append(actor.view())
        
        #Return the response
        return jsonify({
            "success": True,
            "actors": response
        })

    '''
        POST /movies
        It would create a movie
        The user to access this must have privilege 'post:movies'
    '''


    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def postMovies(payload):
        # Get the request object
        body = request.get_json()

        #Get the title
        title = body.get("title")
        
        try:
            #Get the release_date
            release_date = datetime.strptime(body.get("release_date"), '%Y-%m-%d')

            # Create the movie object
            movie = Movies(title = title, release_date = release_date)

            movie.insert()

            #If creation is successful return the response
            return jsonify({
                "success": True,
                "movies": movie.view()
            })
        except:
            # If any error abort
            abort(422)

    '''
        POST /actors
        It would create an actor
        The user to access this must have privilege 'post:actors'
    '''


    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def postActors(payload):
        # Get the request object
        body = request.get_json()

        #Get the name
        name = body.get("name")
        
        #Get the age
        age = body.get("age")

        #Get the gender
        gender = body.get("gender")

        
        try:
            # Create the actor object
            actor = Actors(name = name, age = age, gender = gender)
            
            #Validate the age to be integer
            if not type(age) is int:
                raise TypeError("Only integers are allowed")

            #Validate the gender to be male or female
            if not (gender.lower() == 'male' or gender.lower() == 'female'):
                raise ValueError("Gender can only be male or female")

            actor.insert()

            #If creation is successful return the response
            return jsonify({
                "success": True,
                "actors": actor.view()
            })
        except:
            # If any error abort
            abort(422)


    '''
        PATCH /movies/<id>
        It would update attributes of the movie
        The user to access this must have privilege 'patch:movies'
    '''
    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def patchMovie(payload,id):
        
        # Get the JSON request 
        body = request.get_json()
        
        #Get the title
        title = body.get("title", None)

        #Get the release_date
        release_date = body.get("release_date", None)

        #Get the movie based on the id passed
        movie = Movies.query.filter(Movies.id == id).one_or_none()
        
        # If movie not found return 404
        if movie is None:
            abort(404)
        
        try:
            # If title found in the request, change the title
            if title is not None:
                movie.title = title
        
            # If release_date found in the request, change the release_date
            if release_date is not None:
                movie.release_date = datetime.strptime(release_date, '%Y-%m-%d')
                
            # If any one of release_date or title found in the request than update
            if title is not None or release_date is not None:
                movie.update()

        except:
            # If any error abort
            abort(422)
        

        # Return the response object
        return jsonify({
            "success": True,
            "movies": movie.view()
            })

    '''
        PATCH /actors/<id>
        It would update attributes of the actor
        The user to access this must have privilege 'patch:actors'
    '''
    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def patchActors(payload,id):
        print('Patch')
        # Get the JSON request 
        body = request.get_json()
        
        #Get the name
        name = body.get("name", None)

        #Get the age
        age = body.get("age", None)

        #Get the gender
        gender = body.get("gender", None)

        #Get the actor based on the id passed
        actor = Actors.query.filter(Actors.id == id).one_or_none()

        print(actor)
        # If actor not found return 404
        if actor is None:
            print("here")
            abort(404)

        try:
            # If name found in the request, change the title
            if name is not None:
                actor.name = name
        
            # If age found in the request, change the age
            if age is not None:
                actor.age = age

            # If gender found in the request, change the gender
            if gender is not None:
                actor.gender = gender
            
            #Validate the age is integer
            if not (type(age) is int):
                print("insider error")
                raise TypeError("Only integers are allowed")
            
            #Validate the gender is male or female
            if (gender is not None):
                if not (gender.lower() == 'male' or gender.lower() == 'female'):
                    raise ValueError("Gender can only be male or female")

            # If any one of age or name or gender is found in the request than update
            if age is not None or name is not None or gender is not None:
                actor.update()
        
        except:
            # If any error abort
            abort(422)
        
        # Return the response object
        return jsonify({
            "success": True,
            "actors": actor.view()
            })

    '''
        DELETE /movies/<id>
        It would delete a movie
        The user to access this must have privilege 'delete:movies'
    '''

    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def deleteMovies(payload, id):    
        #Get the movie based on the id passed
        movie = Movies.query.filter(Movies.id == id).one_or_none()
        
        #If the movie is not found, return 404
        if movie is None:
            abort(404)
        
        #Delete the movie
        movie.delete()

        #Return the response object
        return jsonify({
                "success": True,
                "delete": id
        })


    '''
        DELETE /actors/<id>
        It would delete an actor
        The user to access this must have privilege 'delete:actors'
    '''

    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def deleteActors(payload,id):    
        #Get the actor based on the id passed
        actor = Actors.query.filter(Actors.id == id).one_or_none()
        
        #If the actor is not found, return 404
        if actor is None:
            abort(404)
        
        #Delete the actor
        actor.delete()

        #Return the response object
        return jsonify({
                "success": True,
                "delete": id
        })

    # Error Handling

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def notFound(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not Found"
        }), 404

    @app.errorhandler(403)
    def auth_403(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": 'You dont have access for this action'
        }), 403

    @app.errorhandler(AuthError)
    def auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        
        return response

    @app.errorhandler(401)
    def unauthorized(ex):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "unauthorized"
        }), 401
    
    return app
    

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)