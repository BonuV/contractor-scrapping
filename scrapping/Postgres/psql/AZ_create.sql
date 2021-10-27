CREATE TABLE arizona_contactors(
    License_no  NUMERIC(10) UNIQUE NOT NULL,
    Business_name VARCHAR (200) NOT NULL,
    doing_business_as VARCHAR (200) ,
    Address VARCHAR(200),
    Address2 VARCHAR(40),
    City VARCHAR(15) ,
    State VARCHAR(2) ,
    ZIP  VARCHAR(11) ,
    Qualifying_party VARCHAR(50) ,
    Class VARCHAR(6) NOT NULL,
    Class_Detail VARCHAR(80) NOT NULL,
    Class_Type VARCHAR(15) NOT NULL,
    Issued_date DATE NOT NULL,
    Expiration_date DATE,
    Status VARCHAR(10) NOT NULL
);