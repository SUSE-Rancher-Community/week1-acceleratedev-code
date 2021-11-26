-- Drop possibly existing data and create empty tables

DROP TABLE IF EXISTS shoppinglist;

CREATE TABLE shoppinglist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item TEXT UNIQUE NOT NULL,
    quantity INTEGER NOT NULL
);
