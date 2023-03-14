from django.http import JsonResponse
import pymongo

# client = MongoClient()


def get_results(id_list):
    client = pymongo.MongoClient("mongodb+srv://zhou:0219@cluster0.kwwqk4a.mongodb.net/?retryWrites=true&w=majority")
    db =client['ttds']
    collection = db['books']

    # retrieve documents with matching ids
    cursor = collection.find({'_id': {'$in': id_list}})

     # create dictionary where keys are ids and values are documents
    data_dict = {doc['_id']: doc for doc in cursor}

    # create list of documents in the order of input ids
    data = [data_dict[id] for id in id_list]

    # convert cursor to list of dictionaries
    # data = list(data)
    return data

    




