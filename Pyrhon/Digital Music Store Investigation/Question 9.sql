SELECT a.Name , sum(il.UnitPrice * il.Quantity) as best_sale
FROM Artist as a
JOIN Album as al on a.ArtistId == al.ArtistId
JOIN Track as t on al.AlbumId == t.AlbumId
JOIN InvoiceLine as il on t.TrackId == il.TrackId
group by a.Name
ORDER by best_sale DESC
LIMIT 10