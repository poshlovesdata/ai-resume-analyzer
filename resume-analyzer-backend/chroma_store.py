import chromadb
import json
from pprint import pprint

chroma_client = chromadb.PersistentClient('./chroma_db')

collection = chroma_client.get_or_create_collection(name="resources-base")

def seed_vectordb():
    """Reads resources.json and loads it into Chroma if empty."""
    if collection.count() > 0:
        print(f"Knocwledge Base loaded. Contains {collection.count()} resources.") 
        return
    else:
        print("Seeding VectorDB...")
        try:
            with open("resources.json", "r") as f:
                data = json.load(f)
                documents = []
                metadatas = []
                ids = []
                
                for item in data:
                    # ID variable
                    ids.append(item['id'])
                    
                    searchable_text = (
                        f"{item['title']}. "
                        f"{item['description']}. "
                        f"Skill: {item['skill']}. "
                        f"Tags: {', '.join(item['tags'])}. "
                    )
                    documents.append(searchable_text)
                    
                    meta = {
                        "title": item["title"],
                        "url": item["url"],
                        "level": item["level"],
                        "provider": item["provider"],
                        "estimated_hours": item["estimated_hours"],
                        "prerequisites": ", ".join(item.get("prerequisites", [])) # Handle list
                    }
                    
                    metadatas.append(meta)
                    
                collection.add(
                    documents=documents,
                    metadatas=metadatas,
                    ids=ids
                )
            print(f"Loaded {len(ids)}  resources.")
        except FileNotFoundError:
            print("Error: resources.json not found. Database is empty.")

def query_resources(query_text: str, n_number: int = 2):  
    results = collection.query(query_texts=query_text, n_results=n_number)
    
    found_resources = []
    
    if results['metadatas'] and results['metadatas'][0]:
        # Return the metadata (Title, URL, etc.) instead of just the text
        for meta in results['metadatas'][0]:
            found_resources.append(meta)
    return found_resources


seed_vectordb()
            