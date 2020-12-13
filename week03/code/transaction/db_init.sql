CREATE TABLE IF NOT EXISTS `user`
(
ID          INTEGER         NOT NULL,
user_name   NVARCHAR(255)   NOT NULL,
PRIMARY KEY (ID)
);

CREATE TABLE IF NOT EXISTS `account`
(
ID          INTEGER     NOT NULL,
amount      INTEGER     NOT NULL    DEFAULT(0),
PRIMARY KEY (ID)
);

CREATE TABLE IF NOT EXISTS `audit`
(
ID          INTEGER     NOT NULL    AUTO_INCREMENT,
user_in     INTEGER     NOT NULL,
user_out    INTEGER     NOT NULL,
amount      INTEGER     NOT NULL,
createtime  TIMESTAMP   NOT NULL    DEFAULT now(),          
PRIMARY KEY (ID)
);

INSERT INTO `user` (ID, user_name) VALUES (1, '张三');
INSERT INTO `account` (ID) VALUES (1);

INSERT INTO `user` (ID, user_name) VALUES (2, '李四');
INSERT INTO `account` (ID) VALUES (2);


