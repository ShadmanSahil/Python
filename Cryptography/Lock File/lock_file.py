class GUI_d:
    def __init__(self, username, password):
        self.name = username
        self.Pass = password

    def caesar(self):
        x = list(word)
        a = 'abcdefghijklmnopqrstuvwxyz'
        b = a.upper()
        a = list(a)
        b = list(b)
        if dir == 'l':
            if n == 'brute':
                for i in range(1, 27):
                    am = []
                    c = a[-i:] + a[:-i]
                    d = b[-i:] + b[:-i]
                    for k in range(len(x)):
                        if x[k] in a:
                            am.append(c[a.index(x[k])])
                        elif x[k] in b:
                            am.append(d[b.index(x[k])])
                        else:
                            am.append(x[k])
                    z = str(i)
                    print('Left Shift of ' + z, ':', ''.join(am))
            else:
                n = int(n)
                c = a[-n:] + a[:-n]
                d = b[-n:] + b[:-n]
                for k in range(len(x)):
                    if x[k] in a:
                        x[k] = c[a.index(x[k])]
                    elif x[k] in b:
                        x[k] = d[b.index(x[k])]
                return ''.join(x)
        elif dir == 'r':
            if n == 'brute':
                for i in range(1, 27):
                    am = []
                    c = a[i:] + a[:i]
                    d = b[i:] + b[:i]
                    for k in range(len(x)):
                        if x[k] in a:
                            am.append(c[a.index(x[k])])
                        elif x[k] in b:
                            am.append(d[b.index(x[k])])
                        else:
                            am.append(x[k])
                    z = str(i)
                    print('Righ Shift of ' + z, ':', ''.join(am))
            else:
                n = int(n)
                c = a[n:] + a[:n]
                d = b[n:] + b[:n]
                for k in range(len(x)):
                    if x[k] in a:
                        x[k] = c[a.index(x[k])]
                    elif x[k] in b:
                        x[k] = d[b.index(x[k])]
                return ''.join(x)
            

    def vigenere(self):
        pass
        
    def rsaAlgorithmD(self):
        pass
        
    def new(self):
        pass

   

   
