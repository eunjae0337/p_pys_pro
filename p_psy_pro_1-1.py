#!python3.9
print("Content-Type: text/html")
print()
import cgi
form = cgi.FieldStorage()
velocity = form["velocity"].value
time = form["time"].value


print('''
<h1>물체의 등속 운동 그래프</h1>

''')