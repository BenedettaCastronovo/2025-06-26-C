from database.DB_connect import DBConnect


class DAO():
    @staticmethod
    def getAllConstructors():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * 
                    from constructors"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row)

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getY():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        anni = []
        query= """                    
             select distinct `year` 
             from seasons 
             order by `year`
            """
        cursor.execute(query)
        for row in cursor:
            anni.append(row["year"])

        cursor.close()
        cnx.close()

        return anni
