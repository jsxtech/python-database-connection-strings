# Python Database Connection Strings

A comprehensive reference guide for connecting to 220+ databases using Python.

**Author:** Jaspal  
**Contact:** 9891156880 | jsxtech@gmail.com

## Overview

This repository contains connection string examples organized into 22 categories:

### 1. Relational Databases (SQL)
PostgreSQL, MySQL, MariaDB, SQLite, SQL Server, Oracle, IBM Db2, SAP HANA, Teradata, Vertica, Informix, Sybase/SAP ASE, Greenplum, Netezza, Exasol, MonetDB, Firebird, InterSystems IRIS, Actian Vector, Actian Zen, Altibase, Yellowbrick, NuoDB, Raima, Empress, Valentina, OpenLink Virtuoso, FileMaker, 4D

### 2. NoSQL Databases
MongoDB, Redis, Cassandra, ScyllaDB, CouchDB, Couchbase, RethinkDB, ArangoDB, OrientDB, RavenDB, Aerospike, Riak, Voldemort, Datomic, FaunaDB, SurrealDB, EdgeDB, Tarantool

### 3. Graph Databases
Neo4j, Dgraph, Amazon Neptune, Memgraph, NebulaGraph, JanusGraph, TigerGraph, Apache AGE, RedisGraph, Cayley, StarDog, AllegroGraph, Blazegraph, Apache Jena Fuseki, GraphDB, Titan, HyperGraphDB, TypeDB (Grakn), TerminusDB, FalkorDB

### 4. Key-Value Stores
Memcached, LevelDB, RocksDB, LMDB, BerkeleyDB, UnQLite, Vedis, Tokyo Cabinet, Kyoto Cabinet, WhiteDB, FoundationDB, Hazelcast, Apache Geode, GridDB, Apache Ignite

### 5. Vector Databases
Pinecone, Weaviate, Milvus, Qdrant, Chroma, pgvector, Vespa, LanceDB, Marqo

### 6. Time-Series Databases
InfluxDB, TimescaleDB, TDengine, QuestDB, Amazon Timestream

### 7. Search & Analytics Engines
Elasticsearch, Apache Solr

### 8. Columnar & Analytical Databases
ClickHouse, Apache Druid, Apache Pinot, Apache Kudu, Kdb+

### 9. Big Data & Data Warehouses
Apache Hive, Apache Impala, Trino, Presto (legacy), Apache Drill, Apache HBase, Apache Phoenix, Apache Accumulo, Snowflake, Databricks, Dremio, Splice Machine

> Note: Rockset has been discontinued (acquired by OpenAI, 2024)

### 10. Cloud Databases - AWS
Amazon RDS (PostgreSQL/MySQL), Amazon Aurora (PostgreSQL/MySQL), Amazon Redshift, Amazon DynamoDB, Amazon DocumentDB

### 11. Cloud Databases - Azure
Azure SQL Database, Azure Cosmos DB

### 12. Cloud Databases - Google Cloud
Google Cloud SQL (PostgreSQL/MySQL), Google BigQuery, Google Firestore

### 13. Managed Database Services
Supabase, PlanetScale, Neon, CockroachDB, YugabyteDB, TiDB, SingleStore, Vitess, CrateDB, MatrixOne, OceanBase, OpenGauss, Databend

### 14. Embedded Databases
H2, Apache Derby, HSQLDB, Realm, ObjectBox, ITTIA DB

### 15. XML Databases
MarkLogic, BaseX, eXist-db, Sedna, Tamino

### 16. Object Databases
Objectivity/DB, Versant, GemStone/S

### 17. Mainframe & Legacy Databases
Adabas, Model 204, IDMS, IMS, DATACOM, GT.M, Caché, Mnesia

### 18. Specialized & Other Databases
VoltDB, Clustrix, Sadas, Polyglot, Ehcache, Infinispan, Coherence, GemFire, Redis-Compatible (Dragonfly, KeyDB, Garnet, Redict, Valkey), Skytable, DuckDB, Polars, Firebolt, Hydrolix, Tinybird, MotherDuck, Turso, Xata, Convex

### 19. Data Formats & File-Based
TileDB, Zarr, HDF5, Parquet, ORC, Avro, Feather, Arrow

### 20. Message & Event Stores
Apache Kafka, Apache Pulsar, RabbitMQ, NATS, EventStoreDB, Pravega

### 21. Cloud-Native & Serverless
Upstash Redis, Momento, Aerospike Cloud, Astra DB, MongoDB Atlas, Redis Cloud, ElastiCache, MemoryDB, Azure Cache for Redis, Google Cloud Memorystore, Cloudflare D1/KV/Durable Objects, Vercel Postgres/KV, Railway, Render, Fly.io

### 22. SQLAlchemy (Universal ORM)
Connection strings for PostgreSQL, MySQL, SQLite, SQL Server, Oracle

## Usage

The `db_connections.py` file is a **reference guide only** - not meant to be executed as-is. Copy the relevant connection code for your specific database.

## Important Notes

- Replace placeholder credentials (`user`, `password`, `localhost`) with actual values
- Use environment variables for sensitive credentials in production
- Install required Python packages before use (see installation examples below)
- Variable names (`conn`, `client`, `db`) are reused throughout - use unique names in your code
- Add proper error handling and connection closing in production code
- Some packages may require additional system dependencies or JDBC drivers

## Installation Examples

```bash
# Relational Databases
pip install psycopg2-binary          # PostgreSQL
pip install mysql-connector-python   # MySQL
pip install mariadb                  # MariaDB
pip install pyodbc                   # SQL Server (requires ODBC drivers)
pip install oracledb                 # Oracle (successor to cx_Oracle)
pip install ibm_db                   # IBM Db2
pip install teradatasql              # Teradata

# NoSQL Databases
pip install pymongo                  # MongoDB
pip install redis                    # Redis
pip install cassandra-driver         # Cassandra, ScyllaDB
pip install couchdb                  # CouchDB
pip install rethinkdb                # RethinkDB
pip install edgedb                   # EdgeDB

# Graph Databases
pip install neo4j                    # Neo4j
pip install pydgraph                 # Dgraph
pip install FalkorDB                 # FalkorDB (RedisGraph successor)

# Vector Databases
pip install pinecone                 # Pinecone (v3+)
pip install weaviate-client          # Weaviate
pip install pymilvus                 # Milvus
pip install qdrant-client            # Qdrant
pip install chromadb                 # Chroma

# Time-Series
pip install influxdb-client          # InfluxDB
pip install taos                     # TDengine

# Big Data
pip install pyhive                   # Hive
pip install trino                    # Trino (formerly Presto)
pip install impyla                   # Impala
pip install happybase                # HBase

# Cloud
pip install boto3                    # AWS services
pip install google-cloud-bigquery    # Google BigQuery
pip install google-cloud-firestore   # Google Firestore

# Universal ORM
pip install sqlalchemy               # SQLAlchemy

# Managed Services
pip install crate                    # CrateDB

# Key-Value Stores
pip install plyvel                   # LevelDB
pip install rocksdict                # RocksDB (maintained; replaces unmaintained python-rocksdb)
pip install lmdb                     # LMDB
pip install berkeleydb               # BerkeleyDB (replaces deprecated bsddb3, Python 3.6+)

# Analytical & Embedded
pip install duckdb                   # DuckDB
pip install snowflake-connector-python  # Snowflake
pip install databricks-sql-connector # Databricks
```

## Example Usage

```python
import psycopg2
from contextlib import closing
import os

# Use environment variables for credentials
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'mydb')
DB_USER = os.getenv('DB_USER', 'user')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')

# Use context manager for proper connection handling
try:
    with closing(psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT version();")
            print(cur.fetchone())
except psycopg2.Error as e:
    print(f"Database error: {e}")
```

## File Structure

```
db_connections.py    # Main reference file with all connection strings organized by category
README.md           # This file
```

## Contributing

Feel free to submit PRs for:
- Additional databases
- Corrections or improvements
- Better examples
- Missing installation instructions

## License

MIT
