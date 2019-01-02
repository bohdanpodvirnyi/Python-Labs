CREATE DATABASE IF NOT EXISTS FamilyBudget;

CREATE TABLE IF NOT EXISTS FamilyBudget.family(
family_id INT UNSIGNED NOT NULL auto_increment,
PRIMARY KEY(family_id)
);

CREATE TABLE IF NOT EXISTS FamilyBudget.user(
user_id INT UNSIGNED NOT NULL auto_increment,
family_id INT UNSIGNED NOT NULL,
name VARCHAR(256) NOT NULL,
surname VARCHAR(256) NOT NULL,
PRIMARY KEY(user_id),
CONSTRAINT user_family FOREIGN KEY(family_id)
REFERENCES FamilyBudget.family(family_id)
ON DELETE NO ACTION ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS FamilyBudget.personal_account(
pa_id INT UNSIGNED NOT NULL auto_increment,
u_id INT UNSIGNED NOT NULL,
sum INT UNSIGNED NULL,
PRIMARY KEY(pa_id),
CONSTRAINT user_pa FOREIGN KEY(u_id)
REFERENCES FamilyBudget.user(user_id)
ON DELETE NO ACTION ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS FamilyBudget.family_account(
fa_id INT UNSIGNED NOT NULL auto_increment,
family_id INT UNSIGNED NOT NULL,
sum INT UNSIGNED NULL,
PRIMARY KEY(fa_id),
CONSTRAINT user_fa FOREIGN KEY(family_id)
REFERENCES FamilyBudget.family(family_id)
ON DELETE NO ACTION ON UPDATE NO ACTION
);

DROP PROCEDURE IF EXISTS FamilyBudget.getAllUsers;
CREATE PROCEDURE FamilyBudget.getAllUsers ()
  BEGIN
    select name, surname from user;
  end;
  
DROP PROCEDURE IF EXISTS FamilyBudget.getFamilyMemers;
CREATE PROCEDURE FamilyBudget.getFamilyMembers (IN fam_id INT)
  BEGIN
    select name, surname from User
    where family_id=fam_id;
  end; 

DROP PROCEDURE IF EXISTS FamilyBudget.getFamilyAccount;
CREATE PROCEDURE FamilyBudget.getFamilyAccount (IN u_id INT)
  BEGIN
    select fa_id, sum from family_account
  where family_account.family_id = (select family.family_id from family INNER JOIN user
        ON family.family_id=user.family_id
        where user.user_id = u_id);
  end;
  
DROP PROCEDURE IF EXISTS FamilyBudget.getPersonalAccount;
CREATE PROCEDURE FamilyBudget.getPersonalAccount (IN u_id INT)
  BEGIN
    select pa_id, sum from personal_account
  where personal_account.u_id = u_id;
  end;
  
DROP PROCEDURE IF EXISTS FamilyBudget.addMoneyToFamilyAccount;
CREATE PROCEDURE FamilyBudget.addMoneyToFamilyAccount (IN u_id INT, money INT)
  BEGIN
    update family_account set sum=sum+money
  where family_account.family_id = (select family.family_id from family INNER JOIN user
        ON family.family_id=user.family_id
        where user.user_id = u_id);
  end;
  
DROP PROCEDURE IF EXISTS FamilyBudget.fromFamilyToPersonal;
CREATE PROCEDURE FamilyBudget.fromFamilyToPersonal (IN u_id INT, money INT)
  BEGIN
    update family_account set sum=sum-money
    where family_account.family_id = (select family.family_id from family INNER JOIN user
        ON family.family_id=user.family_id
        where user.user_id = u_id);
    update personal_account set sum=sum+money
    where personal_account.u_id = u_id);
  end;
  
DROP PROCEDURE IF EXISTS FamilyBudget.loginUser;
CREATE PROCEDURE FamilyBudget.loginUser (IN s_name VARCHAR(256), s_surname VARCHAR(256))
  BEGIN
    select user_id from user 
    where name = s_name
    AND surname = s_surname;
  end;