
1select * from auto;
2select make, model from auto where make contains 'volv';
3select make, model, cylinder_layout, boost_type as "марка", "модель", "положение цилиндров","наличие турбины" from auto;
4select * from auto where cylinder_layout = 'V-type';
5select * from auto where year_from >= '1999';
6select * from auto where year_from >= 2001 and year_to <= 2010;
6select * from auto where year_from berween (2001, 2010);
7select * from auto where series != 'sedan' and series != 'crossover';
7select * from auto where series not in ('sedan','crossover');
8select make, model, series, drive_wheels, transmission from auto where year_from > 2014 and drive_wheels not in 'Turbo';
9select * from auto where model like '%t%' and make like '%t%';
10select make, model, year_from, series, transmission from auto where drive_wheels = 'Four wheel drive' order by make limit 20;
