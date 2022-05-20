SELECT  g.Name , count(a.ArtistId) as artist_number
from Artist a
JOIN Album al on a.ArtistId == al.ArtistId
JOIN Track t on al.AlbumId == t.AlbumId
join Genre g on t.GenreId == g.GenreId
GROUP by g.Name
order by artist_number DESC

