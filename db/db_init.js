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
