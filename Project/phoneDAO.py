import mysql.connector.authentication

#import mysql.connector.authentication
class PhoneDAO:
    db = ""

    def __init__(self):

        self.db = mysql.connector.connect(

            host="localhost",

            user="root",

            password="12345",

            # user="datarep",  # this is the user name on my mac

            # passwd="password" # for my mac

            database="datarepresentation"

        )

    def create(self, values):
        cursor = self.db.cursor()
        sql = "insert into phone (make, model, price) values (%s,%s,%s)"
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = "select * from phone"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql = "select * from phone where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        sql = "update phone set make= %s,model=%s, price=%s  where id = %s"
        cursor.execute(sql, values)
        self.db.commit()

    def delete(self, id):
        cursor = self.db.cursor()
        sql = "delete from phone where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.db.commit()
        print("delete done")

    def convertToDictionary(self, result):
        colnames = ['id', 'Make', 'Model', "Price"]
        item = {}

        if result:

            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value

        return item

phoneDAO = PhoneDAO()