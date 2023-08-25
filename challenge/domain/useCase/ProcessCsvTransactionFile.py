from services.Csv import Csv
from services.TransactionService import TransactionService
from services.email.EmailService import EmailService
from services.PrepareSummary import PrepareSummary

class ProcessCsvTransactionFile():

    def __init__(self, csv:Csv = Csv(), transactionService: TransactionService = TransactionService(), 
                 emailService: EmailService = EmailService(),
                 prepareSummary: PrepareSummary = PrepareSummary()):
        self.csv:Csv = csv
        self.transactionService = transactionService
        self.emailService = emailService
        self.prepareSummary = prepareSummary

    def save_transaction_in_db_and_send_to_user_extract_resume(self, request):

        file = request.files['transactionFile']
        email = request.args.get('email')

        # Csv list to object python
        dictListOfTranssaction: list = self.csv.csv_to_list_of_dicts(file)

        # Save the transacction to postgress db
        self.transactionService.save_transaction(dictListOfTranssaction)

        # Prepare summary
        summary = self.prepareSummary.prepare(dictListOfTranssaction)

        # Send Summary email
        self.emailService.send_account_summary("ACCOUNT SUMMARY", [email], summary, file)

        # Give to user notification of what happend. 
        return {"message": "se le a enviado un correo a "+email, "summary": summary}