db.createUser(
    {
        user: "fastapi",
        pwd: "password12345",
        roles: [
            {role: "readWrite",
            db: "currency_api"}
        ]
    }
)

db.createCollection("currency_tables")
db.createCollection("currency_rates")

db.currency_tables.createIndex({"table_type": 1, "date_published": -1})
db.currency_rates.createIndex({"table_id": -1, "date_published": -1})
