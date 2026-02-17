SELECT customers.name AS 'Customers' 
FROM Customers
WHERE customers.id NOT IN
(
    select customerId FROM Orders
);