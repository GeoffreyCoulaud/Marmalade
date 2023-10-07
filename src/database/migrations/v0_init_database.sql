-- Migration applied on top of version v0 (database was just created)

BEGIN;

-- Creating tables

CREATE TABLE Meta (
	row_key VARCHAR(64) NOT NULL,
	row_value TINYTEXT,
	CONSTRAINT PK_Meta PRIMARY KEY (row_key)
);

CREATE TABLE Servers (
	address TINYTEXT NOT NULL,
	name TINYTEXT NOT NULL,
	server_id CHAR(32) NOT NULL,
	CONSTRAINT PK_Servers PRIMARY KEY (address)
);

CREATE TABLE Tokens (
	address TINYTEXT NOT NULL,
	user_id CHAR(32) NOT NULL,
	token CHAR(32) NOT NULL,
	active BOOLEAN DEFAULT 0,
	CONSTRAINT PK_Tokens PRIMARY KEY (address, user_id),
	CONSTRAINT FK_TokensServerAddress FOREIGN KEY (address) REFERENCES Servers(address)
);

CREATE INDEX INDEX_active ON Tokens (active);

-- Inserting values

INSERT INTO Meta (row_key, row_value) VALUES ("version", "v1");

-- Finish

COMMIT;