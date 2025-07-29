-- Creates the 'users' table with unique constraint and auto-incremented
-- Ensures email uniqueness and prevents the script from failing
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
);
