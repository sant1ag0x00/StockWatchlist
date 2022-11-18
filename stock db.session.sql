SELECT u.id,
    s.Sector,
    s.Name
    FROM User u
    INNER JOIN user_stock AS us ON u.id = us.user_id
    INNER JOIN stocks s on us.stock_symbol = s.Symbol
WHERE u.name = 'Robert'