CREATE TABLE IF NOT EXISTS currency(
    currency_id INTEGER PRIMARY KEY,
    currency TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS conversion(
    currency_id INTEGER,
    conversion_currency TEXT,
    FOREIGN KEY("currency_id") REFERENCES "currency"("currency_id")
);