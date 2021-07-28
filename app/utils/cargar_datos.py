import csv
from typing import List
class CsvtoList():

    def __init__(self, filename:str) -> None:
        self.filename = filename

    def getList(self)->List:
        data:List = []
        try:
            with open(self.filename, newline='', ) as f:
                reader = csv.DictReader(f, delimiter = ';')
                for row in reader:
                  data.append(row)

                
        except OSError as err:
            print(f"OS error: {err}" )
            raise
        except IOError as err:
            print(f"IOError: {err}")
            raise
        return data