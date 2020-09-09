class GUI_d:
    def __init__(self, username, password):
        self.name = username
        self.Pass = password

    def caesar(self, word, dir, n):
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
            

    def vigenere(self, word1, key1):
         alpha = 'abcdefghijklmnopqrstuvwxyz'
        alpha = list(alpha)
        gamma = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        gamma = list(gamma)
        word = list(word1)
        key = list(key1)
        # keeping record of index position of alphabets in key
        x = []
        for z in range(len(key)):
            if key[z] in alpha:
                x.append(alpha.index(key[z]))
            elif key[z] in gamma:
                x.append(gamma.index(key[z]))
        # keeping record of index position of spaces
        a = []
        for c in range(len(word)):
            if word[c] == ' ':
                a.append(c)
        # removing all spaces
        while word.count(' ') != 0:
            word.remove(' ')
        # encrypting using vigenere cipher
        for i in range(len(x)):
            for k in range(i, len(word), len(x)):
                if word[k] in alpha:
                    n = alpha.index(word[k])
                    if n - x[i] < 0:
                        beta = alpha[n + 1:] + alpha[:n + 1]
                        word[k] = beta[beta.index(word[k]) - x[i]]
                    else:
                        word[k] = alpha[n - x[i]]
                elif word[k] in gamma:
                    n = gamma.index(word[k])
                    if n - x[i] < 0:
                        beta = gamma[n + 1:] + gamma[:n + 1]
                        word[k] = beta[beta.index(word[k]) - x[i]]
                    else:
                        word[k] = gamma[n - x[i]]
        # adding spaces in original position
        new = []
        for j in range(len(word)):
            if j in a:
                new.insert(j, ' ')
            new.append(word[j])
        return ''.join(new)

        
    def rsaAlgorithmD(self, t, p, q):
        def gcd(ele1, ele2):
            if ele2 == 0:
                return ele1
            else:
                return gcd(ele2, ele1 % ele2)

        p = int(p)
        q = int(q)
        text = ""
        N = p * q
        phiN = (p - 1) * (q - 1)
        for i in range(2, phiN):
            if gcd(N, i) == 1 and gcd(phiN, i) == 1:
                e = i
                break
        k = 1
        d = (phiN * k + 1) / e
        while d != int(d):
            k += 1
            d = (phiN * k + 1) / e
        t = t.split(' ')
        i = 0
        for j in range(len(t)):
            if t[j].isnumeric() and i == 0:
                t[j] = int(t[j])
                calc = 64 + int((t[j] ** d) % N)
                text += chr(calc)
                i += 1
            elif t[j].isnumeric():
                t[j] = int(t[j])
                calc = 96 + int((t[j] ** d) % N)
                text += chr(calc)
            elif j != (len(t) - 1) and t[j] == '' and t[j + 1] == '':
                text += ' '
            else:
                text += t[j]
        return text

        
    def new(self):
        file = open('file-1.txt', 'r')
        read = file.readlines()
        x = ''
        c = []
        a = []
        for line in read:
            if str(self.name) in line:
                x = str(line)
                x = x.split(' ')
                a.append('y')
                c.append(x)
            else:
                a.append('n')
        if 'y' not in a:
            user_not_found()
            return 'Username not found'
        else:
            z = []
            for k in range(len(c)):
                pa = (c[k])[1]
                if len(pa) == len(self.Pass):
                    z = c[k]
            if z != []:
                password = z[1]
                new = z[2:]
                for i in range(len(new) - 1, -1, -1):
                    if new[i] == 'caesar':
                        if new[i + 1] == 'r':
                            password = self.caesar(password, 'l', new[i + 2])
                        elif new[i + 1] == 'l':
                            password = self.caesar(password, 'r', new[i + 2])
                    elif new[i] == 'vig':
                        password = self.vigenere(password, new[i + 1])
                    elif new[i] == 'rsa':
                        password = self.rsaAlgorithmD(password, new[i + 1], new[i + 2])
                if self.Pass == password:
                    login_success()
                    return 'correct password'
                else:
                    incorrect_password()
                    return 'wrong password'

            else:
                incorrect_password()
                return 'wrong password'

 
   

   
