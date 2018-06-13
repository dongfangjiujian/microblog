import os
basedir = os.path.abspath(os.path.dirname(__file__))
print("basedir : "+basedir)\

class Config:

    @staticmethod
    def init_app(app):
        pass