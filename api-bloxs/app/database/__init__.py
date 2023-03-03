class DataBaseConnection:

    @staticmethod
    def select_one(_class, comparator_object):
        from sqlalchemy.sql import select
        from sqlalchemy import create_engine
    
        engine = create_engine('mysql+pymysql://root:password@localhost:3306/desafio')
        expression = select(_class).filter_by(**comparator_object)
        conn = engine.connect()
        result = conn.execute(expression)

        return result.fetchone()
    
    @staticmethod
    def select_many(_class, comparator_object):
        from sqlalchemy.sql import select
        from sqlalchemy import create_engine
    
        engine = create_engine('mysql+pymysql://root:password@localhost:3306/desafio')
        expression = select(_class).filter_by(**comparator_object)
        conn = engine.connect()
        result = conn.execute(expression)

        return result.fetchall()

    def select_transactions(page, account_id):
        from app.models.transaction import Transaction
        from sqlalchemy.sql import select
        from sqlalchemy import create_engine, or_
        from sqlalchemy import desc 
        
        engine = create_engine('mysql+pymysql://root:password@localhost:3306/desafio')
        expression = select(Transaction).filter(or_(
                        Transaction.transfer_sender_id == account_id, 
                        Transaction.transfer_receiver_id == account_id,         
                        )).order_by(desc(Transaction.id)).limit(10*page)

        conn = engine.connect()
        result = conn.execute(expression)

        return result.fetchall()


    def select_transactions_of_today(account_id):
        from app.models.transaction import Transaction
        from sqlalchemy.sql import select
        from sqlalchemy import create_engine, and_
        from sqlalchemy import desc 
        from datetime import datetime

        date, _ = str(datetime.now()).split()

        min_date = date + "T00:00:00"
        max_date = date + 'T23:59:59'

        engine = create_engine('mysql+pymysql://root:password@localhost:3306/desafio')
        expression = select(Transaction).filter(
            and_(
                Transaction.transaction_date >= min_date, 
                Transaction.transaction_date <= max_date, 
            )
        ).filter(Transaction.transfer_sender_id == account_id).order_by(desc(Transaction.id))

        conn = engine.connect()
        result = conn.execute(expression)

        return result.fetchall()