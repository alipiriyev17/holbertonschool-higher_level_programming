-- List all cities and their state names in hbtn_0d_usa, sorted by cities.id

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
