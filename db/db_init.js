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

db.createCollection("currency")

db.currency_rates.createIndex({"date_published": -1, "code": 1})
