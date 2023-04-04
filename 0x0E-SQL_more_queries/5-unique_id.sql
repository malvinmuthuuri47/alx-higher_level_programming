-- create a table in the SQL server
-- The DB name will be passed as an argument in the command
-- if table already exists, the script shouldn't fail

CREATE TABLE IF NOT EXISTS unique_id(
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256)
	);
