UPDATE Salary SET sex = CHAR(ASCII('f') + ASCII('m') - ASCII(sex));

# faster
UPDATE Salary SET sex = IF(sex='m', 'f', 'm'); 