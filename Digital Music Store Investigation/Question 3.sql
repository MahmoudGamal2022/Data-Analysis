SELECT BillingCountry , sum(total) as Seles
from Invoice
GROUP by BillingCountry
ORDER by Seles DESC
