/*股票信息数据库DDL脚本*/

/*创建数据库*/

CREATE DATABASE IF NOT EXISTS CHINAEASTERN;


use CHINAEASTERN;

DROP TABLE IF EXISTS HistoricalQuote;

DROP TABLE IF EXISTS Stocks;

CREATE TABLE HistoricalQuote(
HDate date not null,
Open decimal(8,4),
High decimal(8,4),
Low decimal(8,4),
Close decimal(8,4),
Change varchar(10),
Chg varchar(10),
Volume bigint,
Turnover bigint,
Amplitude varchar(10),
TurnoverRate varchar(10),
Symbol varchar(10),
primary key(Date)
);

CREATE TABLE Stocks(
Symbol varchar(10) not null,
Company varchar(50) not null,
Industry varchar(10) not null,
primary key(Symbol)
);

ALTER TABLE HistoricalQuote ADD CONSTRAINT FK_Reference_1 FOREIGN KEY(Symbol)  
REFERENCES Stocks(Symbol) ON DELETE RESTRICT ON UPDATE RESTRICT;

INSERT INTO STOCKS(Symbol,Company,Industry)  VALUES('CEA','ChinaEastern','Transport');


 