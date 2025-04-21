
## Conversion: test-oracle.sql → test-oracle.sql

**Oracle SQL:**
```sql
BEGIN
 
IF CheckObject('DEFAULT','TABLE','Z_PJPUPPSR_COMP') = '1' THEN
	EXECUTE IMMEDIATE 'DROP TABLE Z_PJPUPPSR_COMP CASCADE CONSTRAINTS';
END IF;
 
IF CheckObject('DEFAULT','TABLE','Z_PJPUPPSR_OC') = '1' THEN
	EXECUTE IMMEDIATE 'DROP TABLE Z_PJPUPPSR_OC CASCADE CONSTRAINTS';
END IF;
 
IF CheckObject('DEFAULT','TABLE','Z_PJPUPPSR_PROJ') = '1' THEN
	EXECUTE IMMEDIATE 'DROP TABLE Z_PJPUPPSR_PROJ CASCADE CONSTRAINTS';
END IF;
 
IF CheckObject('DEFAULT','TABLE','Z_PJPUPPSR_RND') = '1' THEN
	EXECUTE IMMEDIATE 'DROP TABLE Z_PJPUPPSR_RND CASCADE CONSTRAINTS';
END IF;
 
IF CheckObject('DEFAULT','TABLE','Z_PJPUPPSR_TEST_10') = '1' THEN
	EXECUTE IMMEDIATE 'DROP TABLE Z_PJPUPPSR_TEST_10 CASCADE CONSTRAINTS';
END IF;
 
INSERT INTO DB_TABLE_VERS ( TABLE_NAME, CUR_VERS_ID, CONV_DT, COMMENTS, CONV_CP_VERS_ID, MODIFIED_BY, TIME_STAMP, ROWVERSION ) 
VALUES ( 'dbc_820_11694', '8.2.0', SYSDATE, 'dbc_820_11694 has been applied.', ' ', 'DELTEK', SYSDATE, 0 );
 
COMMIT;
 
END;
```

**SQL Server:**
```sql
BEGIN
 
IF EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Z_PJPUPPSR_COMP]') AND type in (N'U'))
BEGIN
	DROP TABLE [dbo].[Z_PJPUPPSR_COMP]
END
 
IF EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Z_PJPUPPSR_OC]') AND type in (N'U'))
BEGIN
	DROP TABLE [dbo].[Z_PJPUPPSR_OC]
END
 
IF EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Z_PJPUPPSR_PROJ]') AND type in (N'U'))
BEGIN
	DROP TABLE [dbo].[Z_PJPUPPSR_PROJ]
END
 
IF EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Z_PJPUPPSR_RND]') AND type in (N'U'))
BEGIN
	DROP TABLE [dbo].[Z_PJPUPPSR_RND]
END
 
IF EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Z_PJPUPPSR_TEST_10]') AND type in (N'U'))
BEGIN
	DROP TABLE [dbo].[Z_PJPUPPSR_TEST_10]
END
 
INSERT INTO DB_TABLE_VERS ( TABLE_NAME, CUR_VERS_ID, CONV_DT, COMMENTS, CONV_CP_VERS_ID, MODIFIED_BY, TIME_STAMP, ROWVERSION ) 
VALUES ( 'dbc_820_11694', '8.2.0', GETDATE(), 'dbc_820_11694 has been applied.', ' ', 'DELTEK', GETDATE(), 0 );
 
COMMIT;
 
END
```

**Key Differences:**

| Feature/Function         | Oracle SQL Example                | SQL Server Equivalent         |
|------------------------- |-----------------------------------|------------------------------|
| Date/Time Functions      | SYSDATE                           | GETDATE()                    |
| Data Types               | NUMBER, VARCHAR2                  | INT, DECIMAL, VARCHAR        |
| NULL Handling            | NVL(expr1, expr2)                 | ISNULL(expr1, expr2)         |
| String Functions         | TO_CHAR(date, format)             | CONVERT(VARCHAR, date, style)|
| Sequences                | CREATE SEQUENCE ...               | IDENTITY or SEQUENCE         |
| Triggers                 | Oracle PL/SQL trigger syntax      | SQL Server T-SQL trigger     |
| PL/SQL Blocks            | BEGIN ... END;                    | BEGIN ... END                |
| Dual Table               | FROM DUAL                         | (No equivalent needed)       |

---
