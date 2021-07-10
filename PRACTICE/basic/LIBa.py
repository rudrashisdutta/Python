import urllib,webbrowser
w=urllib.request.urlopen("https://github.com/pricing")
w1=w.read()
w2=w.getcode()
w3=w.headers
w4=w.info()
print(w1)
print(w2)
print(w3)
print(w4)
w5=w.geturl()
print(w5)
webbrowser.open(w5)
