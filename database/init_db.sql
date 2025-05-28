CREATE TABLE products (
    product_id TEXT PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    cost REAL NOT NULL
);

CREATE TABLE regions (
    region_id TEXT PRIMARY KEY,
    region_name TEXT NOT NULL,
    country TEXT NOT NULL
);

CREATE TABLE customers (
    customer_id TEXT PRIMARY KEY,
    customer_name TEXT NOT NULL,
    region_id TEXT NOT NULL,
    segment TEXT NOT NULL,
    FOREIGN KEY (region_id) REFERENCES regions(region_id)
);

CREATE TABLE sales (
    sale_id TEXT PRIMARY KEY,
    date TEXT NOT NULL,
    customer_id TEXT NOT NULL,
    product_id TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    revenue REAL NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert sample data for products
INSERT INTO products VALUES ('P001', 'Product A', 'Electronics', 1200.00, 800.00);
INSERT INTO products VALUES ('P002', 'Product B', 'Electronics', 1500.00, 1000.00);
INSERT INTO products VALUES ('P003', 'Product C', 'Furniture', 350.00, 200.00);
INSERT INTO products VALUES ('P004', 'Product D', 'Office Supplies', 25.00, 15.00);
INSERT INTO products VALUES ('P005', 'Product E', 'Furniture', 450.00, 300.00);

-- Insert sample data for regions
INSERT INTO regions VALUES ('R001', 'North America', 'USA');
INSERT INTO regions VALUES ('R002', 'Europe', 'Germany');
INSERT INTO regions VALUES ('R003', 'Asia Pacific', 'Japan');
INSERT INTO regions VALUES ('R004', 'Latin America', 'Brazil');
INSERT INTO regions VALUES ('R005', 'Middle East', 'UAE');

-- Insert sample data for customers
INSERT INTO customers VALUES ('C001', 'Customer 1', 'R001', 'Corporate');
INSERT INTO customers VALUES ('C002', 'Customer 2', 'R001', 'Consumer');
INSERT INTO customers VALUES ('C003', 'Customer 3', 'R002', 'Corporate');
INSERT INTO customers VALUES ('C004', 'Customer 4', 'R003', 'Consumer');
INSERT INTO customers VALUES ('C005', 'Customer 5', 'R002', 'Corporate');
INSERT INTO customers VALUES ('C006', 'Customer 6', 'R004', 'Consumer');
INSERT INTO customers VALUES ('C007', 'Customer 7', 'R005', 'Corporate');
INSERT INTO customers VALUES ('C008', 'Customer 8', 'R003', 'Consumer');
INSERT INTO customers VALUES ('C009', 'Customer 9', 'R004', 'Corporate');
INSERT INTO customers VALUES ('C010', 'Customer 10', 'R005', 'Consumer');

-- Insert sample data for sales (last 6 months)
-- November 2024
INSERT INTO sales VALUES ('S001', '2024-11-01', 'C001', 'P001', 5, 6000.00);
INSERT INTO sales VALUES ('S002', '2024-11-05', 'C002', 'P002', 3, 4500.00);
INSERT INTO sales VALUES ('S003', '2024-11-10', 'C003', 'P003', 10, 3500.00);
INSERT INTO sales VALUES ('S004', '2024-11-15', 'C004', 'P004', 20, 500.00);
INSERT INTO sales VALUES ('S005', '2024-11-20', 'C005', 'P005', 8, 3600.00);
INSERT INTO sales VALUES ('S006', '2024-11-25', 'C006', 'P001', 4, 4800.00);
INSERT INTO sales VALUES ('S007', '2024-11-30', 'C007', 'P002', 2, 3000.00);

-- December 2024
INSERT INTO sales VALUES ('S008', '2024-12-03', 'C008', 'P003', 12, 4200.00);
INSERT INTO sales VALUES ('S009', '2024-12-08', 'C009', 'P004', 30, 750.00);
INSERT INTO sales VALUES ('S010', '2024-12-12', 'C010', 'P005', 6, 2700.00);
INSERT INTO sales VALUES ('S011', '2024-12-15', 'C001', 'P001', 3, 3600.00);
INSERT INTO sales VALUES ('S012', '2024-12-18', 'C002', 'P002', 5, 7500.00);
INSERT INTO sales VALUES ('S013', '2024-12-22', 'C003', 'P003', 8, 2800.00);
INSERT INTO sales VALUES ('S014', '2024-12-27', 'C004', 'P004', 15, 375.00);

-- January 2025
INSERT INTO sales VALUES ('S015', '2025-01-02', 'C005', 'P005', 10, 4500.00);
INSERT INTO sales VALUES ('S016', '2025-01-07', 'C006', 'P001', 6, 7200.00);
INSERT INTO sales VALUES ('S017', '2025-01-12', 'C007', 'P002', 4, 6000.00);
INSERT INTO sales VALUES ('S018', '2025-01-17', 'C008', 'P003', 15, 5250.00);
INSERT INTO sales VALUES ('S019', '2025-01-22', 'C009', 'P004', 25, 625.00);
INSERT INTO sales VALUES ('S020', '2025-01-27', 'C010', 'P005', 7, 3150.00);

-- February 2025
INSERT INTO sales VALUES ('S021', '2025-02-01', 'C001', 'P001', 8, 9600.00);
INSERT INTO sales VALUES ('S022', '2025-02-06', 'C002', 'P002', 6, 9000.00);
INSERT INTO sales VALUES ('S023', '2025-02-11', 'C003', 'P003', 20, 7000.00);
INSERT INTO sales VALUES ('S024', '2025-02-16', 'C004', 'P004', 40, 1000.00);
INSERT INTO sales VALUES ('S025', '2025-02-21', 'C005', 'P005', 12, 5400.00);
INSERT INTO sales VALUES ('S026', '2025-02-26', 'C006', 'P001', 5, 6000.00);

-- March 2025
INSERT INTO sales VALUES ('S027', '2025-03-03', 'C007', 'P002', 7, 10500.00);
INSERT INTO sales VALUES ('S028', '2025-03-08', 'C008', 'P003', 18, 6300.00);
INSERT INTO sales VALUES ('S029', '2025-03-13', 'C009', 'P004', 35, 875.00);
INSERT INTO sales VALUES ('S030', '2025-03-18', 'C010', 'P005', 9, 4050.00);
INSERT INTO sales VALUES ('S031', '2025-03-23', 'C001', 'P001', 10, 12000.00);
INSERT INTO sales VALUES ('S032', '2025-03-28', 'C002', 'P002', 8, 12000.00);

-- April 2025
INSERT INTO sales VALUES ('S033', '2025-04-02', 'C003', 'P003', 25, 8750.00);
INSERT INTO sales VALUES ('S034', '2025-04-07', 'C004', 'P004', 50, 1250.00);
INSERT INTO sales VALUES ('S035', '2025-04-12', 'C005', 'P005', 15, 6750.00);
INSERT INTO sales VALUES ('S036', '2025-04-17', 'C006', 'P001', 12, 14400.00);
INSERT INTO sales VALUES ('S037', '2025-04-22', 'C007', 'P002', 9, 13500.00);
INSERT INTO sales VALUES ('S038', '2025-04-27', 'C008', 'P003', 22, 7700.00);

-- May 2025
INSERT INTO sales VALUES ('S039', '2025-05-02', 'C009', 'P004', 45, 1125.00);
INSERT INTO sales VALUES ('S040', '2025-05-07', 'C010', 'P005', 11, 4950.00);
INSERT INTO sales VALUES ('S041', '2025-05-12', 'C001', 'P001', 15, 18000.00);
INSERT INTO sales VALUES ('S042', '2025-05-17', 'C002', 'P002', 10, 15000.00);
INSERT INTO sales VALUES ('S043', '2025-05-22', 'C003', 'P003', 30, 10500.00);
INSERT INTO sales VALUES ('S044', '2025-05-27', 'C004', 'P004', 60, 1500.00);
