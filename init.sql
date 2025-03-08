CREATE DATABASE IF NOT EXISTS testdb;
USE testdb;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE usersheader (header VARCHAR(100));

INSERT INTO users (name, email) VALUES
('Babita', 'Babita@example.com'),
('jethalal', 'jethalal@example.com');
INSERT INTO usersheader(header) VALUES ('JAYESH-MORE');
