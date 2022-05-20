select al.AlbumId, al.Title ,SUM(il.unitprice * il.quantity) as top_album
from Album al
JOIN Track t on al.AlbumId == t.AlbumId
join InvoiceLine il on  t.TrackId == il.TrackId 
GROUP by al.Title
order by top_album DESC
LIMIT 10
