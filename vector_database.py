from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection, utility
from Util.EnvironmentVariable import env
from embedder import embedding

param = {
    'metric_type': "COSINE",
    'index_type': "IVF_FLAT",
    'params': {
        "nlist": int(env('EMBEDDING_DIMENSION'))
    }
}
connections.connect(host="127.0.0.1", port="19530")

# 아래 두 줄을 활성화하면 코드를 실행할 때마다 데이터베이스가 초기화됩니다.
for collection_name in ["test"]:
    if utility.has_collection(collection_name): utility.drop_collection(collection_name)

collection = Collection(
    name="test",
    schema=CollectionSchema(
        fields=[
            FieldSchema(name='id', dtype=DataType.INT64, is_primary=True, auto_id=True),
            FieldSchema(name='file_id', dtype=DataType.VARCHAR, max_length=64),
            FieldSchema(name='embedding', dtype=DataType.FLOAT_VECTOR, dim=int(env('EMBEDDING_DIMENSION')))
        ]
    ),
)

collection.create_index(
    field_name="embedding",
    index_params=param
)
collection.load()

async def insert_data(file_id, func, args):
    embedded_vector = await func(*args)

    collection.insert({
        "file_id": file_id,
        "embedding": embedded_vector
    })

    collection.flush()
    return

async def retrieval(text):
    embedded_vector = embedding(text)

    result = collection.search(
        data=[embedded_vector.tolist()],
        anns_field="embedding",
        param=param,
        limit=3,
        output_fields=["file_id"]
    )

    ret = []

    for hits in result:
        for hit in hits:
            temp = hit.to_dict()["entity"]
            ret.append(temp["file_id"])
    
    return ret