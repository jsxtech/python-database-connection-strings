"""
Python Database Connection Strings - Reference Guide
Author: Jaspal | Contact: 9891156880 | jsxtech@gmail.com

IMPORTANT: This is a reference guide only - not meant to be executed as-is.
Copy the relevant connection code for your specific database.

Note: Variable names (conn, client, db) are reused throughout.
Use unique names in your actual code.
"""

# ============================================================================
# RELATIONAL DATABASES (SQL)
# ============================================================================

# --- PostgreSQL ---
import psycopg2
conn = psycopg2.connect("postgresql://user:password@localhost:5432/dbname")
conn = psycopg2.connect(host="localhost", database="dbname", user="user", password="password", port=5432)

# --- MySQL ---
import mysql.connector
conn = mysql.connector.connect(host="localhost", user="user", password="password", database="dbname", port=3306)

# --- MariaDB ---
import mariadb
conn = mariadb.connect(host="localhost", user="user", password="password", database="dbname", port=3306)

# --- SQLite ---
import sqlite3
conn = sqlite3.connect("database.db")
conn = sqlite3.connect(":memory:")  # In-memory database

# --- SQL Server ---
import pyodbc
conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=dbname;UID=user;PWD=password")
conn = pyodbc.connect("DRIVER={SQL Server};SERVER=localhost;DATABASE=dbname;Trusted_Connection=yes")  # Windows Auth

# --- Oracle ---
import cx_Oracle
conn = cx_Oracle.connect("user/password@localhost:1521/service_name")

# --- IBM Db2 ---
import ibm_db
conn = ibm_db.connect("DATABASE=dbname;HOSTNAME=localhost;PORT=50000;PROTOCOL=TCPIP;UID=user;PWD=password;", "", "")

# --- SAP HANA ---
from hdbcli import dbapi
conn = dbapi.connect(address='localhost', port=30015, user='user', password='password')

# --- Teradata ---
import teradata
conn = teradata.connect(host='localhost', user='user', password='password')

# --- Vertica ---
import vertica_python
conn = vertica_python.connect(host='localhost', port=5433, user='user', password='password', database='dbname')

# --- Informix ---
import pyodbc
conn = pyodbc.connect("DRIVER={IBM INFORMIX ODBC DRIVER};SERVER=localhost;DATABASE=dbname;HOST=localhost;SERVICE=9088;UID=user;PWD=password")

# --- Sybase/SAP ASE ---
import pyodbc
conn = pyodbc.connect("DRIVER={Adaptive Server Enterprise};SERVER=localhost;PORT=5000;DATABASE=dbname;UID=user;PWD=password")

# --- Greenplum ---
import psycopg2
conn = psycopg2.connect("postgresql://user:password@localhost:5432/greenplum_db")

# --- Pivotal Greenplum ---
import psycopg2
conn = psycopg2.connect("postgresql://gpadmin:password@localhost:5432/gpadmin")

# --- Netezza ---
import pyodbc
conn = pyodbc.connect("DRIVER={NetezzaSQL};SERVER=localhost;PORT=5480;DATABASE=dbname;UID=admin;PWD=password")

# --- Exasol ---
import pyexasol
conn = pyexasol.connect(dsn='localhost:8563', user='sys', password='exasol')

# --- MonetDB ---
import pymonetdb
conn = pymonetdb.connect(hostname='localhost', port=50000, username='monetdb', password='monetdb', database='dbname')

# --- Firebird ---
import fdb
conn = fdb.connect(host='localhost', database='/path/to/database.fdb', user='SYSDBA', password='masterkey')

# --- InterSystems IRIS ---
import pyodbc
conn = pyodbc.connect("DRIVER={InterSystems ODBC};SERVER=localhost;PORT=1972;DATABASE=USER;UID=_SYSTEM;PWD=SYS")

# --- Actian Vector ---
import pyodbc
conn = pyodbc.connect("DRIVER={Actian Vector};SERVER=localhost;DATABASE=dbname;UID=user;PWD=password")

# --- Actian Zen ---
import pyodbc
conn = pyodbc.connect("DRIVER={Actian Zen ODBC Driver};ServerName=localhost;DBQ=dbname;UID=user;PWD=password")

# --- Altibase ---
import pyodbc
conn = pyodbc.connect("DRIVER={Altibase};SERVER=localhost;PORT=20300;DATABASE=mydb;UID=sys;PWD=manager")

# --- Yellowbrick ---
import psycopg2
conn = psycopg2.connect("postgresql://user:password@localhost:5432/yellowbrick")

# --- NuoDB ---
import pynuodb
conn = pynuodb.connect('dbname', 'localhost', user='user', password='password', options={'schema': 'schema'})

# --- Raima ---
import pyodbc
conn = pyodbc.connect("DRIVER={Raima Database Manager};SERVER=localhost;DATABASE=dbname;UID=user;PWD=password")

# --- Empress ---
import pyodbc
conn = pyodbc.connect("DSN=EmpressDSN;UID=user;PWD=password")

# --- Valentina ---
import pyodbc
conn = pyodbc.connect("DRIVER={Valentina};DATABASE=/path/to/db.vdb;UID=user;PWD=password")

# --- OpenLink Virtuoso ---
import pyodbc
conn = pyodbc.connect("DRIVER={OpenLink Virtuoso};HOST=localhost:1111;UID=dba;PWD=dba")

# --- FileMaker ---
import pyodbc
conn = pyodbc.connect("DRIVER={FileMaker ODBC};SERVER=localhost;DATABASE=dbname;UID=user;PWD=password")

# --- 4D ---
import pyodbc
conn = pyodbc.connect("DRIVER={4D v19 ODBC Driver 64-bit};SERVER=localhost;PORT=19812;UID=Designer;PWD=password")


# ============================================================================
# NOSQL DATABASES
# ============================================================================

# --- MongoDB ---
from pymongo import MongoClient
client = MongoClient("mongodb://user:password@localhost:27017/")
client = MongoClient("mongodb://localhost:27017/")  # No auth

# --- Redis ---
import redis
r = redis.Redis(host='localhost', port=6379, db=0, password='password')
r = redis.from_url("redis://:password@localhost:6379/0")

# --- Cassandra ---
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
auth = PlainTextAuthProvider(username='user', password='password')
cluster = Cluster(['localhost'], auth_provider=auth)

# --- ScyllaDB (Cassandra compatible) ---
from cassandra.cluster import Cluster
cluster = Cluster(['localhost'], port=9042)
session = cluster.connect('keyspace')

# --- CouchDB ---
import couchdb
server = couchdb.Server("http://user:password@localhost:5984/")

# --- Couchbase ---
from couchbase.cluster import Cluster
from couchbase.auth import PasswordAuthenticator
cluster = Cluster('couchbase://localhost', authenticator=PasswordAuthenticator('user', 'password'))

# --- RethinkDB ---
import rethinkdb as r
conn = r.connect(host='localhost', port=28015, db='dbname', user='user', password='password')

# --- ArangoDB ---
from arango import ArangoClient
client = ArangoClient(hosts='http://localhost:8529')
db = client.db('dbname', username='user', password='password')

# --- OrientDB ---
import pyorient
client = pyorient.OrientDB('localhost', 2424)
client.connect('user', 'password')

# --- RavenDB ---
from pyravendb.store import document_store
store = document_store.DocumentStore(urls=['http://localhost:8080'], database='dbname')
store.initialize()

# --- Aerospike ---
import aerospike
config = {'hosts': [('localhost', 3000)]}
client = aerospike.client(config).connect('user', 'password')

# --- Riak ---
import riak
client = riak.RiakClient(host='localhost', pb_port=8087, protocol='pbc')

# --- Voldemort ---
from voldemort.client import StoreClient
client = StoreClient('store_name', [('localhost', 6666)])

# --- Datomic ---
import requests
conn = requests.post('http://localhost:8998/data/dbname/')

# --- FaunaDB ---
from faunadb import query as q
from faunadb.client import FaunaClient
client = FaunaClient(secret="secret_key")

# --- SurrealDB ---
from surrealdb import Surreal
db = Surreal('ws://localhost:8000/rpc')
db.signin({'user': 'root', 'pass': 'root'})

# --- EdgeDB ---
import edgedb
client = edgedb.create_client(host='localhost', port=5656, user='edgedb', password='password', database='edgedb')

# --- Tarantool ---
import tarantool
conn = tarantool.connect('localhost', 3301, user='guest', password='password')


# ============================================================================
# GRAPH DATABASES
# ============================================================================

# --- Neo4j ---
from neo4j import GraphDatabase
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("user", "password"))

# --- Dgraph ---
import pydgraph
client_stub = pydgraph.DgraphClientStub('localhost:9080')
client = pydgraph.DgraphClient(client_stub)

# --- Amazon Neptune (Gremlin) ---
from gremlin_python.driver import client
gremlin_client = client.Client('wss://cluster.region.neptune.amazonaws.com:8182/gremlin', 'g')


# ============================================================================
# KEY-VALUE STORES
# ============================================================================

# --- Memcached ---
import pymemcache.client
client = pymemcache.client.base.Client(('localhost', 11211))

# --- LevelDB ---
import plyvel
db = plyvel.DB('database/', create_if_missing=True)

# --- RocksDB ---
import rocksdb
db = rocksdb.DB('database.db', rocksdb.Options(create_if_missing=True))

# --- LMDB ---
import lmdb
env = lmdb.open('database', max_dbs=10)

# --- BerkeleyDB ---
import bsddb3
db = bsddb3.hashopen('database.db', 'c')

# --- UnQLite ---
from unqlite import UnQLite
db = UnQLite('database.db')

# --- Vedis ---
import vedis
db = vedis.Vedis('database.db')

# --- Tokyo Cabinet ---
import pytc
db = pytc.HDB()
db.open('database.tch', pytc.HDBOWRITER | pytc.HDBOCREAT)

# --- Kyoto Cabinet ---
import kyotocabinet as kc
db = kc.DB()
db.open('database.kch', kc.DB.OWRITER | kc.DB.OCREATE)

# --- WhiteDB ---
import whitedb
db = whitedb.attach_database('1000')

# --- FoundationDB ---
import fdb
fdb.api_version(710)
db = fdb.open()

# --- Hazelcast ---
import hazelcast
client = hazelcast.HazelcastClient(cluster_members=['localhost:5701'])

# --- Apache Geode ---
import gemfire
cache = gemfire.CacheFactory().create()

# --- GridDB ---
import griddb_python as griddb
factory = griddb.StoreFactory.get_instance()
store = factory.get_store(host='localhost', port=10001, cluster_name='cluster', username='admin', password='admin')

# --- Apache Ignite ---
from pyignite import Client
client = Client()
client.connect('localhost', 10800)


# ============================================================================
# VECTOR DATABASES
# ============================================================================

# --- Pinecone ---
import pinecone
pinecone.init(api_key='api_key', environment='environment')

# --- Weaviate ---
import weaviate
client = weaviate.Client(url='http://localhost:8080', auth_client_secret=weaviate.AuthApiKey('api_key'))

# --- Milvus ---
from pymilvus import connections
connections.connect(host='localhost', port=19530, user='user', password='password')

# --- Qdrant ---
from qdrant_client import QdrantClient
client = QdrantClient(host='localhost', port=6333, api_key='api_key')

# --- Chroma ---
import chromadb
client = chromadb.Client()

# --- pgvector (PostgreSQL extension) ---
import psycopg2
conn = psycopg2.connect("postgresql://user:password@localhost:5432/vectordb")

# --- Vespa ---
from vespa.application import Vespa
app = Vespa(url='http://localhost:8080')

# --- LanceDB ---
import lancedb
db = lancedb.connect('data/lancedb')

# --- Marqo ---
import marqo
mq = marqo.Client(url='http://localhost:8882')


# ============================================================================
# TIME-SERIES DATABASES
# ============================================================================

# --- InfluxDB ---
from influxdb_client import InfluxDBClient
client = InfluxDBClient(url="http://localhost:8086", token="token", org="org")

# --- TimescaleDB (PostgreSQL extension) ---
import psycopg2
conn = psycopg2.connect("postgresql://user:password@localhost:5432/timescaledb")

# --- TDengine ---
import taos
conn = taos.connect(host='localhost', user='root', password='taosdata', database='dbname')

# --- QuestDB ---
import psycopg2
conn = psycopg2.connect("postgresql://admin:quest@localhost:8812/qdb")

# --- Amazon Timestream ---
import boto3
client = boto3.client('timestream-write', region_name='us-east-1')


# ============================================================================
# SEARCH & ANALYTICS ENGINES
# ============================================================================

# --- Elasticsearch ---
from elasticsearch import Elasticsearch
es = Elasticsearch(["http://localhost:9200"], basic_auth=("user", "password"))

# --- Apache Solr ---
import pysolr
solr = pysolr.Solr('http://localhost:8983/solr/collection', always_commit=True)


# ============================================================================
# COLUMNAR & ANALYTICAL DATABASES
# ============================================================================

# --- ClickHouse ---
from clickhouse_driver import Client
client = Client(host='localhost', port=9000, user='user', password='password', database='dbname')

# --- Apache Druid ---
from pydruid.db import connect
conn = connect(host='localhost', port=8082, path='/druid/v2/sql/', scheme='http')

# --- Apache Pinot ---
from pinotdb import connect
conn = connect(host='localhost', port=8099, path='/query/sql', scheme='http')

# --- Apache Kudu ---
import kudu
client = kudu.connect(host='localhost', port=7051)

# --- Kdb+ ---
from qpython import qconnection
q = qconnection.QConnection(host='localhost', port=5000, username='user', password='password')


# ============================================================================
# BIG DATA & DATA WAREHOUSES
# ============================================================================

# --- Apache Hive ---
from pyhive import hive
conn = hive.Connection(host='localhost', port=10000, username='user', database='dbname')

# --- Apache Impala ---
from impala.dbapi import connect
conn = connect(host='localhost', port=21050, database='default')

# --- Presto/Trino ---
from pyhive import presto
conn = presto.Connection(host='localhost', port=8080, username='user', catalog='catalog', schema='schema')

# --- Presto (prestodb) ---
import prestodb
conn = prestodb.dbapi.connect(host='localhost', port=8080, user='user', catalog='hive', schema='default')

# --- Apache Drill ---
from pydrill.client import PyDrill
drill = PyDrill(host='localhost', port=8047)

# --- Apache HBase ---
import happybase
conn = happybase.Connection('localhost', port=9090)

# --- Apache Phoenix (HBase SQL) ---
import phoenixdb
conn = phoenixdb.connect('http://localhost:8765/', autocommit=True)

# --- Apache Accumulo ---
from pyaccumulo import Accumulo
conn = Accumulo(host='localhost', port=42424, user='root', password='secret')

# --- Snowflake ---
import snowflake.connector
conn = snowflake.connector.connect(user='user', password='password', account='account', warehouse='warehouse', database='dbname', schema='schema')

# --- Databricks ---
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('app').config('spark.databricks.service.address', 'https://workspace.cloud.databricks.com').config('spark.databricks.service.token', 'token').getOrCreate()

# --- Rockset ---
from rockset import Client
client = Client(api_key='api_key', api_server='https://api.rs2.usw2.rockset.com')

# --- Dremio ---
import pyodbc
conn = pyodbc.connect("DRIVER={Dremio Connector};HOST=localhost;PORT=31010;UID=user;PWD=password")

# --- Splice Machine ---
import jaydebeapi
conn = jaydebeapi.connect('com.splicemachine.db.jdbc.ClientDriver', 'jdbc:splice://localhost:1527/splicedb', ['splice', 'admin'], '/path/to/splice.jar')


# ============================================================================
# CLOUD DATABASES - AWS
# ============================================================================

# --- Amazon RDS (PostgreSQL) ---
import psycopg2
conn = psycopg2.connect("postgresql://user:password@instance.region.rds.amazonaws.com:5432/dbname")

# --- Amazon RDS (MySQL) ---
import mysql.connector
conn = mysql.connector.connect(host='instance.region.rds.amazonaws.com', user='user', password='password', database='dbname')

# --- Amazon Aurora (PostgreSQL) ---
import psycopg2
conn = psycopg2.connect("postgresql://user:password@cluster.region.rds.amazonaws.com:5432/dbname")

# --- Amazon Aurora (MySQL) ---
import mysql.connector
conn = mysql.connector.connect(host='cluster.region.rds.amazonaws.com', user='user', password='password', database='dbname')

# --- Amazon Redshift ---
import psycopg2
conn = psycopg2.connect("postgresql://user:password@cluster.region.redshift.amazonaws.com:5439/dbname")

# --- Amazon DynamoDB ---
import boto3
dynamodb = boto3.resource('dynamodb', region_name='us-east-1', aws_access_key_id='key', aws_secret_access_key='secret')

# --- Amazon DocumentDB (MongoDB compatible) ---
from pymongo import MongoClient
client = MongoClient("mongodb://user:password@cluster.region.docdb.amazonaws.com:27017/?tls=true&tlsCAFile=rds-combined-ca-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred")


# ============================================================================
# CLOUD DATABASES - AZURE
# ============================================================================

# --- Azure SQL Database ---
import pyodbc
conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=server.database.windows.net;DATABASE=dbname;UID=user;PWD=password")

# --- Azure Cosmos DB (MongoDB API) ---
from pymongo import MongoClient
client = MongoClient("mongodb://account:key@account.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb")


# ============================================================================
# CLOUD DATABASES - GOOGLE CLOUD
# ============================================================================

# --- Google Cloud SQL (PostgreSQL) ---
import psycopg2
conn = psycopg2.connect("postgresql://user:password@/dbname?host=/cloudsql/project:region:instance")

# --- Google Cloud SQL (MySQL) ---
import mysql.connector
conn = mysql.connector.connect(unix_socket='/cloudsql/project:region:instance', user='user', password='password', database='dbname')

# --- Google BigQuery ---
from google.cloud import bigquery
client = bigquery.Client(project='project-id')

# --- Google Firestore ---
from google.cloud import firestore
db = firestore.Client(project='project-id')


# ============================================================================
# MANAGED DATABASE SERVICES
# ============================================================================

# --- Supabase (PostgreSQL) ---
import psycopg2
conn = psycopg2.connect("postgresql://user:password@db.project.supabase.co:5432/postgres")

# --- PlanetScale (MySQL) ---
import mysql.connector
conn = mysql.connector.connect(host='host.psdb.cloud', user='user', password='password', database='dbname', ssl_ca='/path/to/ca.pem')

# --- Neon (PostgreSQL) ---
import psycopg2
conn = psycopg2.connect("postgresql://user:password@project.neon.tech/dbname?sslmode=require")

# --- CockroachDB ---
import psycopg2
conn = psycopg2.connect("postgresql://user:password@localhost:26257/dbname?sslmode=require")

# --- YugabyteDB ---
import psycopg2
conn = psycopg2.connect("postgresql://user:password@localhost:5433/yugabyte")

# --- TiDB (MySQL compatible) ---
import mysql.connector
conn = mysql.connector.connect(host='localhost', port=4000, user='root', password='password', database='dbname')

# --- SingleStore (MemSQL) ---
import mysql.connector
conn = mysql.connector.connect(host='localhost', port=3306, user='user', password='password', database='dbname')

# --- Vitess (MySQL) ---
import mysql.connector
conn = mysql.connector.connect(host='localhost', port=15306, user='user', password='password', database='dbname')

# --- CrateDB ---
import crate
conn = crate.client.connect('localhost:4200')

# --- MatrixOne ---
import pymysql
conn = pymysql.connect(host='localhost', port=6001, user='root', password='111', database='dbname')

# --- OceanBase ---
import pymysql
conn = pymysql.connect(host='localhost', port=2881, user='root', password='password', database='oceanbase')

# --- OpenGauss ---
import psycopg2
conn = psycopg2.connect("postgresql://user:password@localhost:5432/postgres")

# --- Databend ---
import mysql.connector
conn = mysql.connector.connect(host='localhost', port=3307, user='root', password='', database='default')


# ============================================================================
# EMBEDDED DATABASES
# ============================================================================

# --- H2 Database ---
import jaydebeapi
conn = jaydebeapi.connect('org.h2.Driver', 'jdbc:h2:~/test', ['sa', ''], '/path/to/h2.jar')

# --- Apache Derby ---
import jaydebeapi
conn = jaydebeapi.connect('org.apache.derby.jdbc.EmbeddedDriver', 'jdbc:derby:dbname;create=true', ['user', 'password'], '/path/to/derby.jar')

# --- HSQLDB ---
import jaydebeapi
conn = jaydebeapi.connect('org.hsqldb.jdbc.JDBCDriver', 'jdbc:hsqldb:file:dbname', ['SA', ''], '/path/to/hsqldb.jar')

# --- Realm ---
import realm
config = realm.Configuration()
realm_instance = realm.Realm(config=config)

# --- ObjectBox ---
from objectbox import Store
store = Store()

# --- ITTIA DB ---
import ctypes
ittiadb = ctypes.CDLL('libittiadb.so')


# ============================================================================
# XML DATABASES
# ============================================================================

# --- MarkLogic ---
from marklogic import Client
client = Client('http://localhost:8000', digest=('user', 'password'))

# --- BaseX ---
from BaseXClient import Session
session = Session('localhost', 1984, 'admin', 'admin')

# --- eXist-db ---
import requests
from requests.auth import HTTPBasicAuth
response = requests.get('http://localhost:8080/exist/rest/db/', auth=HTTPBasicAuth('admin', 'admin'))

# --- Sedna ---
import pysedna
conn = pysedna.connect('localhost', 'dbname', 'user', 'password')

# --- Tamino ---
import requests
response = requests.get('http://localhost/tamino/dbname', auth=('user', 'password'))


# ============================================================================
# OBJECT DATABASES
# ============================================================================

# --- Objectivity/DB ---
import objy
ooConnection = objy.bootConnection('localhost', 6779)

# --- Versant ---
import versant
db = versant.connect('localhost', 'dbname', 'user', 'password')

# --- GemStone/S ---
import gemstone
session = gemstone.GsSession('localhost', 'DataCurator', 'swordfish')


# ============================================================================
# MAINFRAME & LEGACY DATABASES
# ============================================================================

# --- Adabas ---
import pyodbc
conn = pyodbc.connect("DRIVER={Adabas D};SERVERDB=localhost:7200;SERVERNODE=localhost:7269;UID=user;PWD=password")

# --- Model 204 ---
import m204
conn = m204.connect('localhost', 'user', 'password')

# --- IDMS ---
import pyodbc
conn = pyodbc.connect("DRIVER={CA IDMS};DICTNAME=SYSTEM;DBNAME=IDMS;HOST=localhost;PORT=3709;UID=user;PWD=password")

# --- IMS ---
import jaydebeapi
conn = jaydebeapi.connect('com.ibm.ims.db.opendb.jdbc.IMSDriver', 'jdbc:ims://localhost:9999', ['user', 'password'], '/path/to/ims.jar')

# --- DATACOM ---
import pyodbc
conn = pyodbc.connect("DRIVER={CA Datacom};SERVER=localhost;DATABASE=dbname;UID=user;PWD=password")

# --- GT.M ---
import gtm
gtm.open()

# --- Caché (InterSystems) ---
import intersys.pythonbind3
conn = intersys.pythonbind3.connection()
conn.connect_now('localhost[1972]:USER', 'user', 'password', None)

# --- Mnesia (Erlang) ---
from pyrlang import Node, Atom
node = Node('py@localhost', 'cookie')


# ============================================================================
# SPECIALIZED & OTHER DATABASES
# ============================================================================

# --- VoltDB ---
import voltdb
client = voltdb.FastSerializer('localhost', 21212)

# --- VoltDB (using voltcli) ---
from voltcli import connect
conn = connect(host='localhost', port=21212, username='user', password='password')

# --- Clustrix (now MariaDB Xpand) ---
import mysql.connector
conn = mysql.connector.connect(host='localhost', port=3306, user='user', password='password', database='dbname')

# --- Sadas ---
import pyodbc
conn = pyodbc.connect("DSN=SadasDSN;UID=user;PWD=password")

# --- Polyglot (GraalVM) ---
import polyglot
context = polyglot.eval(language='js', string='({connect: function() {}})')

# --- Apache Solr ---
import pysolr
solr = pysolr.Solr('http://localhost:8983/solr/collection', always_commit=True)

# --- Memgraph ---
from neo4j import GraphDatabase
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("user", "password"))

# --- NebulaGraph ---
from nebula3.gclient.net import ConnectionPool
from nebula3.Config import Config
config = Config()
connection_pool = ConnectionPool()
connection_pool.init([('localhost', 9669)], config)

# --- JanusGraph ---
from gremlin_python.driver import client
gremlin_client = client.Client('ws://localhost:8182/gremlin', 'g')

# --- TigerGraph ---
import pyTigerGraph as tg
conn = tg.TigerGraphConnection(host="localhost", graphname="MyGraph", username="user", password="password")

# --- Apache AGE (PostgreSQL extension) ---
import psycopg2
conn = psycopg2.connect("postgresql://user:password@localhost:5432/postgres")

# --- RedisGraph ---
from redisgraph import Graph
graph = Graph('social', redis.Redis(host='localhost', port=6379))

# --- Cayley ---
import requests
response = requests.post('http://localhost:64210/api/v2/query', json={'query': 'g.V().All()'})

# --- StarDog ---
import requests
from requests.auth import HTTPBasicAuth
response = requests.post('http://localhost:5820/mydb/query', auth=HTTPBasicAuth('admin', 'admin'), data={'query': 'SELECT * WHERE {?s ?p ?o}'})

# --- AllegroGraph ---
from franz.openrdf.sail.allegrographserver import AllegroGraphServer
server = AllegroGraphServer('localhost', port=10035, user='user', password='password')

# --- Blazegraph ---
import requests
response = requests.post('http://localhost:9999/blazegraph/sparql', data={'query': 'SELECT * WHERE {?s ?p ?o}'})

# --- Apache Jena Fuseki ---
from SPARQLWrapper import SPARQLWrapper
sparql = SPARQLWrapper("http://localhost:3030/dataset/query")

# --- GraphDB (Ontotext) ---
from SPARQLWrapper import SPARQLWrapper
sparql = SPARQLWrapper("http://localhost:7200/repositories/repo")

# --- Titan ---
from gremlin_python.driver import client
gremlin_client = client.Client('ws://localhost:8182/gremlin', 'g')

# --- HyperGraphDB ---
import jpype
jpype.startJVM(classpath=['hypergraphdb.jar'])

# --- Grakn (TypeDB) ---
from typedb.client import TypeDB
client = TypeDB.core_client('localhost:1729')

# --- TerminusDB ---
from terminusdb_client import WOQLClient
client = WOQLClient("http://localhost:6363")

# --- FalkorDB ---
from redis import Redis
from redisgraph import Graph
r = Redis(host='localhost', port=6379)
graph = Graph('social', r)

# --- Memcached (pymemcache) ---
from pymemcache.client.base import Client
client = Client(('localhost', 11211))

# --- Ehcache ---
import requests
response = requests.get('http://localhost:8080/ehcache/rest/cache/key')

# --- Infinispan ---
from infinispan.hotrod import RemoteCacheManager
cache_manager = RemoteCacheManager(host='localhost', port=11222)

# --- Coherence ---
import coherence
session = coherence.Session('localhost:7574')

# --- GemFire ---
import gemfire
cache = gemfire.CacheFactory().create()

# --- Apache Kafka (as database) ---
from kafka import KafkaProducer, KafkaConsumer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
consumer = KafkaConsumer('topic', bootstrap_servers='localhost:9092')

# --- Apache Pulsar ---
import pulsar
client = pulsar.Client('pulsar://localhost:6650')

# --- RabbitMQ (as message store) ---
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# --- NATS ---
import nats
nc = nats.connect("nats://localhost:4222")

# --- EventStoreDB ---
from esdbclient import EventStoreDBClient
client = EventStoreDBClient(uri="esdb://localhost:2113?tls=false")

# --- Pravega ---
import pravega_client
stream_manager = pravega_client.StreamManager("tcp://localhost:9090")

# --- Dragonfly ---
import redis
r = redis.Redis(host='localhost', port=6379)

# --- KeyDB ---
import redis
r = redis.Redis(host='localhost', port=6379)

# --- Garnet ---
import redis
r = redis.Redis(host='localhost', port=6379)

# --- Redict ---
import redis
r = redis.Redis(host='localhost', port=6379)

# --- Valkey ---
import redis
r = redis.Redis(host='localhost', port=6379)

# --- DragonflyDB ---
import redis
r = redis.Redis(host='localhost', port=6379)

# --- Skytable ---
import skytable
conn = skytable.Connection('localhost', 2003)

# --- TileDB ---
import tiledb
ctx = tiledb.Ctx()

# --- Zarr ---
import zarr
store = zarr.DirectoryStore('data.zarr')

# --- HDF5 ---
import h5py
f = h5py.File('data.h5', 'r')

# --- Parquet ---
import pyarrow.parquet as pq
table = pq.read_table('data.parquet')

# --- ORC ---
import pyarrow.orc as orc
table = orc.read_table('data.orc')

# --- Avro ---
from avro.datafile import DataFileReader
from avro.io import DatumReader
reader = DataFileReader(open('data.avro', 'rb'), DatumReader())

# --- Feather ---
import pyarrow.feather as feather
df = feather.read_feather('data.feather')

# --- Arrow ---
import pyarrow as pa
table = pa.ipc.open_file('data.arrow').read_all()

# --- DuckDB ---
import duckdb
conn = duckdb.connect('database.db')

# --- Polars ---
import polars as pl
df = pl.read_database("SELECT * FROM table", "postgresql://user:password@localhost:5432/dbname")

# --- Databend Cloud ---
import mysql.connector
conn = mysql.connector.connect(host='tenant.databend.com', port=443, user='user', password='password', database='default')

# --- Firebolt ---
from firebolt.db import connect
conn = connect(database='dbname', username='user', password='password', engine_name='engine')

# --- Hydrolix ---
import requests
response = requests.post('https://cluster.hydrolix.io/query', auth=('user', 'password'), json={'query': 'SELECT * FROM table'})

# --- Tinybird ---
import requests
response = requests.get('https://api.tinybird.co/v0/pipes/pipe.json', headers={'Authorization': 'Bearer token'})

# --- MotherDuck ---
import duckdb
conn = duckdb.connect('md:database?motherduck_token=token')

# --- Turso (libSQL) ---
import libsql_client
client = libsql_client.create_client(url='libsql://database.turso.io', auth_token='token')

# --- Xata ---
import requests
response = requests.get('https://workspace.xata.sh/db/database:branch/tables/table/query', headers={'Authorization': 'Bearer token'})

# --- Convex ---
import requests
response = requests.post('https://happy-animal-123.convex.cloud/api/query', json={'path': 'messages:list'})

# --- Fauna (v10) ---
from fauna import fql
from fauna.client import Client
client = Client(secret='secret')

# --- Upstash Redis ---
import redis
r = redis.Redis(host='endpoint.upstash.io', port=6379, password='password', ssl=True)

# --- Momento ---
from momento import CacheClient, Configurations, CredentialProvider
client = CacheClient(Configurations.Laptop.v1(), CredentialProvider.from_environment_variable('MOMENTO_API_KEY'), default_ttl_seconds=60)

# --- Aerospike Cloud ---
import aerospike
config = {'hosts': [('cluster.aerospike.io', 3000)], 'policies': {'auth_mode': aerospike.AUTH_EXTERNAL}}
client = aerospike.client(config).connect('user', 'password')

# --- Astra DB (DataStax) ---
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
cloud_config = {'secure_connect_bundle': '/path/to/bundle.zip'}
auth_provider = PlainTextAuthProvider('token', 'token')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)

# --- MongoDB Atlas ---
from pymongo import MongoClient
client = MongoClient("mongodb+srv://user:password@cluster.mongodb.net/?retryWrites=true&w=majority")

# --- Redis Cloud ---
import redis
r = redis.Redis(host='endpoint.cloud.redislabs.com', port=12345, password='password', ssl=True)

# --- ElastiCache (Redis) ---
import redis
r = redis.Redis(host='cluster.cache.amazonaws.com', port=6379, ssl=True)

# --- MemoryDB (AWS) ---
import redis
r = redis.Redis(host='cluster.memorydb.region.amazonaws.com', port=6379, ssl=True)

# --- Azure Cache for Redis ---
import redis
r = redis.Redis(host='cache.redis.cache.windows.net', port=6380, password='password', ssl=True)

# --- Google Cloud Memorystore (Redis) ---
import redis
r = redis.Redis(host='10.0.0.3', port=6379)

# --- Cloudflare D1 ---
import requests
response = requests.post('https://api.cloudflare.com/client/v4/accounts/account_id/d1/database/database_id/query', headers={'Authorization': 'Bearer token'}, json={'sql': 'SELECT * FROM table'})

# --- Cloudflare KV ---
import requests
response = requests.get('https://api.cloudflare.com/client/v4/accounts/account_id/storage/kv/namespaces/namespace_id/values/key', headers={'Authorization': 'Bearer token'})

# --- Cloudflare Durable Objects ---
import requests
response = requests.post('https://worker.account.workers.dev/', json={'method': 'get', 'key': 'value'})

# --- Vercel Postgres ---
import psycopg2
conn = psycopg2.connect("postgres://user:password@endpoint.postgres.vercel-storage.com/database?sslmode=require")

# --- Vercel KV ---
import redis
r = redis.Redis(host='endpoint.kv.vercel-storage.com', port=6379, password='password', ssl=True)

# --- Railway PostgreSQL ---
import psycopg2
conn = psycopg2.connect("postgresql://user:password@containers.railway.app:5432/railway")

# --- Render PostgreSQL ---
import psycopg2
conn = psycopg2.connect("postgresql://user:password@hostname.render.com/database")

# --- Fly.io PostgreSQL ---
import psycopg2
conn = psycopg2.connect("postgresql://user:password@appname.internal:5432/database")


# ============================================================================
# SQLALCHEMY - UNIVERSAL ORM
# ============================================================================

from sqlalchemy import create_engine

# PostgreSQL
engine = create_engine("postgresql://user:password@localhost:5432/dbname")

# MySQL
engine = create_engine("mysql+mysqlconnector://user:password@localhost:3306/dbname")

# SQLite
engine = create_engine("sqlite:///database.db")

# SQL Server
engine = create_engine("mssql+pyodbc://user:password@localhost/dbname?driver=ODBC+Driver+17+for+SQL+Server")

# Oracle
engine = create_engine("oracle+cx_oracle://user:password@localhost:1521/?service_name=service")
