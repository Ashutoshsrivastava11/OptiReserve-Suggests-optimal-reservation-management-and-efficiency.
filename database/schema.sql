-- Drop existing tables if they exist (useful for development/testing)
DROP TABLE IF EXISTS reservations CASCADE;
DROP TABLE IF EXISTS users CASCADE;

-- Create 'users' table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create 'reservations' table
CREATE TABLE reservations (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    reservation_date DATE NOT NULL,
    status VARCHAR(50) CHECK (status IN ('confirmed', 'canceled', 'pending')) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_reservation_user_id ON reservations(user_id);
CREATE INDEX idx_reservation_date ON reservations(reservation_date);

-- Example data insertion (optional, for initial testing)
INSERT INTO users (name, email) VALUES
('Alice', 'alice@example.com'),
('Bob', 'bob@example.com');

INSERT INTO reservations (user_id, reservation_date, status) VALUES
(1, '2024-09-01', 'confirmed'),
(2, '2024-09-02', 'canceled');
