ora-dblink-password-decrypter
=============================

Tool to decrypt database link passwords in Oracle 10g/11g

Usage instructions

Run the following query against the database (obviously you need to have select privilege on link$ or be SYS)

select userid||':'||passwordx from sys.link$;

userid||':'||passwordx

django:050E1146FB18E013A378432A39171BC64D70B3BF2F671C9B16

Feed this output 

python oraDbLinkPassDecrypt.py 11 django:050E1146FB18E013A378432A39171BC64D70B3BF2F671C9B16
Decrypted password of django is djangotest321
