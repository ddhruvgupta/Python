import sqlite3

conn = sqlite3.connect('py4e.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    # email = pieces[1]
    email = pieces[1].split('@')
    org = email[1].split('.')
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (org[0],))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (org[0],))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (org[0],))


# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
conn.commit()

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
