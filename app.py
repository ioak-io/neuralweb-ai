from flask import Flask

from src.main.controller.similarity_controller import similarity_controller

app = Flask(__name__)
app.register_blueprint(similarity_controller, url_prefix='/api/similarity/<space>')

@app.route('/')
def index():
    return 'Hello, World!'
