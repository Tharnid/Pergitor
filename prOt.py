hrs = input("Enter Hours: ")
r = 10.50
h = float(hrs)
if h <= 40:
	pay = r * h
if h > 40:
	pay = r * 40 + (r * 1.5 *( h - 40))
print pay
