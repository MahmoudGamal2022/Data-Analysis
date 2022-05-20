
SELECT BillingCountry , count(BillingCountry) as Invoices
from Invoice
GROUP by BillingCountry
ORDER by Invoices DESC
-----------------------------------------------------------------------
SELECT DISTINCT c.Email, c.FirstName, c.LastName,g.Name
from Customer c
JOIN Invoice i , InvoiceLine il , Track t, Genre g
ON c.CustomerId == i.CustomerId and i.InvoiceId == il.InvoiceId and il.TrackId == t.TrackId and t.GenreId == g.GenreId
WHERE g.Name == 'Rock'
ORDER by c.Email
------------------------------------------------------------------
SELECT BillingCountry , sum(total) as Seles
from Invoice
GROUP by BillingCountry
ORDER by Seles DESC
----------------------------------------------------------------------
SELECT BillingCity,
       SUM(Total)  AS Dollars 
  FROM Invoice 
GROUP BY BillingCity 
ORDER BY Dollars DESC
LIMIT 10
-------------------------------------------------------------------------
SELECT i.CustomerId , c.FirstName , SUM(i.Total) AS money_spent 
FROM Invoice i
LEFT JOIN Customer c on i.CustomerId == c.CustomerId
GROUP BY i.CustomerId
ORDER BY money_spent DESC 
LIMIT 10
-----------------------------------------------------------------
SELECT  g.Name , count(a.ArtistId) as artist_number
from Artist a
JOIN Album al on a.ArtistId == al.ArtistId
JOIN Track t on al.AlbumId == t.AlbumId
join Genre g on t.GenreId == g.GenreId
GROUP by g.Name
order by artist_number DESC
-------------------------------------------------------------------------
SELECT a.ArtistId, a.Name,g.Name , count(a.ArtistId) as artist_number
from Artist a
JOIN Album al on a.ArtistId == al.ArtistId
JOIN Track t on al.AlbumId == t.AlbumId
join Genre g on t.GenreId == g.GenreId
where g.Name == 'Rock'
GROUP by a.Name
order by artist_number DESC
LIMIT 10
---------------------------------------------------------------------------
select al.AlbumId, al.Title ,SUM(il.unitprice * il.quantity) as top_album
from Album al
JOIN Track t on al.AlbumId == t.AlbumId
join InvoiceLine il on  t.TrackId == il.TrackId 
GROUP by al.Title
order by top_album DESC
LIMIT 10
----------------------------------------------------------------------------------
SELECT a.Name , sum(il.UnitPrice * il.Quantity) as best_sale
FROM Artist as a
JOIN Album as al on a.ArtistId == al.ArtistId
JOIN Track as t on al.AlbumId == t.AlbumId
JOIN InvoiceLine as il on t.TrackId == il.TrackId
group by a.Name
ORDER by best_sale DESC
LIMIT 10
---------------------------------------------------------------------------
SELECT g.Name , g.GenreId , sum(il.Quantity * il.UnitPrice) as sum_genre
from Genre g
JOIN Track t on g.GenreId == t.GenreId
JOIN InvoiceLine il on t.TrackId == il.TrackId 
GROUP by g.Name
order by sum_genre DESC