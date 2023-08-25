from config.db import get_db_session

class TransactionRepository():

    def __init__(self) -> None:
        pass

    def save_transactions(self, transactionModelList) :
        try:
            session = get_db_session()
            session.add_all(transactionModelList)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()



            
 