ora-dblink-password-decrypter
=============================

Tool to decrypt database link passwords in Oracle 10g/11g

**Usage instructions**

Run the following query against the database (obviously you need to have select privilege on link$ or be SYS)

```sql
select userid, passwordx from sys.link$;

| USERID   | PASSWORDX**                                       |
|--------- | --------------------------------------------------|
| django   | 050E1146FB18E013A378432A39171BC64D70B3BF2F671C9B16|
```

**usage()**

oraDBLinkPassDecrypter.py takes two arguments

- Oracle Database version, 11 for 11g and 12 for 12c
- USERID:PASSWORDX comes from the select query above

oraDBLinkPassDecrypter.py 11|12 USERID:PASSWORDX

```python
python oraDbLinkPassDecrypt.py 11 django:050E1146FB18E013A378432A39171BC64D70B3BF2F671C9B16
```

**Decrypted password of django is djangotest321**
