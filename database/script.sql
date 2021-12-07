CREATE TABLE login (
  id serial,
  username varchar(100) DEFAULT NULL,
  email varchar(100) DEFAULT NULL,
  password varchar(100) DEFAULT NULL,
  PRIMARY KEY (id)
) 
CREATE TABLE mobile (
  id serial,
  screen_size varchar(50) DEFAULT NULL,
  color varchar(50) DEFAULT NULL,
  PRIMARY KEY (id)
)

create TABLE laptop(
	id serial,
    HD_Capacity varchar(100) DEFAULT NULL,
  	PRIMARY KEY (id)
)

CREATE TABLE products (
  id serial,
  NAME varchar(100) DEFAULT NULL,
  Description varchar(255) DEFAULT NULL,
  Category varchar(10) DEFAULT NULL,
  Processor varchar(100) DEFAULT NULL,
  RAM varchar(50) DEFAULT NULL,
  laptop_id INT,
  mobile_id INT,
  PRIMARY KEY (id),
  CONSTRAINT fk_laptop FOREIGN KEY (laptop_id) REFERENCES laptop(id) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_mobile FOREIGN KEY (mobile_id) REFERENCES mobile (id) ON DELETE CASCADE ON UPDATE CASCADE
) 