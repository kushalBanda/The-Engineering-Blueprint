# Database Indexing

## Overview

![DB Indexing](./assets/DB%20Indexing.png)

## How do indexes speed up queries?

![How do indexes speed up queries?](./assets/How%20do%20indexes%20speed%20up%20queries%3F.png)

## Types of Index

### B-Tree

The workhorse of databases. B-Trees handle 95% of indexing needs in production systems like PostgreSQL, MySQL, and Oracle. They're fast for both exact matches (`WHERE user_id = 123`) and range queries (`WHERE age > 25 AND age < 40`).

**When to use:** Default choice for most indexes. Works for sorting, searching, and filtering across any data type.

**Production reality:** Every relational database uses B-Trees as the primary index structure. If you're not sure which index to use, use this one.

![B-Tree](./assets/B-Tree.png)

### Hash Index

Lightning-fast lookups for exact matches, but useless for anything else. Hash indexes can't handle range queries, sorting, or pattern matching. They only answer "does this exact value exist?"

**When to use:** In-memory databases (Redis, Memcached) or when you only need equality checks like session lookups (`WHERE session_id = 'abc123'`).

**Production reality:** Less common than B-Trees. MySQL's MEMORY engine supports them, but InnoDB doesn't even offer hash indexes as an option. Most teams stick with B-Trees because the flexibility is worth the tiny performance trade-off.

![Hash Index](./assets/Hash%20Index.png)

### Geospatial Indexes

Built for location queries like "find all restaurants within 5km" or "which delivery zone contains this address?" You can't do this efficiently with regular B-Trees because coordinates are two-dimensional.

**When to use:** Any app with maps, location search, or proximity features. Ride-sharing, food delivery, real estate, and gaming all rely on these.

**Production reality:** R-trees dominate production systems (PostGIS uses them). Geohashing shows up in distributed systems like Elasticsearch. Quadtrees are common in game engines and tile-based mapping.

![Geospatial Indexes](./assets/Geospatial%20Indexes.png)

#### 1. Geohashing

Converts 2D coordinates into a single string like "9q8yy". Nearby locations share the same prefix, so you can search by prefix to find neighbors. Simple to implement and works great with regular databases.

**Best for:** Proximity searches in distributed systems. Uber and DoorDash use variants of this for driver matching.
![Geohashing](./assets/Geohasing.png)

#### 2. Quadtrees

Divides space into four quadrants recursively until each quadrant has few enough points. Think of Google Maps zooming in—each zoom level splits the map into smaller tiles.

**Best for:** In-memory spatial indexing and collision detection. Game engines use quadtrees to find objects near the player. Google Maps uses them for rendering tile layers.

![Quadtrees](./assets/QuadTrees.png)

#### 3. R-trees

Stores bounding boxes that group nearby spatial objects. Handles overlapping regions and complex shapes (not just points). Can answer "which polygons intersect this area?"

**Best for:** Full-featured spatial databases. PostGIS (PostgreSQL's spatial extension) uses R-trees. Every serious mapping application—Google Maps data storage, GPS systems, GIS software—runs on R-trees.

**Production reality:** If you're using `ST_Distance` or `ST_Contains` in PostgreSQL, you're using an R-tree under the hood.
![R-trees](./assets/R-Tree.png)

### Inverted Index

Flips the normal index structure on its head. Instead of mapping documents to words, it maps words to documents. When you search for "pizza", the index instantly returns every document containing that word.

Regular B-Trees fail at full-text search because they can't handle `LIKE '%pizza%'` queries without scanning every row. Inverted indexes solve this by pre-processing text and building a lookup table of every word.

**When to use:** Full-text search across documents, logs, or any text-heavy content. Search bars, document management systems, and log analysis tools all need this.

**Production reality:** Elasticsearch and Solr are built entirely on inverted indexes. PostgreSQL's `tsvector` type uses them for full-text search. Every search engine you've used—Google, database search features, documentation sites—runs on inverted indexes.

![Inverted Index](./assets/Inverted%20Index.png)

## Choosing the Right Index

![Flow Chart](./assets/Flow%20Chart.png)
