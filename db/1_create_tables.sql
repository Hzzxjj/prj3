-- Create users table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    joined_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Create tokens table
CREATE TABLE IF NOT EXISTS tokens (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    used_at TIMESTAMP NULL
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_tokens_user_id ON tokens(user_id);
CREATE INDEX IF NOT EXISTS idx_tokens_created_at ON tokens(created_at);
CREATE INDEX IF NOT EXISTS idx_tokens_used_at ON tokens(used_at);