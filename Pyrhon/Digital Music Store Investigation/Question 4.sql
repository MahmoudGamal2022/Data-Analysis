SELECT BillingCity,
       SUM(Total)  AS Dollars 
  FROM Invoice 
GROUP BY BillingCity 
ORDER BY Dollars DESC
LIMIT 10