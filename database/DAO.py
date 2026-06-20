from database.DB_connect import DBConnect
from model.arco import Arco
from model.costruttore import Costruttore
from model.piazzamento import Piazzamento


class DAO():
    @staticmethod
    def getAll():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * 
                    from constructors"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Costruttore(**row))

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

    @staticmethod
    def getP(c, min, max):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        piaz = {}
        query = """select ra.`year` as y, r.driverId as id, r.`position` as p
                    from results r, races ra
                    where r.raceId = ra.raceId and r.constructorId = %s and (ra.`year` between %s and %s)  and r.`position` is not null
                    group by y, id, p
                    order by r.`position` """
        cursor.execute(query, (c, min, max))
        for row in cursor:
            if row["y"] in piaz:
                piaz[row["y"]].append(Piazzamento(row["id"], row["p"]))
            else:
                piaz[row["y"]] = [Piazzamento(row["id"], row["p"])]

        cursor.close()
        cnx.close()
        return piaz

    @staticmethod
    def getA(mappa, min, max):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        archi = []
        query= """select c1.constructorid as c1, c2.constructorid as c2, (c1.cnt + c2.cnt) as peso
                    from(select r.constructorId, count( *) as cnt
                    from races ra, results r
                    where ra.year >= %s and ra.year <= %s and ra.raceId = r.raceId and r.`position` is not null
                    group by r.constructorId ) c1, 
                    (select r.constructorId , count(*) as cnt
                    from races ra, results r
                    where ra.year >= %s and ra.year <= %s and ra.raceId = r.raceId and r.`position` is not null
                    group by r.constructorId 
                    ) c2
                    where c1.constructorid < c2.constructorid 
					group by c1.constructorid , c2.constructorid """

        cursor.execute(query, (min, max, min, max))
        for row in cursor:
            archi.append(Arco(mappa[row["c1"]], mappa[row["c2"]], row["peso"]))
        cursor.close()
        cnx.close()
        return archi

