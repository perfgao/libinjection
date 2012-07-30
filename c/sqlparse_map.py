#!/usr/bin/env python

#
#  Copyright 2012, Nick Galbreath
#  nickg@client9.com
#  GPL v2 License -- Commericial Licenses available.
#  http://www.gnu.org/licenses/gpl-2.0.txt
#

keywords = dict({
'UTL_INADDR.GET_HOST_ADDRESS': 'f',

# http://blog.red-database-security.com/2009/01/17/tutorial-oracle-sql-injection-in-webapps-part-i/print/
'DBMS_PIPE.RECEIVE_MESSAGE':   'f',
'CTXSYS.DRITHSX.SN': 'f',
'SYS.STRAGG': 'f',
'ABS'                         : 'f',
'ACCESSIBLE'                  : 'k',
'ACOS'                        : 'f',
'ADD'                         : 'k',
'ADDDATE'                     : 'f',
'ADDTIME'                     : 'f',
'AES_DECRYPT'                 : 'f',
'AES_ENCRYPT'                 : 'f',
'AGAINST'                     : 'k',
'ALTER'                       : 'k',
'ALL_USERS'                   : 'k', # oracle
'ANALYZE'                     : 'k',
'AND'                         : '&',
'AS'                          : 'k',
'ASC'                         : 'k',
'ASCII'                       : 'f',
'ASENSITIVE'                  : 'k',
'ASIN'                        : 'f',
'ATAN'                        : 'f',
'ATAN2'                       : 'f',
'AVG'                         : 'f',
'BEFORE'                      : 'k',
'BEGIN'                       : 'k',
'BENCHMARK'                   : 'f',
'BETWEEN'                     : 'k',
'BIGINT'                      : 'k',
'BINARY'                      : 'k',
'BINBINARY'                   : 'f',
'BIT_AND'                     : 'f',
'BIT_COUNT'                   : 'f',
'BIT_LENGTH'                  : 'f',
'BIT_OR'                      : 'f',
'BIT_XOR'                     : 'f',
'BLOB'                        : 'k',
'BOOLEAN'                     : 'k',
'BOTH'                        : 'k',
'BY'                          : 'n',
'CALL'                        : 'k',
'CASCADE'                     : 'k',
'CASE'                        : 'o',
'CAST'                        : 'f',
'CEIL'                        : 'f',
'CEILING'                     : 'f',
'CHANGE'                      : 'k',
# sometimes a function too
'CHAR'                        : 'k',

'CHARACTER'                   : 'k',
'CHARACTER_LENGTH'            : 'f',
'CHARSET'                     : 'f',
'CHAR_LENGTH'                 : 'f',
'CHECK'                       : 'k',
'CHR'                         : 'f',
'COALESCE'                    : 'k',
'COERCIBILITY'                : 'f',
'COLLATE'                     : 'k',
'COLLATION'                   : 'f',
'COLUMN'                      : 'k',
'COMPRESS'                    : 'f',
'CONCAT'                      : 'f',
'CONCAT_WS'                   : 'f',
'CONDITION'                   : 'k',
'CONNECTION_ID'               : 'f',
'CONSTRAINT'                  : 'k',
'CONTINUE'                    : 'k',
'CONV'                        : 'f',
'CONVERT'                     : 'f',
'CONVERT_TZ'                  : 'f',
'COS'                         : 'f',
'COT'                         : 'f',
'COUNT'                       : 'f',
'CRC32'                       : 'f',
'CREATE'                      : 'k',
'CURDATE'                     : 'f',
'CURRENT_DATE'                : 'k',
'CURRENT_DATECURRENT_TIME'    : 'f',
'CURRENT_TIME'                : 'k',
'CURRENT_TIMESTAMP'           : 'k',
'CURRENT_USER'                : 'k',
'CURSOR'                      : 'k',
'CURTIME'                     : 'f',
'DATABASE'                    : 'k',
'DATABASES'                   : 'k',
'DATE'                        : 'f',
'DATEDIFF'                    : 'f',
'DATE_ADD'                    : 'f',
'DATE_FORMAT'                 : 'f',
'DATE_SUB'                    : 'f',
'DAY'                         : 'f',
'DAYNAME'                     : 'f',
'DAYOFMONTH'                  : 'f',
'DAYOFWEEK'                   : 'f',
'DAYOFYEAR'                   : 'f',
'DAY_HOUR'                    : 'k',
'DAY_MICROSECOND'             : 'k',
'DAY_MINUTE'                  : 'k',
'DAY_SECOND'                  : 'k',
'DEC'                         : 'k',
'DECIMAL'                     : 'k',
'DECLARE'                     : 'k',
'DECODE'                      : 'f',
'DEFAULT'                     : 'k',
'DEGREES'                     : 'f',
'DELAY'                       : 'k',
'DELAYED'                     : 'k',
'DELETE'                      : 'k',
'DESC'                        : 'k',
'DESCRIBE'                    : 'k',
'DES_DECRYPT'                 : 'f',
'DES_ENCRYPT'                 : 'f',
'DETERMINISTIC'               : 'k',
'DISTINCROW'                  : 'k',
'DISTINCT'                    : 'k',
'DIV'                         : 'o',
'DROP'                        : 'k',
'DUAL'                        : 'k',
'EACH'                        : 'k',
'ELSE'                        : 'k',
'ELSEIF'                      : 'k',
'ELT'                         : 'f',
'ENCLOSED'                    : 'k',
'ENCODE'                      : 'f',
'ENCRYPT'                     : 'f',
'ESCAPED'                     : 'k',
# TBD
#'END'                         : 'k',
'EXEC'                        : 'k',   # mssql
'EXECUTE'                     : 'k',
'EXISTS'                      : 'k',
'EXIT'                        : 'k',
'EXP'                         : 'f',
'EXPLAIN'                     : 'k',
'EXPORT_SET'                  : 'f',
'EXTRACT'                     : 'f',
'EXTRACTVALUE'                : 'f',
'EXTRACT_VALUE'               : 'f',
'FALSE'                       : 'k',
'FETCH'                       : 'k',
'FIELD'                       : 'f',
'FIND_IN_SET'                 : 'f',
'FLOOR'                       : 'f',
'FORCE'                       : 'k',
'FOREIGN'                     : 'k',
'FOR'                         : 'n',
'FORMAT'                      : 'f',
'FOUND_ROWS'                  : 'f',
'FROM'                        : 'k',
'FROM_DAYS'                   : 'f',
'FROM_UNIXTIME'               : 'f',
'FULLTEXT'                    : 'k',
'GENERATE_SERIES'             : 'f',
'GET_FORMAT'                  : 'f',
'GET_LOCK'                    : 'f',
'GOTO'                        : 'k',
'GRANT'                       : 'k',
'GREATEST'                    : 'f',
'GROUP'                       : 'n',
'GROUP_CONCAT'                : 'f',
'HAVING'                      : 'k',  # MSSQL
'HEX'                         : 'f',
'HIGH_PRIORITY'               : 'k',
'HOUR'                        : 'f',
'HOUR_MICROSECOND'            : 'k',
'HOUR_MINUTE'                 : 'k',
'HOUR_SECOND'                 : 'k',
'HOST_NAME'                   : 'f',  # unknown DB
# if is normally a function, except in TSQL
# http://msdn.microsoft.com/en-us/library/ms182717.aspx
'IF'                          : 'k',
'IFF'                         : 'f',
'IFNULL'                      : 'f',
'IGNORE'                      : 'k',
'IIF'                         : 'f',

# IN is a special case.. sometimes a function, sometimes a keyword
'IN'                          : 'n',

'INDEX'                       : 'k',
'INET_ATON'                   : 'f',
'INET_NTOA'                   : 'f',
'INFILE'                      : 'k',
'INNER'                       : 'k',
'INOUT'                       : 'k',
'INSENSITIVE'                 : 'k',
'INSERT'                      : 'k',
'INSTR'                       : 'f',
'INT'                         : 'k',
'INT1'                        : 'k',
'INT2'                        : 'k',
'INT3'                        : 'k',
'INT4'                        : 'k',
'INT8'                        : 'k',
'INTEGER'                     : 'k',
'INTERVAL'                    : 'k',
'INTO'                        : 'k',
'IS'                          : 'o',
'ISNULL'                      : 'f',
'IS_FREE_LOCK'                : 'f',
'IS_MEMBER'                   : 'f',  # MSSQL
'IS_SRVROLEMEMBER'            : 'f',  # MSSQL
'IS_USED_LOCK'                : 'f',
'ITERATE'                     : 'k',
'JOIN'                        : 'k',
'KEYS'                        : 'k',
'KILL'                        : 'k',
'LAST_INSERT_ID'              : 'f',
'LCASE'                       : 'f',
'LEADING'                     : 'k',
'LEAST'                       : 'f',
'LEAVE'                       : 'k',
'LEFT'                        : 'f',
'LENGTH'                      : 'f',
'LIKE'                        : 'o',
'LIMIT'                       : 'k',
'LINEAR'                      : 'k',
'LINES'                       : 'k',
'LN'                          : 'f',
'LOAD'                        : 'k',
'LOAD_FILE'                   : 'f',
'LOCALTIME'                   : 'k',
'LOCALTIMESTAMP'              : 'k',
'LOCATE'                      : 'f',
'LOCK'                        : 'k',
'LOG'                         : 'f',
'LOG10'                       : 'f',
'LOG2'                        : 'f',
'LONGBLOB'                    : 'k',
'LONGTEXT'                    : 'k',
'LOOP'                        : 'k',
'LOWER'                       : 'f',
'LOW_PRIORITY'                : 'k',
'LPAD'                        : 'f',
'LTRIM'                       : 'f',
'MAKEDATE'                    : 'f',
'MAKE_SET'                    : 'f',
'MASTER_BIND'                 : 'k',
'MASTER_POS_WAIT'             : 'f',
'MASTER_SSL_VERIFY_SERVER_CERT': 'k',
'MATCH'                       : 'k',
'MAX'                         : 'f',
'MAXVALUE'                    : 'k',
'MD5'                         : 'f',
'MEDIUMBLOB'                  : 'k',
'MEDIUMINT'                   : 'k',
'MEDIUMTEXT'                  : 'k',
'MERGE'                       : 'k',
'MICROSECOND'                 : 'f',
'MID'                         : 'f',
'MIDDLEINT'                   : 'k',
'MIN'                         : 'f',
'MINUTE'                      : 'f',
'MINUTE_MICROSECOND'          : 'k',
'MINUTE_SECOND'               : 'k',
'MOD'                         : 'o',
'MODE'                        : 'n',
'MODIFIES'                    : 'k',
'MONTH'                       : 'f',
'MONTHNAME'                   : 'f',
'NAME_CONST'                  : 'f',
'NOT'                         : 'o',
'NOW'                         : 'f',
'NO_WRITE_TO_BINLOG'          : 'k',
'NULL'                        : '1',
'NULLIF'                      : 'f',
'NUMERIC'                     : 'k',
'OCT'                         : 'f',
'OCTET_LENGTH'                : 'f',
'OFFSET'                      : 'k',
'OLD_PASSWORD'                : 'f',
# need to investigate how used
#'ON'                          : 'k',
'ONE_SHOT'                    : 'k',
# obviously not SQL but used in attacks
'OWN3D'                       : 'k',
'OPEN'                        : 'k', # http://msdn.microsoft.com/en-us/library/ms190500.aspx
'OPENDATASOURCE'              : 'f', # http://msdn.microsoft.com/en-us/library/ms179856.aspx
'OPENXML'                     : 'f',
'OPENQUERY'                   : 'f',
'OPENROWSET'                  : 'f',
'OPTIMIZE'                    : 'k',
'OPTION'                      : 'k',
'OPTIONALLY'                  : 'k',
'OR'                          : '&',
'ORD'                         : 'f',
'ORDER'                       : 'n',
'OUT'                         : 'k',
'OUTFILE'                     : 'k',
'PARTITION'                   : 'k',
'PASSWORD'                    : 'k',  # keyword "SET PASSWORD", and a function
'PERIOD_ADD'                  : 'f',
'PERIOID_DIFF'                : 'f',
'PG_SLEEP'                    : 'f',
'PI'                          : 'f',
'POSITION'                    : 'f',
'POW'                         : 'f',
'POWER'                       : 'f',
'PRECISION'                   : 'k',
'PRIMARY'                     : 'k',
'PROCEDURE'                   : 'k',
'PURGE'                       : 'k',
'QUARTER'                     : 'f',
'QUOTE'                       : 'f',
'RADIANS'                     : 'f',
'RAND'                        : 'f',
'RANDOMBLOB'                  : 'f',  # sqlite3
'RANGE'                       : 'k',
'READ'                        : 'k',
'READS'                       : 'k',
'READ_WRITE'                  : 'k',
'REAL'                        : 'n',   # only used in data definition
'REFERENCES'                  : 'k',
'REGEXP'                      : 'o',
'RELEASE'                     : 'k',
'RELEASE_LOCK'                : 'f',
'RENAME'                      : 'k',
'REPEAT'                      : 'k',
'REPLACE'                     : 'k',
'REQUIRE'                     : 'k',
'RESIGNAL'                    : 'k',
'RESTRICT'                    : 'k',
'RETURN'                      : 'k',
'REVERSE'                     : 'f',
'REVOKE'                      : 'k',
'RIGHT'                       : 'f',
'RLIKE'                       : 'o',
'ROUND'                       : 'f',
'ROW'                         : 'f',
'ROW_COUNT'                   : 'f',
'RPAD'                        : 'f',
'RTRIM'                       : 'f',
'SCHEMA'                      : 'k',
'SCHEMAS'                     : 'k',
'SECOND_MICROSECOND'          : 'k',
'SEC_TO_TIME'                 : 'f',
'SELECT'                      : 'k',
'SENSITIVE'                   : 'k',
'SEPARATOR'                   : 'k',
'SESSION_USER'                : 'f',
'SET'                         : 'k',
'SHA'                         : 'f',
'SHA1'                        : 'f',
'SHA2'                        : 'f',
'SHOW'                        : 'k',
'SHUTDOWN'                    : 'k',
'SIGN'                        : 'f',
'SIGNAL'                      : 'k',
'SIMILAR'                     : 'k',
'SIN'                         : 'f',
'SLEEP'                       : 'f',
'SMALLINT'                    : 'k',
'SOUNDEX'                     : 'f',
'SOUNDS'                      : 'o',
'SPACE'                       : 'f',
'SPATIAL'                     : 'k',
'SPECIFIC'                    : 'k',
'SQL'                         : 'k',
'SQLEXCEPTION'                : 'k',
'SQLSTATE'                    : 'k',
'SQLWARNING'                  : 'k',
'SQL_BIG_RESULT'              : 'k',
'SQL_CALC_FOUND_ROWS'         : 'k',
'SQL_SMALL_RESULT'            : 'k',
'SQRT'                        : 'f',
'SSL'                         : 'k',
'STARTING'                    : 'k',
'STDDEV'                      : 'f',
'STDDEV_POP'                  : 'f',
'STDDEV_SAMP'                 : 'f',
'STRAIGHT_JOIN'               : 'k',
'STRCMP'                      : 'f',
'STR_TO_DATE'                 : 'f',
'SUBDATE'                     : 'f',
'SUBSTR'                      : 'f',
'SUBSTRING'                   : 'f',
'SUBSTRING_INDEX'             : 'f',
'SUBTIME'                     : 'f',
'SUM'                         : 'f',
'SYSDATE'                     : 'f',
'SYSCOLUMNS'                  : 'k',  # http://msdn.microsoft.com/en-us/library/aa260398(v=sql.80).aspx
'SYSOBJECTS'                  : 'k',  # http://msdn.microsoft.com/en-us/library/aa260447(v=sql.80).aspx
'SYSUSERS'                    : 'k',  # MSSQL
'SYSTEM_USER'                 : 'f',
'TABLE'                       : 'k',
'TAN'                         : 'f',
'TERMINATED'                  : 'k',
'THEN'                        : 'k',
'TIME'                        : 'k',
'TIMEDIFF'                    : 'f',
'TIMESTAMP'                   : 'f',
'TIMESTAMPADD'                : 'f',
'TIME_FORMAT'                 : 'f',
'TIME_TO_SEC'                 : 'f',
'TINYBLOB'                    : 'k',
'TINYINT'                     : 'k',
'TINYTEXT'                    : 'k',
'TO_DAYS'                     : 'f',
'TO_SECONDS'                  : 'f',
'TOP'                         : 'k',
'TRAILING'                    : 'k',
'TRIGGER'                     : 'k',
'TRIM'                        : 'f',
'TRUE'                        : 'k',
'TRUNCATE'                    : 'f',
'UCASE'                       : 'f',
'UNCOMPRESS'                  : 'f',
'UNCOMPRESS_LENGTH'           : 'f',
'UNDO'                        : 'k',
'UNHEX'                       : 'f',
'UNION'                       : 'U',
# only used as a function (DB2) or as "CREATE UNIQUE"
'UNIQUE'                      : 'n',
'UNIX_TIMESTAMP'              : 'f',
'UNLOCK'                      : 'k',
'UNSIGNED'                    : 'k',
'UPDATE'                      : 'k',
'UPDATEXML'                   : 'f',
'UPPER'                       : 'f',
'USAGE'                       : 'k',
'USE'                         : 'k',
#'USER'                       : 'k',   # MySQL function?
'USING'                       : 'f',
'UTC_DATE'                    : 'k',
'UTC_TIME'                    : 'k',
'UTC_TIMESTAMP'               : 'k',
'UUID'                        : 'f',
'UUID_SHORT'                  : 'f',
'VALUES'                      : 'k',
'VARBINARY'                   : 'k',
'VARCHAR'                     : 'k',
'VARCHARACTER'                : 'k',
'VARIANCE'                    : 'f',
'VARYING'                     : 'k',
'VAR_POP'                     : 'f',
'VAR_SAMP'                    : 'f',
'VERSION'                     : 'f',
'WAITFOR'                     : 'k',
'WEEK'                        : 'f',
'WEEKDAY'                     : 'f',
'WEEKOFYEAR'                  : 'f',
'WHEN'                        : 'k',
'WHERE'                       : 'k',
'WHILE'                       : 'k',
'WITH'                        : 'k',
'XMLELEMENT'                  : 'f',   # oracle
'XMLFOREST'                   : 'f',   # oracle
'XMLFORMAT'                   : 'f',   # oracle
'XMLTYPE'                     : 'f',
'XOR'                         : 'o',
'XP_EXECRESULTSET'            : 'k',
'YEAR'                        : 'f',
'YEARWEEK'                    : 'f',
'YEAR_MONTH'                  : 'k',
'ZEROFILL'                    : 'k'
})

mapping = ['', '(', ')', ',', '1', ';', 'c', 'f', 'k', 'n', 'o', 's', 'v']


sqlipat = frozenset([
'1)));',
'1))))',
'1,1),',
'1),(1',
'1,(f(',
'1,f(1',
'1,(k(',
'1;k((',
'1);k(',
'1));k',
'1)))k',
'1,(k1',
'1;k(1',
'1)k1',
'1))k1',
'1k1c',
'1k1Uk',
'1)k1c',
'1)k1o',
'1,(kf',
'1;kf(',
'1);kf',
'1kf(1',
'1);kk',
'1))kk',
'1kk(1',
'1;kks',
'1)kks',
'1kksc',
'1;kn(',
'1);kn',
'1;knc',
'1;k(o',
'1;ko(',
'1);ko',
'1;kok',
'1)))o',
'1))o(',
'1o(((',
'1))o1',
'1)o(1',
'1o((1',
'1o(1)',
'1)o1f',
'1o1f(',
'1)o1k',
'1o1kf',
'1)o1o',
'1o(1o',
'1o1)o',
'1o1o(',
'1o1o1',
'1o1of',
'1o1oo',
'1o1ov',
'1))of',
'1)of(',
'1o((f',
'1o(f(',
'1of()',
'1of(1',
'1of(f',
'1of(n',
'1))ok',
'1)o(k',
'1)ok(',
'1ok1',
'1)ok1',
'1o(k1',
'1ok(1',
'1ok1,',
'1ok1c',
'1ok1k',
'1o(kf',
'1okf(',
'1ok(k',
'1o(kn',
'1oks,',
'1oksc',
'1okv,',
'1))on',
'1)o(n',
'1o(n)',
'1)ono',
'1ono1',
'1onos',
'1o(s)',
'1oso1',
'1,s),',
'1)()s',
'f(1,f',
'f(1)o',
'f(1o1',
'f(f()',
'f(f(1',
'f(k,(',
'f(k()',
'f(n()',
'f()of',
'f(v,1',
'k1,1,',
'k1,1k',
'k1k(k',
'k1o(s',
'kf(1,',
'kf(1)',
'kf(f(',
'kf(n,',
';kknc',
'k()ok',
'k(ok(',
'kvk(1',
'k(vv)',
'n)));',
'n,(f(',
'n,f(1',
'n,(k(',
'n;k((',
'n);k(',
'n));k',
'n)))k',
'n,(k1',
'n;k(1',
'n)k1o',
'n,(kf',
'n;kf(',
'n);kf',
'n);kk',
'n))kk',
'n;kks',
'n)kks',
'nkksc',
'n;kn(',
'n);kn',
'n;ko(',
'n);ko',
'n;kok',
'n)))o',
'n))o(',
'n))o1',
'no(1)',
'n)o1f',
'no1f(',
'n)o1o',
'no1o(',
'no1o1',
'no1of',
'no1oo',
'n))of',
'n)of(',
'nof(1',
'n))ok',
'n)o(k',
'n)ok(',
'no(k1',
'nok(1',
'nok(k',
'no(o1',
'o1kf(',
'of(1)',
'of()o',
'ok1o1',
'okkkn',
'ook1,',
's)));',
's,1),',
's),(1',
'sf(1)',
'sf(n,',
'sf(s)',
's;k;',
's;k((',
's);k(',
's));k',
's)))k',
's;k(1',
's;k1,',
's)k1',
's))k1',
'sk1c',
's)k1c',
's;k1o',
's)k1o',
'sk1o1',
'sk1os',
's;kf(',
's);kf',
's;k[k',
's);kk',
's))kk',
'sk);k',
'sk)k1',
'sk)kk',
's;kkn',
'skks',
's;kks',
's)kks',
'skksc',
's;k[n',
's;kn(',
's);kn',
's;knk',
's;knn',
's;k(o',
's;ko(',
's);ko',
'sk)o(',
'sk)o1',
'sk)of',
's;kok',
'sk)ok',
's;kvc',
's;kvk',
's;n:k',
's)))o',
's))o(',
'so(((',
's))o1',
's)o(1',
'so(1)',
'so1c',
's)o1f',
'so1f(',
's)o1k',
'so1kf',
's)o1o',
'so(1o',
'so1o(',
'so1o1',
'so1of',
'so1ok',
'so1oo',
'so1os',
'so1ov',
's))of',
's)of(',
'so(f(',
'sof()',
'sof(1',
'sof(f',
'sof(k',
's))ok',
's)o(k',
's)ok(',
'so((k',
'so(k)',
'sok1',
's)ok1',
'so(k1',
'sok(1',
'sok1,',
'sok1c',
'sok1o',
'sokc',
'sokf(',
'so(kk',
'sok(k',
'so(kn',
'sokn,',
'soknk',
'so(ko',
'sok(o',
'soko(',
'soko1',
'sokok',
'sokos',
'so(ks',
'sok(s',
'sonk1',
'sono1',
'sonos',
'so(os',
'sos',
'so((s',
'so(s)',
'soso(',
'sosos',
'sov:o',
'sovo1',
'sovok',
'sovos',
'sovov',
'sovso',
'vok1,',
'1B1',
's)B1c',
'sB1',
'1)o1B',
's)B1',
'1)))B',
'1))B1',
'1B1c',
'1Bk(1',
'1Bf(1',
'1)B1o',
'1o1Bf',
's)B1o',
'1)B1c',
'1)B1',
's)))B',
's))B1',
'sk)B1',
    "sB1c",
    "sB1os",
    "so1Bf",
    "s)o1B",
'1)))U',
'1))Un',
'1)Unk',
'1Uk',
'kok(k',
'1Ukns',
'1Uk1',
'1Uk1,',
'1Uk1c',
'1Uk1k',
'1Ukv,',
'1Unk(',
'1Unk1',
'1Unkf',
'Ukkkn',
'nUnk(',
'oUk1,',
's)))U',
's))Un',
's)Unk',
'sU((k',
'sU(kk',
'sU(kn',
'sU(ks',
'sUk(k',
'sUkf(',
'sUkn,',
'sUknk',
'sUn(k',
'sUnk1',
'sUnkf',
'sUno1',
'sk)Un',
'so1Uk',
'vUk1,',
'sUk1,',
'sUk1c',
'sUk1o',
'sk)Uk',
's))Uk',
's)Uk1',
'1))Uk',
'1)Uk1',
'sUk1',
'1Uk(k',
'1Uks,',
'1Uksc',
'1Ukf(',
'nUk(k'
'&f()o',
'&f(1)',
'1&(k1',
'1&(kf',
'1&1Bf',
'1&1f(',
'1&1o(',
'1&1o1',
'1&1of',
'1&1ov',
'1&f(1',
'1&f(n',
'1&no1',
'1&o(1',
'1&o1o',
'1)&(1',
'1)&(k',
'1)&1B',
'1)&1f',
'1)&1o',
'1)&f(',
'1)&o(',
'1))&(',
'1))&1',
'1))&f',
'1))&o',
'1)))&',
'1)B1&',
'1)on&',
'f()&f',
'f(1)&',
'n&(1)',
'n&(k1',
'n&(o1',
'n&1f(',
'n&1o(',
'n&1o1',
'n&1of',
'n&f(1',
'n&k(1',
'n&o1o',
'n)&(k',
'n)&1f',
'n)&1o',
'n)&f(',
'n))&(',
'n))&1',
'n))&f',
'n)))&',
'n)o1&',
'no1&1',
's&(1)',
's&(1o',
's&(f(',
's&(k)',
's&(k1',
's&1Bf',
's&1Uk',
's&1f(',
's&1o(',
's&1o1',
's&1of',
's&1on',
's&1oo',
's&1os',
's&1ov',
's&f()',
's&f(1',
's&k&s',
's&k(1',
's&k(o',
's&k1o',
's&kc',
's&knk',
's&ko(',
's&ko1',
's&kok',
's&kos',
's&n&s',
's&no1',
's&nos',
's&o(1',
's&o(k',
's&o1o',
's&okc',
's&oko',
's&os',
's&sos',
's&v:o',
's&vos',
's&vso',
's)&(k',
's)&1B',
's)&1f',
's)&1o',
's)&f(',
's)&o(',
's))&(',
's))&1',
's))&f',
's))&o',
's)))&',
's);k&',
's)B1&',
's;k&k',
'sB1&s',
'sUk1&',
'sk)&(',
'sk)&1',
'sk)&f',
'sk1&1',
'so1&1',
'so1&o',
'so1&s',
'sok&s',
'sos&(',
'sov&1',
'sov&s',
'&f()o',
'n;k&k',
'1;kok',
'1);ko',
'n);ko',
'1&(kn',
'1);k&',
'n);k&',
'1;k&k',
's&f(1',
'nUk(k',
'1&1oo',
'n&1oo',
'1&so1',
's)&(1',
'1&(1o',
'sUkv,',
'1)Ukn',
'1Ukn,',
'1&f(f',
'1&1on',
'sU(k(',
'1&1Uk',
'1&(1,',
'1&f((',
'1)&(f',
'1Ukkk',
's&(1,',
'1Uknk',
'1o1)&',
's&f(v',
'1&n()',
'1&(ko',
'1Ukvc',
'1)U(k',
'1Ukn(',
'kn1kk',
'k;non',
'n;no1',
's&f(f',
'kn1vn',
'kn1vk',
'1Ukk(',
'1&(f(',
'1)Ukf',
'sk1Uk',
'sUkn1',
'1,1B1',
's&(kf',
'1Ukk,',
'&1o1U',
'1&kUk',
'1)&1U',
'1)Ukk',
'1,1Uk',
'1B1Uk',
'1U(k1',
'1U(kf',
'1U1,1',
'1Uc',
'1Uk(n',
'1Uk1f',
'1Uk1n',
'1Ukf',
'1Ukkn',
'1Ukn&',
'1Ukn1',
'1Uknc',
'1Ukno',
'1Uko1',
'1Ukok',
'1Ukv',
'1Un',
'1Un,1,'
'1Un1,',
'1Uon1',
'1k1U(',
'1kU1,',
'1nUk1',
'1nUkn',
'1o1Uk',
'Uk1,1',
'Uk1,f',
'Uk1,n',
'k(1)U',
'n:o1U',
'nUk1,',
'nUkn,',
'nk1Uk',
'nnn)U',
'nno1U',
'no1Uk',
's)U(k',
'sB1Uk',
'sUk1k',
'sUkkk',
'sUkn(',
'sUkok',
'sUkvc',
'skU1,',
'sno1U',
's&f((',
'1,1)o',
'1f()k',
'1)&(n',
'1&f(v',
'1Bnk1',
's))&n',
'1B1,1',
'v:o1)',
'1Un1,',
'1o(kv',
'1Bf(f',
'1Un,1',
'1&((f',
'1;k1,',
'1Bn,n',
'1&f()',
'1&f(k',
'1;kn,',
'f((kf',
'1&(v)',
'kf(v:',
'kv)',
'kk1vn',
'1n&f(',
'1nkf(',
'f((k(',
'f(k,n',
'k1,f(',
'kk(f(',
'n&f(f',
'nkf(1',
'sn,f(',
'k1,1c',
'1&k(f',
'1&1ok',
'kk1vk',
'kk1nk',
'kk1kk',
'sUkk1',
'1Ukk1',
's&1c',
'1nk1c'
])

        # special in that single char is a valid operator
        # special case in that '<=' might also be '<=>'
        # ":" isn't an operator in mysql, but other dialects
        #   use it.
double_char_operators = frozenset( (
                '!=',   # oracle
                '||',
                '&&',
                '>=',
                '>>',
                '<=',
                '<>',
                ':=',
                '<<',
                '!<', # http://msdn.microsoft.com/en-us/library/ms188074.aspx
                '!>', # http://msdn.microsoft.com/en-us/library/ms188074.aspx
                '+=',
                '-=',
                '*=',
                '/=',
                '%=',
                '|=',
                '&=',
                '^=',
                '|/', # http://www.postgresql.org/docs/9.1/static/functions-math.html
                '!!', # http://www.postgresql.org/docs/9.1/static/functions-math.html
                '~*', # http://www.postgresql.org/docs/9.1/static/functions-matching.html
                '!~', # http://www.postgresql.org/docs/9.1/static/functions-matching.html
                '@>',
                '<@'
                # '!~*'
                ) )

CHAR_WORD = 0
CHAR_NONE = 1
CHAR_WHITE = 2
CHAR_STR = 3
CHAR_OP1 = 4
CHAR_OP2 = 5
CHAR_CHAR = 6
CHAR_COM1 = 7
CHAR_DASH = 8
CHAR_SLASH = 9
CHAR_BACK = 10
CHAR_NUM = 11
CHAR_VAR = 13
CHAR_OTHER = 14

charmap = [
            CHAR_WHITE, # 0
            CHAR_WHITE, # 1
            CHAR_WHITE, # 2
            CHAR_WHITE, # 3
            CHAR_WHITE, # 4
            CHAR_WHITE, # 5
            CHAR_WHITE, # 6
            CHAR_WHITE, # 7
            CHAR_WHITE, # 8
            CHAR_WHITE, # 9
            CHAR_WHITE, # 10
            CHAR_WHITE,
            CHAR_WHITE,
            CHAR_WHITE,
            CHAR_WHITE,
            CHAR_WHITE,
            CHAR_WHITE,
            CHAR_WHITE,
            CHAR_WHITE,
            CHAR_WHITE,
            CHAR_WHITE, # 20
            CHAR_WHITE,
            CHAR_WHITE,
            CHAR_WHITE,
            CHAR_WHITE,
            CHAR_WHITE,
            CHAR_WHITE,
            CHAR_WHITE,
            CHAR_WHITE,
            CHAR_WHITE,
            CHAR_WHITE, #30
            CHAR_WHITE,
            CHAR_WHITE,
            CHAR_OP2,   # 33 !
            CHAR_STR,   # 34 "
            CHAR_COM1,  # 35 "#"
            CHAR_WORD,  # 36 $
            CHAR_OP1,   # 37 %
            CHAR_OP2,   # 38 &
            CHAR_STR,   # 39 '
            CHAR_CHAR,  # 40 (
            CHAR_CHAR,  # 41 )
            CHAR_OP2,   # 42 *
            CHAR_OP1,   # 43 +
            CHAR_CHAR,  # 44 ,
            CHAR_DASH,  # 45 -
            CHAR_NUM,   # 46 .
            CHAR_SLASH, # 47 /
            CHAR_NUM,   # 48 0
            CHAR_NUM,   # 49 1
            CHAR_NUM,   # 50 2
            CHAR_NUM,   # 51 3
            CHAR_NUM,   # 52 4
            CHAR_NUM,   # 53 5
            CHAR_NUM,   # 54 6
            CHAR_NUM,   # 55 7
            CHAR_NUM,   # 56 8
            CHAR_NUM,   # 57 9
            CHAR_CHAR,  # 58 : colon
            CHAR_CHAR,  # 59 ; semiclon
            CHAR_OP2,   # 60 <
            CHAR_OP2,   # 61 =
            CHAR_OP2,   # 62 >
            CHAR_OTHER, # 63 ?   BEEP BEEP
            CHAR_VAR,   # 64 @
            CHAR_WORD,  # 65 A
            CHAR_WORD,  # 66 B
            CHAR_WORD,  # @
            CHAR_WORD,  # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # Z
            CHAR_OTHER,           # [
            CHAR_BACK,            # \\
            CHAR_OTHER,           # ]
            CHAR_OP1,             # ^
            CHAR_WORD,            # _
            CHAR_WORD,            # backtick
            CHAR_WORD,            # A
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # @
            CHAR_WORD,            # z
            CHAR_OTHER,            # 123 { left brace
            CHAR_OP2,             # 124 | pipe
            CHAR_OTHER,            # 125 } right brace
            CHAR_OP1,             # 126  ~
            CHAR_WHITE
]

phrases = dict({
'IN BOOLEAN': 'n',
'IN BOOLEAN MODE': 'k',
'CROSS JOIN': 'k',
'ALTER DOMAIN': 'k',
'ALTER TABLE': 'k',
'GROUP BY': 'B',
'ORDER BY': 'B',
'OWN3D BY': 'B',
'SELECT ALL': 'k',
'READ WRITE': 'k',
'LEFT OUTER': 'k',
'LEFT JOIN': 'k',
'RIGHT OUTER': 'k',
'RIGHT JOIN': 'k',
'FULL OUTER': 'k',
'NATURAL JOIN': 'k',
'NATURAL INNER': 'k',
'NATURAL OUTER': 'k',
'NATURAL LEFT': 'k',
'NATURAL RIGHT': 'k',
'NATURAL FULL': 'k',
'SOUNDS LIKE': 'o',
'IS NOT': 'o',
'NOT LIKE': 'o',
'NOT BETWEEN': 'o',
'NOT SIMILAR': 'o',
'NOT IN': 'o',
'SIMILAR TO' : 'o',
'NOT SIMILAR TO': 'o',
'UNION ALL': 'U',
'INTERSECT ALL': 'o'   # ORACLE
})

if False:
    import sys
    count = 0
    for i in sqlipat:
        sys.stdout.write("%5s " % (i,))
        count += 1
        if count == 20:
            sys.stdout.write("\n")
            count = 0

