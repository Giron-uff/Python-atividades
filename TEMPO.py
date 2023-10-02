s = int(input("Informe um tempo"))

h = s // 3600
s = s % 3600
m = s // 60
s = s % 60

print(str(h) + ":" + str(m) + ":" + str(s))
