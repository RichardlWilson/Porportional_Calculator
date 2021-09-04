# h = 12
# w = 10
# mw = 200

# while w <= mw:
# 	h += 1.2
# 	w += 1

# if w > mw:
# 	h -= 1.2
# 	w -= 1

# sqft = h*w/144

# print(h,w, sqft)	


# h = 12
# w = 10
# mw = 6

# while w >= mw:
# 	h -= 1.2
# 	w -= 1


# sqft = h*w/144

# print(h,w, sqft)

#................................................
h=144
w=120
m=3

while w -1 >= m:
	h -= 1.2
	w -= 1

print('low',round(h, 2),round(w, 2),round(h*w/144, 2))	

h=12
w=10
m=200

while w + 1 <= m:
	h += 1.2
	w += 1

# if h*w/144 > msq:
# 	h -= 1.2
# 	w -= 1


print('high',round(h, 2),round(w, 2),round(h*w/144, 2))


