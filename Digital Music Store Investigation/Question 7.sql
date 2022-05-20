SELECT a.ArtistId, a.Name,g.Name , count(a.ArtistId) as artist_number
from Artist a
JOIN Album al on a.ArtistId == al.ArtistId
JOIN Track t on al.AlbumId == t.AlbumId
join Genre g on t.GenreId == g.GenreId
where g.Name == 'Rock'
GROUP by a.Name
order by artist_number DESC
LIMIT 10