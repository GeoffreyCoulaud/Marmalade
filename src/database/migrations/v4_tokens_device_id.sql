BEGIN;

-- ! This migration drops all stored access tokens

-- Drop old token table
DROP TABLE Tokens;

-- Recreate the tokens table, with mandatory device id
CREATE TABLE Tokens (
	address TINYTEXT NOT NULL,
	user_id CHAR(32) NOT NULL,
  device_id TINYTEXT NOT NULL,
	token CHAR(32) NOT NULL,
	active BOOLEAN DEFAULT 0,
	
	CONSTRAINT PK_Tokens 
	PRIMARY KEY (address, user_id),
	
  CONSTRAINT UC_TokensDeviceId
  UNIQUE (device_id),

	CONSTRAINT FK_TokensServerAddress 
	FOREIGN KEY (address) REFERENCES Servers (address)
	ON DELETE CASCADE,

  CONSTRAINT FK_TokensUserId
  FOREIGN KEY (user_id) REFERENCES Users (user_id)
  ON DELETE CASCADE
);

-- Update DB version
UPDATE Meta SET row_value = "v5" WHERE row_key = "version"; 

COMMIT;