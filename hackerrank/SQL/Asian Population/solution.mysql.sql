SELECT SUM(city.population) FROM city JOIN country ON country.code = city.countrycode WHERE continent = 'Asia';
