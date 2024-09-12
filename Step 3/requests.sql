-- 1. Выберите уникальные регионы сбора грибов.

SELECT DISTINCT name
FROM Regions;

-- 2. Выведите название, сезон сбора и съедобность грибов, которые относятся к категории «Трубчатые».

SELECT m.name, m.season, m.edible
FROM Mushrooms m
JOIN Categories c ON m.category_id = c.category_id
WHERE c.name = 'Трубчатые';

-- 3. Посчитайте количество грибов для каждой категории. Выведите название категории и количество в порядке убывания.

SELECT c.name, COUNT(m.mushroom_id) AS mushroom_count
FROM Categories c
LEFT JOIN Mushrooms m ON c.category_id = m.category_id
GROUP BY c.name
ORDER BY mushroom_count DESC;

-- 4. Выведите название и описание съедобных грибов, которые лучше всего собирать в пяти самых больших по размеру (size) регионах.

SELECT m.name, m.description
FROM Mushrooms m
JOIN Regions r ON m.primary_region_id = r.region_id
WHERE m.edible = TRUE
ORDER BY r.size DESC
LIMIT 5;

-- 5. Выведите названия всех грибов, которые растут весной, относятся к категории «Пластинчатые» и которые лучше всего собирать в местах размером до 6000 условных единиц (size).

SELECT m.name
FROM Mushrooms m
JOIN Categories c ON m.category_id = c.category_id
JOIN Regions r ON m.primary_region_id = r.region_id
WHERE m.season = 'Весна'
  AND c.name = 'Пластинчатые'
  AND r.size <= 6000;