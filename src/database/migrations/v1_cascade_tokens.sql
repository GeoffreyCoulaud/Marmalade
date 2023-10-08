BEGIN;


-- Recreate a table with the new ON DELETE CASCADE foreign key
CREATE TABLE Tokens_NEW (
	address TINYTEXT NOT NULL,
	user_id CHAR(32) NOT NULL,
	token CHAR(32) NOT NULL,
	active BOOLEAN DEFAULT 0,
	
	CONSTRAINT PK_Tokens 
	PRIMARY KEY (address, user_id),
	
	CONSTRAINT FK_TokensServerAddress 
	FOREIGN KEY (address) REFERENCES Servers(address)
	ON DELETE CASCADE
);

-- Remove old table's additional index
DROP INDEX INDEX_active;

-- Create the new index on the new table
CREATE INDEX INDEX_tokens_active ON Tokens_NEW (active);

-- Copy data to the new table
INSERT INTO Tokens_NEW SELECT * FROM Tokens;

-- Remove the old table
DROP TABLE Tokens;

-- Rename new table to old name
ALTER TABLE Tokens_NEW RENAME TO Tokens;

-- Update DB version
UPDATE Meta SET row_value = "v2" WHERE row_key = "version"; 

COMMIT;