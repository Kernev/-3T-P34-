import random

a = ['4', '/\\', '@', '^', '∂', '/-\\', '|\\']
b = ['8', '13', '|3', 'ß', '!3', '(3', '/3', ')3']
c = ['(', '¢', '<', '[', '©']
d = ['[)', 'T)', '|)']
e = ['3', '&', '€', 'є', 'ë']
f = ['|=', 'ƒ', '/=']
g = ['6', '(_+']
h = ['#', '/-/', '[-]', ']-[', ')-(', '(-)', ':-:', '|~|', '|-|', ']~[', ']-[', '}-{']
i = ['¡', 'i', '1', '|']
j = ['ʝ']
k = ['X', '|<', '|{']
l = ['£', '1', 'ℓ', '|_']
m = ['|v|', '|\/|', '/\/\\', '(V)', '(\/)', '/|\\', '^^', '/^^\\', '///', '|^^|']
n = ['|\|', '/\/', ']\[', '/V', '₪']
o = ['0', '()', '[]', '¤', '°']
p = ['|*', '|o', '|º', '|"', '|̊', '|7', '?', '/*', '¶']
q = ['()_', '0.']
r = ['Я', '|2', 'ʁ', '|°\\']
s = ['5', '$', 'z', '§', '_/¯']
t = ['†', '¯|¯']
u = ['(_)', '|_|', 'L|', 'µ']
v = ['\/', '1/', '|/']
w = ['\/\/', 'vv', '\^/', '\V/', '\X/', '\|/', '\_|_/', '\_:_/', 'Ш', 'ɰ', '\./']
x = ['><', 'Ж', '}{', '×', '}{', ')(']
y = ['`/', 'Ψ', 'φ', 'λ', 'Ч', '¥', '/']
z = ['~/_', '%', '-\_', '7_', '≥']

alphabet = {'a':a,
            'b':b,
            'c':c,
            'd':d,
            'e':e,
            'f':f,
            'g':g,
            'h':h,
            'i':i,
            'j':j,
            'k':k,
            'l':l,
            'm':m,
            'n':n,
            'o':o,
            'p':p,
            'q':q,
            'r':r,
            's':s,
            't':t,
            'u':u,
            'v':v,
            'w':w,
            'x':x,
            'y':y,
            'z':z
            }

while True:
    phrase = input('>: ')
    if phrase == "J'ai comme une saugrenue envie de m'en aller. Allons-y Martine !":
        break
    nouvelle_phrase = ''
    for lettre in phrase.lower():
        if lettre in alphabet:
            nouvelle_phrase += ' ' + random.choice(alphabet[lettre])
        elif lettre is ' ':
            nouvelle_phrase += '  '
        else:
            nouvelle_phrase += ' ' + lettre

    print(nouvelle_phrase)
