from flask import jsonify, request, g
import logging
from config.exceptions import *
import uuid

def register_error_handlers(app):

    logger = logging.getLogger(__name__)
    
    ERR_MSG = {
        'VALIDATION_ERROR': 'Error en validación',
    }

    def create_response(standarStatusForResponse, statusCode, originalError=None, customError=None, moreInformationError= None):
        response_obj = {
            'status': 'error',
            'message': standarStatusForResponse,
            'error': originalError,
            'comment': customError,
            'moreInformationError': moreInformationError,
            'uidError': g.uidRequest
        }
        return jsonify(response_obj), statusCode
    
    @app.errorhandler(ValidationException)
    def handle_error1(e: ValidationException):
        return create_response(ERR_MSG['VALIDATION_ERROR'], 400,  e.originalError, e.myCustomError, e.whatProcessAndMoreInformactionAboutTheError)
