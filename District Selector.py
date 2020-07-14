import sqlite3

#connection with database
conn = sqlite3.connect('COVID.sqlite')
cur = conn.cursor()


cur.execute('''select * from Districts order by name''')
data = cur.fetchall()

for i in range(75):
    print(data[i])

print('\n')
choice = int(input('Enter District id: '))
print('\n')

print('YYYY-MM-DD \t Confirmed \t Active \t Recovered')
cur.execute('''select dates, confirmed, active, recovered from UttarPradesh where district_id = ?''', (choice,))
data = cur.fetchall()

for i in range(len(data)):
    print(data[i][0], '\t', data[i][1], '\t', data[i][2], '\t', data[i][3])
