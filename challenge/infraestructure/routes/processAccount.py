from flask_restx import Namespace, Resource
from flask import request
from domain.useCase.ProcessCsvTransactionFile import ProcessCsvTransactionFile
from domain.validations.ValidationRequest import ValidationRequest

api = Namespace('api', description='demo route')

@api.route('/transactions')
class Login(Resource):

    api = api
    def __init__(self, restx_placeholder_param=None, useCase:ProcessCsvTransactionFile = ProcessCsvTransactionFile(),
                validation: ValidationRequest = ValidationRequest(),
        ):
        self.useCase:ProcessCsvTransactionFile = useCase
        self.validation: ValidationRequest = validation
        super().__init__(self.api)

    def post(self):

        # Primer paso siempre validar el input recibido.
        self.validation.validate(request)

        # Ejecuto el caso de uso en cuestion, todo lo que hara la tarea
        result = self.useCase.save_transaction_in_db_and_send_to_user_extract_resume(request)
        
        # Envio respuesta del caso de uso.
        return result,200
  
