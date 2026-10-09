import os

import psycopg2 # type: ignore
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from Jenkins EC2 CI/CD!"


@app.route("/db-test")
def db_test():
    connection = psycopg2.connect(
        host=os.environ["DB_HOST"],
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS flask_test (
            id SERIAL PRIMARY KEY,
            message TEXT NOT NULL
        )
        """
    )

    cursor.execute(
        """
        INSERT INTO flask_test (message)
        VALUES (%s)
        RETURNING id
        """,
        ("Hello from the Flask container",),
    )

    inserted_id = cursor.fetchone()[0]
    connection.commit()

    cursor.execute(
        "SELECT id, message FROM flask_test WHERE id = %s",
        (inserted_id,),
    )

    row = cursor.fetchone()

    cursor.close()
    connection.close()

    return f"Inserted and read row: id={row[0]}, message={row[1]}"

@app.route("/health")
def health():
    return "healthy", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)