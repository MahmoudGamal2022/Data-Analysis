SELECT g.Name , g.GenreId , sum(il.Quantity * il.UnitPrice) as sum_genre
from Genre g
JOIN Track t on g.GenreId == t.GenreId
JOIN InvoiceLine il on t.TrackId == il.TrackId 
GROUP by g.Name
order by sum_genre DESC