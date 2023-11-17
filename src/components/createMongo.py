
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
            "_id" : "1",
            "Stock": "",
            "Symbol": "",
            "Quantity": "",
            "Avg_Price" :"",
            "LTP" : ""
        }
        new_collection.insert_one(user_data)
    else:
        new_collection = new_database[new_collection_name]

    return new_collection