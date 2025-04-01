-- Создание таблицы агентов
CREATE TABLE agents (
    id SERIAL PRIMARY KEY,
    company_name VARCHAR,
    type VARCHAR,
    legal_address VARCHAR,
    inn VARCHAR,
    kpp VARCHAR,
    director_name VARCHAR,
    contact_phone VARCHAR,
    contact_email VARCHAR,
    logo_url VARCHAR,
    priority INT,
    sales_history TEXT
);

-- Заявки агентов
CREATE TABLE agent_orders (
    id SERIAL PRIMARY KEY,
    agent_id INT REFERENCES agents(id) ON DELETE CASCADE,
    order_date TIMESTAMP,
    status VARCHAR
);

-- Продукция
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    article VARCHAR,
    name VARCHAR,
    type VARCHAR,
    image_url VARCHAR,
    min_price NUMERIC,
    packaging VARCHAR,
    certificates TEXT,
    standard_number VARCHAR,
    workshop VARCHAR
);

-- Связь заявки с продукцией (многие ко многим)
CREATE TABLE agent_order_products (
    order_id INT REFERENCES agent_orders(id) ON DELETE CASCADE,
    product_id INT REFERENCES products(id) ON DELETE CASCADE,
    quantity INT,
    PRIMARY KEY (order_id, product_id)
);

-- Материалы
CREATE TABLE materials (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    type VARCHAR,
    units_per_pack INT,
    unit VARCHAR,
    stock_qty INT,
    min_stock INT,
    cost NUMERIC,
    image_url VARCHAR,
    description TEXT,
    stock_history TEXT
);

-- Поставщики
CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    inn VARCHAR,
    type VARCHAR,
    supply_history TEXT,
    quality_score INT
);

-- Связь материалов и поставщиков (многие ко многим)
CREATE TABLE material_supplier (
    material_id INT REFERENCES materials(id) ON DELETE CASCADE,
    supplier_id INT REFERENCES suppliers(id) ON DELETE CASCADE,
    PRIMARY KEY (material_id, supplier_id)
);

-- Сотрудники
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR,
    birth_date DATE,
    passport_data TEXT,
    bank_details TEXT,
    work_schedule TEXT,
    workshop VARCHAR,
    specialization VARCHAR,
    health_notes TEXT
);
