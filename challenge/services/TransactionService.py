from infraestructure.repository.TransactionRepository import TransactionRepository
from infraestructure.repository.models.baseModels import Transaction

class TransactionService():

    def __init__(self, transactionRepository: TransactionRepository = TransactionRepository()) -> None:
        self.transactionRepository = transactionRepository

    def save_transaction(self, dictListOfTransacction):
        transactionsDtoList = self._build_list_of_transaction_dto(dictListOfTransacction)
        self.transactionRepository.save_transactions(transactionsDtoList)
    

    def _build_list_of_transaction_dto(self, dictList):
        transactionDtoList= []
        for i in dictList:
            transactionDtoList.append(Transaction(user_id=i["idUser"], ammount=i["ammount"], date_transaction=i["date"],))
        
        return transactionDtoList
