from pymongo import MongoClient

def run_explorer():
    client = MongoClient("mongodb://localhost:27017/")

    while True:
        # --- DATABASES ---
        db_names = client.list_database_names()
        
        if not db_names:
            print("No Database")
            input("\nPress any button to return")
            continue

        print("\nDatabases")
        for db in db_names:
            print(f" - {db}")
        
        while True:
            selected_db = input("\nSelect Database: ")
            if selected_db in db_names:
                break
            print("Datenbank nicht vorhanden. Bitte erneut wählen.")

        db = client[selected_db]

        # --- COLLECTIONS ---
        print(f"\n{selected_db}\n")
        col_names = db.list_collection_names()
        
        if not col_names:
            print("No Collection")
            input("\nPress any button to return")
            continue
        
        print("Collections")
        for col in col_names:
            print(f" - {col}")
            
        while True:
            selected_col = input("\nSelect Collection: ")
            if selected_col in col_names:
                break
            print("Collection nicht vorhanden. Bitte erneut wählen.")
            
        collection = db[selected_col]

        # --- DOCUMENTS ---
        print(f"\n{selected_db}.{selected_col}\n")
        documents = list(collection.find())
        
        if not documents:
            print("No Document")
            input("\nPress any button to return")
            continue
        
        print("Documents")
        # Speichere die Dokumente in einem Dictionary mit der ID als String als Key
        doc_map = {}
        for doc in documents:
            doc_id_str = str(doc['_id'])
            doc_map[doc_id_str] = doc
            print(f" - {doc_id_str}")
            
        while True:
            selected_doc_id = input("\nSelect Document: ")
            if selected_doc_id in doc_map:
                selected_doc = doc_map[selected_doc_id]
                break
            print("Document nicht vorhanden. Bitte erneut wählen.")

        # --- DOCUMENT CONTENT ---
        print(f"\n{selected_db}.{selected_col}.{selected_doc_id}\n")
        
        for key, value in selected_doc.items():
            if key != '_id': # _id wird weggelassen, da sie bereits im Header steht
                print(f"{key}: {value}")
        
        input("\nPress any button to return")

if __name__ == "__main__":
    run_explorer()