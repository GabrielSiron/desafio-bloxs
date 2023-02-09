class DataBaseConnection:

    @staticmethod
    def select_one(_class, comparator_object):
        from sqlalchemy.sql import select
        from sqlalchemy import create_engine
    
        engine = create_engine('mysql+pymysql://gabriel:143867@0.0.0.0:3306/mysql')
        expression = select(_class).filter_by(**comparator_object)
        conn = engine.connect()
        result = conn.execute(expression)

        return result.fetchone()
    
    @staticmethod
    def select_many(_class, comparator_object):
        from sqlalchemy.sql import select
        from sqlalchemy import create_engine
    
        engine = create_engine('mysql+pymysql://gabriel:143867@0.0.0.0:3306/mysql')
        expression = select(_class).filter_by(**comparator_object)
        conn = engine.connect()
        result = conn.execute(expression)

        return result.fetchall()