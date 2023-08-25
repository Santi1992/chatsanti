CREATE TABLE users (
    id VARCHAR(36) PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    CONSTRAINT uk_username UNIQUE (username)
);

INSERT INTO users (id, username)
VALUES ('a3d6b11a-60a1-4b42-ba0d-e5f68e54a04d', 'santiRueda');

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(36) REFERENCES users(id),
    ammount NUMERIC NOT NULL,
    date_transaction TIMESTAMP NOT NULL
);
