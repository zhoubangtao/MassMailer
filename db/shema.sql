
CREATE TABLE smtp_accounts
(
  id             INTEGER PRIMARY KEY NOT NULL,
  name           TEXT                NOT NULL,
  password       TEXT                NOT NULL,
  enable         BOOLEAN DEFAULT TRUE NOT NULL,
  smtp_server_id INTEGER             NOT NULL
);

CREATE TABLE smtp_servers
(
  id                INTEGER PRIMARY KEY NOT NULL,
  name              TEXT                NOT NULL,
  host              TEXT                NOT NULL,
  port              INTEGER             NOT NULL,
  postfix           TEXT                NOT NULL,
  limit_per_day     INTEGER,
  limit_per_hour    INTEGER,
  limit_per_ip      INTEGER,
  limit_per_account INTEGER,
  enable            BOOLEAN DEFAULT TRUE NOT NULL,
  create_at         DATETIME            NOT NULL,
  update_at         DATETIME
);

CREATE UNIQUE INDEX name_index ON smtp_servers (name);
