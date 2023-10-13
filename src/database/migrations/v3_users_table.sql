BEGIN;

-- Add the Users table
CREATE TABLE Users (
  address TINYTEXT NOT NULL,
  user_id CHAR(32) NOT NULL,
  name TEXT NOT NULL,

  CONSTRAINT PK_Users 
  PRIMARY KEY (user_id, address),

  CONSTRAINT FK_UsersAddress 
  FOREIGN KEY (address) REFERENCES Servers (address) 
  ON DELETE CASCADE
);

-- Create the new Tokens table, connected to Users
CREATE TABLE Tokens_NEW (
	address TINYTEXT NOT NULL,
	user_id CHAR(32) NOT NULL,
	token CHAR(32) NOT NULL,
	active BOOLEAN DEFAULT 0,
	
	CONSTRAINT PK_Tokens 
	PRIMARY KEY (address, user_id),
	
	CONSTRAINT FK_TokensServerAddress 
	FOREIGN KEY (address) REFERENCES Servers (address)
	ON DELETE CASCADE,

  CONSTRAINT FK_TokensUserId
  FOREIGN KEY (user_id) REFERENCES Users (user_id)
  ON DELETE CASCADE
);

-- Migrate the tokens
INSERT INTO Tokens_NEW SELECT * FROM Tokens;

-- Drop old token table
DROP TABLE Tokens;

-- Rename new tokens table
ALTER TABLE Tokens_NEW RENAME TO Tokens;

-- Update DB version
UPDATE Meta SET row_value = "v4" WHERE row_key = "version"; 

COMMIT;