import os
import json
from pymongo import MongoClient
from datetime import datetime

def convert_datetime_fields(doc, datetime_fields, dt_format="%Y-%m-%dT%H:%M:%S"):
    """Recursively convert specified fields to datetime if found in doc."""
    if isinstance(doc, dict):
        for key, value in doc.items():
            if key in datetime_fields and isinstance(value, str):
                try:
                    doc[key] = datetime.strptime(value, dt_format)
                except Exception:
                    pass  # leave as string if parsing fails
            else:
                convert_datetime_fields(value, datetime_fields, dt_format)
    elif isinstance(doc, list):
        for item in doc:
            convert_datetime_fields(item, datetime_fields, dt_format)
    return doc

def import_json_to_mongodb(json_dir, mongo_host="localhost", mongo_port=27017, datetime_fields=None, dt_format="%Y-%m-%dT%H:%M:%S"):
    client = MongoClient(host=mongo_host, port=mongo_port)

    for filename in os.listdir(json_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(json_dir, filename)
            
            db_name, coll_name = filename[:-5].split('_')
            collection = client[db_name][coll_name]
            
            print(f"Importing {file_path} into {db_name}.{coll_name} ...")
            
            with open(file_path, 'r') as f:
                data = json.load(f)

                if datetime_fields:
                    data = convert_datetime_fields(data, datetime_fields, dt_format)

                if isinstance(data, list):
                    collection.insert_many(data)
                else:
                    collection.insert_one(data)
    
    print("✅ Import complete.")

if __name__ == "__main__":
    json_import_directory = "mongo_dump_json" 
    mongo_host = "localhost"
    mongo_port = 27017

    # Fields you want as datetime
    datetime_fields = ["transactionDate"]

    # Matches "2021-12-28T00:00:00"
    dt_format = "%Y-%m-%dT%H:%M:%S"

    import_json_to_mongodb(json_import_directory, mongo_host, mongo_port, datetime_fields, dt_format)
