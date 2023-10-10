BEGIN; 

-- Adds created_timestamp and connected_timestamp columns to Servers.

-- Since SQLite doesn't support adding columns with default values that are CURRENT_TIMESTAMP
-- we need to recreate a table and migrate to it.
-- We also need to recreate the tokens table, since sqlite doesn't support dropping foreign keys.

-- Create the new Servers table
CREATE TABLE Servers_NEW (
	address TINYTEXT NOT NULL,
	name TINYTEXT NOT NULL,
	server_id CHAR(32) NOT NULL,
	created_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	connected_timestamp TIMESTAMP DEFAULT NULL,
	CONSTRAINT PK_Servers PRIMARY KEY (address)
);

-- Recreate the new connected Tokens table
CREATE TABLE Tokens_NEW (
	address TINYTEXT NOT NULL,
	user_id CHAR(32) NOT NULL,
	token CHAR(32) NOT NULL,
	active BOOLEAN DEFAULT 0,
	
	CONSTRAINT PK_Tokens 
	PRIMARY KEY (address, user_id),
	
	CONSTRAINT FK_TokensServerAddress 
	FOREIGN KEY (address) REFERENCES Servers_NEW (address)
	ON DELETE CASCADE
);

-- Migrate the data
INSERT INTO Servers_NEW (address, name, server_id) SELECT address, name, server_id FROM Servers;
INSERT INTO Tokens_NEW SELECT * FROM Tokens;

-- Drop old tables
DROP TABLE Servers;
DROP TABLE Tokens;

-- Rename new tables
ALTER TABLE Servers_NEW RENAME TO Servers;
ALTER TABLE Tokens_NEW RENAME TO Tokens;

-- Update DB version
UPDATE Meta SET row_value = "v3" WHERE row_key = "version"; 

COMMIT;