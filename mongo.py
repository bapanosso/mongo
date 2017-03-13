from pymongo import MongoClient

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
DOCUMENT_NAME = 'test'
COLLECTION_NAME = 'service'



if __name__ == "__main__":

    dados = [{'Nome': 'Barbara', 'Idade': '26', 'Sexo': 'Feminino'}, {'Nome': 'Barbara', 'Idade': '26', 'Sexo': 'Feminino'},
    {'Nome': 'Barbara', 'Idade': '26', 'Sexo': 'Feminino'}, {'Nome': 'Barbara', 'Idade': '26', 'Sexo': 'Feminino'}]
    client = MongoClient(MONGO_HOST, MONGO_PORT)
    db = client[DOCUMENT_NAME]
    collection = db[COLLECTION_NAME]
    for dado in dados:
        collection.insert(dado)
        results = collection.find()
        print()
        print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-')

    # display documents from collection
    for record in results:
        print(record['Nome'] + ',',record['Sexo'] + ',',record['Idade'])
