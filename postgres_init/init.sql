CREATE TABLE my_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    value VARCHAR(255) NOT NULL
);

INSERT INTO my_table (name, value)
VALUES ('item1', 'value1'), ('item2', 'value2'), ('item3', 'value3');