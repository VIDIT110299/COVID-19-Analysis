import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('COVID.sqlite')
cur = conn.cursor()

cur.execute('''select * from Districts order by name''')
data = cur.fetchall()

for i in range(75):
    print(data[i][0], '\t', data[i][1])

print('\n')
choice = int(input('Enter District id: '))
print('\n')

cur.execute('''select * from UttarPradesh where district_id = ?''', (choice,))
data = cur.fetchall()

cur.execute('''select name from Districts where id = ?''', (choice,))
state = cur.fetchone()[0]

date_x = []
confirmed_y = []
active_y = []
recovered_y = []

for i in range(len(data)):
    date_x.append(data[i][1])
    confirmed_y.append(data[i][2])
    active_y.append(data[i][3])
    recovered_y.append(data[i][4])

plt.plot(date_x, confirmed_y, label = "Confirmed")
plt.plot(date_x, active_y, label = "Active")
plt.plot(date_x, recovered_y, label = "Recovered")

plt.xlabel('Date')
plt.ylabel('Cases')

plt.legend()
plt.title(state + ' COVID-19 Analysis')

plt.show()