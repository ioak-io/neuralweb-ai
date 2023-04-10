from flask import Blueprint, jsonify, request
import app.main.service.similarity_service as similarity_service

similarity_controller = Blueprint('similarity_controller', __name__)


@similarity_controller.route('/train', methods=['GET'])
def hello(space):
    return similarity_service.hello(space)
