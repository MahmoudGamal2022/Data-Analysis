SELECT i.CustomerId , c.FirstName , SUM(i.Total) AS money_spent 
FROM Invoice i
LEFT JOIN Customer c on i.CustomerId == c.CustomerId
GROUP BY i.CustomerId
ORDER BY money_spent DESC 
LIMIT 10