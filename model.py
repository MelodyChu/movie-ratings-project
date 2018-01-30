"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Model definitions

class User(db.Model):
    """User of ratings website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(64), nullable=True, unique=True)
    password = db.Column(db.String(64), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    zipcode = db.Column(db.String(15), nullable=True)

    def __repr__(self):
        """Provide helpful representation about user when printed."""

        return "<User user_id={} zipcode={} >".format(self.user_id,
                                                   self.email)

# Put your Movie and Rating model classes here.


class Movie(db.Model):
    """Table containing movie info."""

    __tablename__ =  'movies'

    movie_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    released_at = db.Column(db.DateTime, nullable=True)
    imdb_url = db.Column(db.String(250), nullable=True)

    def __repr__(self):
        """Provide helpful representation about user when printed."""

        return "<Movie movie_id={} title={} released_at={}>".format(self.movie_id, self.title, self.released_at)


class Rating(db.Model):
    """Table containing user rating info for movies."""

    __tablename__ = 'ratings'

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    movie_id = db.Column(db.Integer, nullable=False, db.ForeignKey=('movies.movie_id')) #ask about foreign key
    user_id = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Integer, nullable=False) #ask about validating specific range of ratings 1-5

    def __repr__(self):
    """Provide helpful representation when printed."""
        return "<Rating rating_id={} movie_id={} user_id={} score={}>".format(self.rating_id,
                                                                           self.movie_id,
                                                                           self.user_id,

# Why is ForeignKey camel case? What is it's data type?
# What is backref?!


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///ratings'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."