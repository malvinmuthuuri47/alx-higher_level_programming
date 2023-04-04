-- creates a sql table
-- script shouldn't fail if the table already exists.

CREATE TABLE IF NOT EXISTS force_name(
	id INT,
	name VARCHAR(256) NOT NULL
);
