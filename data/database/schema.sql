-- Identifying information for films
-- IMDb ID is an optional field, but useful for connecting to external sources
DROP TABLE IF EXISTS films;

CREATE TABLE films (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    wikidata_id TEXT,
    title TEXT,
    imdb_id TEXT
);

-- Cast and crew information
-- This includes directors, actors, cinematographers, producers, etc.
DROP TABLE IF EXISTS crew;

CREATE TABLE crew (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    wikidata_id TEXT,
    name TEXT,
    imdb_id TEXT
);

-- This table holds Wikidata IDs for connecting terms
-- Ex. Wikidata for 'film director' is Q2526255
DROP TABLE IF EXISTS util;

CREATE TABLE util (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    wikidata_id TEXT,
    connector TEXT
);