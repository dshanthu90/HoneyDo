CREATE TABLE honey_comb(
    honey_comb_id INTEGER PRIMARY KEY AUTOINCREMENT,
    honey_comb_name TEXT  NOT NULL
);

CREATE TABLE user_table(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT NOT NULL,
    comb_id INTEGER NOT NULL,
    FOREIGN KEY (comb_id) REFERENCES honey_comb (honey_comb_id)
);

CREATE TABLE task_list(
    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_detail TEXT NOT NULL,
    task_due DATE,
    task_created_by INTEGER, NOT NULL,
    task_assigned INTEGER NOT NULL,
    task_status INTEGER CHECK (task_status =0 or task_status=1)
)
