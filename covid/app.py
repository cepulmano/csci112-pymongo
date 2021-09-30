import db_crud as crud
from pymongo import MongoClient
from pprint import pprint

if __name__ == '__main__':
    client = MongoClient('172.31.88.83', 27017)
    print(crud.get_collections(client, "sample"))
    
    # Find all students have an exam grade higher than 75
    students = crud.get_students_by_grade(client, "sample", 75)
