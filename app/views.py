from flask import render_template
from app import app
from .requests import get_movies

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    popular_movies = get_movies('popular')
    print(popular_movies)
    title = 'Home - The best Movie Review Website Online'
    return render_template('index.html', title=title, popular = popular_movies)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    title = movie_id
    return render_template('movie.html',id = movie_id, title = movie_id)