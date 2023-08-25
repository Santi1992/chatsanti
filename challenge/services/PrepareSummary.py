class PrepareSummary():

    def __init__(self) -> None:
        pass


    def prepare(self, dictListOfTransactions):
        debit_transactions = [transaction for transaction in dictListOfTransactions if float(transaction['ammount']) < 0]
        credit_transactions = [transaction  for transaction in dictListOfTransactions if float(transaction['ammount']) >= 0]
        total_balance = sum(float(transaction['ammount']) for transaction in dictListOfTransactions)
        average_debit_amount = sum(float(transaction['ammount']) for transaction in debit_transactions) / len(debit_transactions)
        average_credit_amount = sum(float(transaction['ammount']) for transaction in credit_transactions) / len(credit_transactions)

        # Debería existir una lógica, filtro de meses requeridos.
        julyTransactions = sum(1 for transaction in dictListOfTransactions if transaction['date'][5:7] == '07')
        augustTransactions = sum(1 for transaction in dictListOfTransactions if transaction['date'][5:7] == '08')
        septemberTransactions = sum(1 for transaction in dictListOfTransactions if transaction['date'][5:7] == '09')
        octuberTransactions = sum(1 for transaction in dictListOfTransactions if transaction['date'][5:7] == '10')

        result = {
        'total_balance': total_balance,
        'average_debit_amount': average_debit_amount,
        'average_credit_amount': average_credit_amount,
        'total_july_transactions': julyTransactions,
        'total_august_transactions': augustTransactions,
        'total_september_transactions': septemberTransactions,
        'total_octuber_transactions': octuberTransactions,
    }
    
        return result