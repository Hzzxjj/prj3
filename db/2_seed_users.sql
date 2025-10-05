-- Insert sample users
INSERT INTO users (id, joined_at) VALUES 
(1, '2024-01-15 10:30:00'),
(2, '2024-01-16 14:20:00'),
(3, '2024-01-17 09:15:00'),
(4, '2024-01-18 16:45:00'),
(5, '2024-01-19 11:30:00')
ON CONFLICT (id) DO NOTHING;