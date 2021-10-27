CREATE TABLE nashville_contactors(
    Company_name  NUMERIC(10) UNIQUE NOT NULL,
    Profession_type VARCHAR (150) NOT NULL,
    Address VARCHAR (150) ,
    City VARCHAR(40) ,
    State VARCHAR(2) ,
    ZIP  VARCHAR(11) ,
    Phone VARCHAR(15) NOT NULL,
    Fax VARCHAR(15),
    Alternate_phone VARCHAR(15) ,
    Email VARCHAR(50) ,
    Last_permit_date DATE ,
    Mapped_location VARCHAR(50)
);

ALTER TABLE arizona_contactors ADD PRIMARY KEY (license_no);

