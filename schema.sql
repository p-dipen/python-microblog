DROP TABLE IF EXISTS user;

CREATE TABLE user (
    id integer PRIMARY KEY AUTOINCREMENT,
    username text not null,
    password text not null
);