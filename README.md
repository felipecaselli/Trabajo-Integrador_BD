# 🧪 Classroom Stack: Python + Neo4j + MongoDB + Redis (Docker)

Este stack está pensado para levantar **Neo4j**, **MongoDB**, **Redis** y un contenedor de **Python + JupyterLab**
con todas las librerías necesarias preinstaladas.

## 🚀 Requisitos
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Windows/Mac) o Docker Engine (Linux)
- `docker compose` (v2+)

> En Windows, si usás WSL2, asegurate de que Docker Desktop tenga activado el backend WSL.

## 🧩 Servicios
- **python**: JupyterLab en `http://localhost:8888` (sin token), con `neo4j`, `pymongo` y `redis` ya instalados.
- **neo4j**: Browser en `http://localhost:7474`, Bolt en `bolt://localhost:7687`.
- **mongo**: Servidor en `mongodb://<user>:<pass>@localhost:27017/`.
- **redis**: Servidor en `redis://:<password>@localhost:6379`.

## 🔒 Credenciales (editar en `.env` o usar `.env.example`)
```
NEO4J_PASSWORD=neo4j123
MONGO_INITDB_ROOT_USERNAME=admin
MONGO_INITDB_ROOT_PASSWORD=admin123
REDIS_PASSWORD=redis123
```

> Para empezar rápido: copiá `.env.example` a `.env` sin cambios:
> ```bash
> cp .env.example .env
> ```

## ▶️ Levantar el entorno
```bash
docker compose up --build
```
La primera vez tarda un poco (descarga imágenes e instala dependencias).

## ⏹️ Apagar y borrar contenedores
```bash
docker compose down
```
Para borrar volúmenes (datos persistentes), agregá `-v`:
```bash
docker compose down -v
```

## 📒 JupyterLab
Abrí `http://localhost:8888`. Vas a encontrar ejemplos:
- `notebooks/test_connections.ipynb` (o el script `test_connections.py`)

## 🧪 Pruebas rápidas desde Python
Dentro de JupyterLab:
```python
# Neo4j
from neo4j import GraphDatabase
driver = GraphDatabase.driver("bolt://neo4j:7687", auth=("neo4j", "neo4j123"))
with driver.session() as s:
    s.run("CREATE (:City {name:'La Plata'})")
    print(s.run("MATCH (n:City) RETURN count(n) AS c").single()["c"])

# MongoDB
from pymongo import MongoClient
client = MongoClient("mongodb://admin:admin123@mongo:27017/")
db = client["clase"]
db.alumnos.insert_one({"nombre":"Edu","tema":"Grafos"})
print(db.alumnos.count_documents({}))

# Redis
import redis
r = redis.Redis(host="redis", port=6379, password="redis123", decode_responses=True)
r.set("saludo","hola")
print(r.get("saludo"))
```

## Tips
- Si `7474`/`7687`/`27017`/`6379`/`8888` están ocupados, cambiá los puertos publicados en `docker-compose.yml`.
- Los datos **persisten** en los volúmenes docker (`neo4j_data`, `mongo_data`); para empezar limpio, hacé `docker compose down -v`.
