DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS synonyms;
DROP TABLE IF EXISTS examples;
DROP TABLE IF EXISTS antonyms;
DROP TABLE IF EXISTS texts;
DROP TABLE IF EXISTS texts_from_users;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descriptor TEXT NOT NULL,
    pos_tag TEXT,
    content TEXT NOT NULL,
    notes TEXT
);

CREATE TABLE synonyms (
    syn_id INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id INT,
    ascriptor TEXT NOT NULL,
    marks TEXT,
    notes TEXT,
    FOREIGN KEY (post_id) REFERENCES posts(id)
);

CREATE TABLE antonyms (
    ant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id INT,
    ascriptor TEXT NOT NULL,
    marks TEXT,
    notes TEXT,
    FOREIGN KEY (post_id) REFERENCES posts(id)
);

CREATE TABLE examples (
    ex_id INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id INT,
    content TEXT NOT NULL,
    keyword TEXT NOT NULL,
    source INT,
    FOREIGN KEY (post_id) REFERENCES posts(id)
);

CREATE TABLE texts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    link TEXT NOT NULL,
    date TEXT,
    content TEXT NOT NULL
);

CREATE TABLE texts_from_users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    link TEXT NOT NULL,
    date TEXT,
    content TEXT NOT NULL
);