SELECT BillingCountry , count(BillingCountry) as Invoices
from Invoice
GROUP by BillingCountry
ORDER by Invoices DESC
