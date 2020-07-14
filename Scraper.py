import urllib.request, urllib.error
import ssl
import json
import sqlite3

#connection with database
conn = sqlite3.connect('COVID.sqlite')
cur = conn.cursor()

cur.executescript('''
drop table if exists UttarPradesh;
drop table if exists Districts;

create table Districts(
    id integer not null primary key autoincrement unique,
    name text
);

create table UttarPradesh(
    district_id integer not null,
    dates date,
    confirmed integer,
    active integer,
    recovered integer
);
''')


#SSL certificate check
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#opening url
url = 'https://api.covid19india.org/districts_daily.json'
html = urllib.request.urlopen(url, context=ctx)
data = html.read().decode()


#extracting data
info = json.loads(data)

for district in info['districtsDaily']['Uttar Pradesh']:
    cur.execute('''insert or ignore into Districts (name) values (?)''', (district,))
    cur.execute('select id from Districts where name = ?', (district,))
    district_id = cur.fetchone()[0]
    print(district)

    for item in info['districtsDaily']['Uttar Pradesh'][district]:
        date = item.get('date')
        confirmed = item.get('confirmed')
        active = item.get('active')
        recovered = item.get('recovered')

        cur.execute('''insert into UttarPradesh (district_id, dates, confirmed, active, recovered)
                    values (?, ?, ?, ?, ?)''', (district_id, date, confirmed, active, recovered))

    conn.commit()

print('DATA LOADED SUCCESSFULLY!')
