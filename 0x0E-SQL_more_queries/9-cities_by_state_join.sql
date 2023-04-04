-- List all cities contained in the database
-- Each record should display cities.id - cities.name - states.name
-- Results should be ordered in ascending order by cities.id

SELECT c.`id`, c.`name`, s.`name`
	FROM `cities` AS c
	INNER JOIN `states` AS s
	ON c.`state_id` = s.id
	ORDER BY c.`id`;
