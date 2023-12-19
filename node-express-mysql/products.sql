-- User Table
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
);

-- Product Table
CREATE TABLE product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Order Table
CREATE TABLE `order` (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('pending', 'completed', 'cancelled') NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id)
);

-- Order Details Table
CREATE TABLE order_details (
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES `order`(id),
    FOREIGN KEY (product_id) REFERENCES product(id),
    PRIMARY KEY (order_id, product_id)
);

INSERT INTO user (username, password, name, age, email) VALUES
('john_doe', 'password123', 'John Doe', 30, 'john.doe@example.com'),
('jane_doe', 'password123', 'Jane Doe', 28, 'jane.doe@example.com'),
('mike_smith', 'password123', 'Mike Smith', 35, 'mike.smith@example.com'),
('sarah_jones', 'password123', 'Sarah Jones', 26, 'sarah.jones@example.com'),
('william_brown', 'password123', 'William Brown', 40, 'william.brown@example.com'),
('emma_wilson', 'password123', 'Emma Wilson', 22, 'emma.wilson@example.com'),
('olivia_taylor', 'password123', 'Olivia Taylor', 24, 'olivia.taylor@example.com'),
('mason_lee', 'password123', 'Mason Lee', 31, 'mason.lee@example.com'),
('ella_davis', 'password123', 'Ella Davis', 29, 'ella.davis@example.com'),
('james_white', 'password123', 'James White', 27, 'james.white@example.com');

INSERT INTO product (name, description, price, stock) VALUES
('Laptop', 'High performance laptop', 999.99, 50),
('Smartphone', 'Latest Android smartphone', 499.99, 75),
('Headphones', 'Noise-cancelling headphones', 199.99, 100),
('Smartwatch', 'Waterproof smartwatch', 299.99, 80),
('Backpack', 'Durable travel backpack', 59.99, 150),
('Camera', 'Digital SLR camera', 849.99, 30),
('Tablet', '10-inch tablet with WiFi', 399.99, 60),
('Keyboard', 'Mechanical gaming keyboard', 129.99, 90),
('Mouse', 'Wireless Bluetooth mouse', 49.99, 110),
('Monitor', '27-inch 4K UHD monitor', 349.99, 40);


INSERT INTO `order` (user_id, total_price, status) VALUES
(1, 1249.98, 'completed'),
(2, 499.99, 'pending'),
(3, 349.99, 'completed'),
(4, 199.99, 'cancelled'),
(5, 1299.98, 'pending'),
(6, 399.99, 'completed'),
(7, 449.98, 'completed'),
(8, 999.99, 'pending'),
(9, 899.98, 'cancelled'),
(10, 549.98, 'completed');


INSERT INTO order_details (order_id, product_id, quantity, price) VALUES
(1, 1, 1, 999.99),
(2, 2, 1, 499.99),
(3, 5, 1, 59.99),
(4, 3, 1, 199.99),
(5, 1, 1, 999.99),
(6, 6, 1, 399.99),
(7, 4, 1, 299.99),
(8, 1, 1, 999.99),
(9, 7, 1, 399.99),
(10, 2, 1, 499.99);
