DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS product;
CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  authkey TEXT NOT NULL,
  password TEXT NOT NULL
);


CREATE TABLE product (
  id INTEGER PRIMARY KEY unique,
  title TEXT NOT NULL,
  detail TEXT NOT NULL,
  price INTEGER NOT NULL,
  size TEXT NOT NULL,
  color TEXT,
  quantity INTEGER NOT NULL
);

CREATE TABLE product_inv (
  id INTEGER PRIMARY KEY unique,
  title TEXT NOT NULL,
  detail TEXT NOT NULL,
  price INTEGER NOT NULL,
  size TEXT NOT NULL,
  color TEXT,
  quantity INTEGER NOT NULL
);

CREATE TABLE cart(
  id INTEGER PRIMARY KEY,
  total INTEGER ,
  payment_id,
  created_at timestamp,
  modified_at timestamp,
)
