# test_connections.py
# Pruebas mínimas de conexión a Neo4j, MongoDB y Redis desde Python dentro del contenedor.
import os, time

NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "neo4j123")
MONGO_USER = os.getenv("MONGO_INITDB_ROOT_USERNAME", "admin")
MONGO_PASS = os.getenv("MONGO_INITDB_ROOT_PASSWORD", "admin123")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "redis123")

print("Esperando servicios (5s)...")
time.sleep(5)

# ---- Neo4j ----
from neo4j import GraphDatabase
neo4j_uri = "bolt://neo4j:7687"
driver = GraphDatabase.driver(neo4j_uri, auth=("neo4j", NEO4J_PASSWORD))
with driver.session() as s:
    s.run("CREATE (:City {name:$name})", name="La Plata")
    count = s.run("MATCH (n:City) RETURN count(n) AS c").single()["c"]
    print(f"[Neo4j] nodos City: {count}")
driver.close()

# ---- MongoDB ----
from pymongo import MongoClient
mongo_uri = f"mongodb://{MONGO_USER}:{MONGO_PASS}@mongo:27017/"
client = MongoClient(mongo_uri)
db = client["clase"]
db.alumnos.insert_one({"nombre":"Edu","tema":"Grafos"})
print(f"[MongoDB] alumnos: {db.alumnos.count_documents({})}")
client.close()

# ---- Redis ----
import redis
r = redis.Redis(host="redis", port=6379, password=REDIS_PASSWORD, decode_responses=True)
r.set("saludo","hola")
print(f"[Redis] saludo = {r.get('saludo')}")
