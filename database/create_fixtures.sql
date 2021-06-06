CREATE TABLE IF NOT EXISTS Writer 
(
    id SERIAL PRIMARY KEY,
    name CHARACTER VARYING(50)
);

CREATE TABLE IF NOT EXISTS Book 
(
    id SERIAL PRIMARY KEY,
    author_id INTEGER REFERENCES Writer (id),
    name CHARACTER VARYING(50),
    data_json jsonb 
);