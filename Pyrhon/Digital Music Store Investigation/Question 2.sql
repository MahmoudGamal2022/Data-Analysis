SELECT DISTINCT c.Email, c.FirstName, c.LastName,g.Name
from Customer c
JOIN Invoice i , InvoiceLine il , Track t, Genre g
ON c.CustomerId == i.CustomerId and i.InvoiceId == il.InvoiceId and il.TrackId == t.TrackId and t.GenreId == g.GenreId
WHERE g.Name == 'Rock'
ORDER by c.Email