import os
import weaviate
from weaviate.auth import AuthApiKey

client = weaviate.connect_to_local(
    host="65.109.12.98",
    port="8006",
    auth_credentials=AuthApiKey(os.getenv("WEAVIATE_API_KEY")),
)

print(client.is_ready())
