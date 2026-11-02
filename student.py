import mysql.connector
import datetime


class STD:
    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Saneem@1212",
                database="student_db"
            )
            return self.connection
        except Exception as e:
            return None
class SBJ(STD):
    def get(self):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from details"
            self.cursor.execute(query)
            record = self.cursor.fetchall()
            print(record)
        except Exception as e:
            print(e)

    def post(self, **kwargs):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query ="insert into details(name,place,phone,subject, joining_date) values(%s, %s, %s, %s, %s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connect.commit()
            print("new member added successfully..!")
        except Exception as e:
            print(e)
    def get_object(self,id=None):
        try:
            record = self.get_object(id=id)
            if record == None:
                print("student not found..!")
            print(record)
        except Exception as e:
            print(e)

        def delete(self, id=None):
            try:
                record = self.get_object(id=id)
                values = (id,)
                if record != None:
                    query = "delete from details where id=%s"
                    self.cursor.execute(query, values)
                    self.connection.commit()
                    print("student deleted successfully..!")
                else:
                    print("student not found..!")
            except Exception as e:
                print(e)

            def put(self, id=None, **kwargs):
                try:
                    record = self.get_object(id=id)
                    if record != None:
                        self.cursor = self.connection.cursor()
                        placeholder = ""
                        for k in kwargs.keys():
                            placeholder += k + "=%s, "
                            placeholder = placeholder.rstrip(", ")
                            query = f"update details set {placeholder} where id =%s"
                            values = [v for v in kwargs.values()]
                            values.append(id)
                            self.cursor.execute(query, values)
                            self.connection.commit()
                            print("student updated successfully..!")
                    else:
                        print("member not found")
                except Exception as e:
                    print(e)