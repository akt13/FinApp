
import pymongo

client = pymongo.MongoClient(
        "mongodb+srv://abhijithkthoppil:abhijith123@cluster0.bsv5voc.mongodb.net/?retryWrites=true&w=majority")

def mongoCreate():
    # Specify the name of the new database
    new_database_name = "testDB"

    # Create a reference to the new database
    new_database = client[new_database_name]

    # Specify the name of the new collection
    new_collection_name = "stock_table"

    # Check if the collection already exists
    if new_collection_name not in new_database.list_collection_names():
        # Create the new collection
        new_collection = new_database[new_collection_name]
    # Insert a document into the 'users' collection
        user_data = {
            "_id": "1",
            "employee": "",
            "department" :""
        }
        new_collection.insert_one(user_data)
    else:
        new_collection = new_database[new_collection_name]
    
    # Find the maximum existing 'ID' value
    # max_id = new_collection.find_one(sort=[("_id", pymongo.DESCENDING)])

    # If the collection is empty, start with ID = 1, otherwise increment the maximum ID
    # next_id = 1 if not max_id else max_id["_id"] + 1

    # Add a field 'ID' to the documents in the collection
    # new_collection.update_many({}, {"$set": {"_id": next_id}})

    return new_collection