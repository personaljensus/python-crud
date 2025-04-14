SELECT * FROM pg_stat_activity WHERE datname = 'dummy_database';
DROP DATABASE IF EXISTS dummy_database;
CREATE DATABASE dummy_database;
