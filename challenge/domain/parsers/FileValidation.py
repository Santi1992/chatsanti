from config.exceptions import ValidationException
from werkzeug.utils import secure_filename

class FileValidation ():

    def __init__(self) -> None:
        pass

    def validate_file_and_return_secure_name(self, fileBytes, fileName,height, requiredExtension):
        if fileName == '':
            ValidationException("Debe enviar un nombre en el file")
        filename = secure_filename(fileName)
        if fileName.lower().endswith(requiredExtension) == False:
            raise ValidationException("La extensión del archivo no es la solicitada")
        max_file_size = height * 1024 * 1024  # MB
        tamano_mb = len(fileBytes) / 1048576.0 
        print("El tamañao del archivo es de ", tamano_mb, " mb")
        if tamano_mb > max_file_size:
            raise ValidationException("El archivo excede los 5mb permitidos")
        return filename