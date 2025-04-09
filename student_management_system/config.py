import os

class Config:
    # Application configuration
    SECRET_KEY = 'dev'  # Development key, production should use a complex random key
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Application basic information
    APP_NAME = "Student Management System"
    
    # Pagination settings
    ITEMS_PER_PAGE = 10