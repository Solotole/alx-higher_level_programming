-- script that creates the MySQL server user user_0d_1
-- does not fail if already exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
