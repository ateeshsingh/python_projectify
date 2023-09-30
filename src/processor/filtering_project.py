from typing import Dict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils.database_functions import DbFunctions
from ..administrator.app import gallery_app


project_documents = DbFunctions.find_all(database=gallery_app.db, collection_name="PROJECT_GALLERY", projection={"_id": 0},
                                 query={})


def pre_processor(data: Dict):
    idx = data.get('Project').get('Title') + "/"
    st1 = f"project title {data.get('Project').get('Title')} technologies used {data.get('Project').get('Technologies')}"
    st2 = f"technical skill set frontend {data.get('Technical_Skillset').get('Frontend')}"
    st3 = f"technical skill set backend {data.get('Technical_Skillset').get('Backend')}"
    st4 = f"technical skill set frontend {data.get('Technical_Skillset').get('Databases')}"
    st5 = f"availability {data.get('Other_Information').get('Availability')}"
    return idx+st1 + st2 + st3 + st4 + st5


documents = [pre_processor(rec) for rec in project_documents]


# Preprocess and vectorize the documents


def search(query):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    # Preprocess the user query and vectorize it
    query_vector = vectorizer.transform([query])

    # Calculate cosine similarity between the query and documents
    similarity_scores = cosine_similarity(query_vector, tfidf_matrix)

    # Rank the documents by similarity score
    ranked_documents = [(score,doc.split("/")[0]) for score, doc in zip(similarity_scores[0], documents) if score >0.5*max(similarity_scores[0])]

    # Sort documents by similarity score (higher score means more similar)
    ranked_documents.sort(reverse=True, key=lambda x: x[0])

    return ranked_documents


def filter_project(user_query: str):
    if not user_query:
        return project_documents
    filtered_data=[]
    search_results = search(user_query)
    for _,i in search_results:
        for j in project_documents:
            if i==j.get('Project').get('Title'):
                j.update({"score":_})
                filtered_data.append(j)
    return filtered_data
