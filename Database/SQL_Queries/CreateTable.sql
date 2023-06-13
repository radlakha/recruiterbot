CREATE TABLE chatHistory1(
Chat_ID INT IDENTITY(1,1) PRIMARY KEY,
Chat_Sender varchar(200),
Chat_Message varchar(max),
CONSTRAINT checkSender1 CHECK (Chat_Sender IN ('AI', 'Human')),
Creation_Time DATETIME DEFAULT CURRENT_TIMESTAMP
)