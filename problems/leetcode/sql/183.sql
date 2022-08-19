SELECT A.Name as Customers FROM Customers A
WHERE NOT EXISTS (SELECT 1 FROM Orders B WHERE A.Id = B.CustomerId)

SELECT A.Name as Customers FROM Customers A
WHERE A.Id NOT IN (SELECT B.CustomerId from Orders B)

SELECT A.Name as Customers from Customers A
LEFT JOIN Orders B on A.Id = B.CustomerId
WHERE B.CustomerId IS NULL