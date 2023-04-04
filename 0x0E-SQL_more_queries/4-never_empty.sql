-- create a table on the sql server
-- Db name will be passed as an argument in the sql command
-- if table exists, the script shouldn't fail

CREATE TABLE IF NOT EXISTS id_not_null(
	id INT DEFAULT 1,
	name VARCHAR(256)
	);
