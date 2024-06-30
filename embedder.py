from sentence_transformers import SentenceTransformer
from Util.EnvironmentVariable import env

model = SentenceTransformer(
    env("EMBEDDING_MODEL_NAME"),
    cache_folder="./model"
)

def embedding(text):
    sentences = text
    if isinstance(text, str):
        sentences = [text]
    
    result = model.encode(sentences, convert_to_tensor=True)
    
    if isinstance(text, str):
        return result[0]

    return result