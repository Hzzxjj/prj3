import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration from environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.environ.get('DB_USERNAME', 'postgres')}:{os.environ.get('DB_PASSWORD', 'mypassword')}@{os.environ.get('DB_HOST', 'postgresql-service')}:{os.environ.get('DB_PORT', '5432')}/{os.environ.get('DB_NAME', 'postgres')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configure logging
logging.basicConfig(level=logging.INFO)
app.logger.info("Flask application configured")

db = SQLAlchemy(app)

# Database models
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    joined_at = db.Column(db.DateTime, nullable=False)
    
    def __repr__(self):
        return f'<User {self.id}>'


class Token(db.Model):
    __tablename__ = 'tokens'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    used_at = db.Column(db.DateTime, nullable=True)
    
    def __repr__(self):
        return f'<Token {self.id}>'