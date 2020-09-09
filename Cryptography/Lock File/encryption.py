class GUI_e:

    def __init__(self, username, password):
        self.name = username
        self.Pass = password
        self.types = ['caesar', 'vig', 'rsa']
        self.n = len(self.Pass)
        
     def caesar(self, word, dir, n):
        x = list(word)
        a = 'abcdefghijklmnopqrstuvwxyz'
        b = a.upper()
        a = list(a)
        b = list(b)
        if dir == 'l':
            if n == 'brute':
                # speaker.say('performing brute force encryption with left shift')
                # speaker.runAndWait()
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
                # speaker.say('performing caesar cipher encryption with left shift of {}'.format(int(n)))
                # speaker.runAndWait()
                n = int(n)
                c = a[-n:] + a[:-n]
                d = b[-n:] + b[:-n]
                for k in range(len(x)):
                    if x[k] in a:
                        x[k] = c[a.index(x[k])]
                    elif x[k] in b:
                        x[k] = d[b.index(x[k])]
                return ''.join(x)
                # speaker.say('encryption complete')
                # speaker.runAndWait()
        elif dir == 'r':
            if n == 'brute':
                # speaker.say('performing brute force encryption with right shift')
                # speaker.runAndWait()
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
                # speaker.say('performing caesar cipher encryption with right shift of {}'.format(int(n)))
                # speaker.runAndWait()
                n = int(n)
                c = a[n:] + a[:n]
                d = b[n:] + b[:n]
                for k in range(len(x)):
                    if x[k] in a:
                        x[k] = c[a.index(x[k])]
                    elif x[k] in b:
                        x[k] = d[b.index(x[k])]
                return ''.join(x)
                # speaker.say('encryption complete')
                # speaker.runAndWait()
    def vigenere(self, word, key1):
        # speaker.say('performing Vigenère encryption using the given key')
        # speaker.runAndWait()
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        alpha = list(alpha)
        gamma = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        gamma = list(gamma)
        word = list(word)
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
                    num = n + x[i]
                    if n + x[i] > 25:
                        num2 = num - 25
                        beta = alpha[num2:] + alpha[:num2]
                        word[k] = beta[beta.index(word[k]) + x[i]]
                    else:
                        word[k] = alpha[alpha.index(word[k]) + x[i]]
                elif word[k] in gamma:
                    n = gamma.index(word[k])
                    if n + x[i] > 25:
                        num2 = (n + x[i]) - 25
                        beta = gamma[num2:] + gamma[:num2]
                        word[k] = beta[beta.index(word[k]) + x[i]]
                    else:
                        word[k] = gamma[n + x[i]]
        # adding spaces in original position
        new = []
        for j in range(len(word)):
            if j in a:
                new.insert(j, ' ')
            new.append(word[j])
        return ''.join(new)
        # speaker.say('encryption complete')
        # speaker.runAndWait()
    def rsa(self, word, p, q):
        def gcd(ele1, ele2):
            if ele2 == 0:
                return ele1
            else:
                return gcd(ele2, ele1 % ele2)

        text = ""
        N = p * q
        phiN = (p - 1) * (q - 1)
        e = 0
        for i in range(2, phiN):
            if gcd(N, i) == 1 and gcd(phiN, i) == 1:
                e = i
                break
        for j in word:
            if j.isupper():
                k = ord(j) - 64
                calc = (k ** e) % N
                text += str(calc) + ' '
            elif j.islower():
                k = ord(j) - 96
                calc = (k ** e) % N
                text += str(calc) + ' '
            else:
                text += j + ' '
        return text
      
         def new(self):
        k = ''
        cd = []
        new_pass = self.Pass
        # encrypting thrice
        for i in range(2):
            x = random.choice(['caesar', 'vig'])
            if x == 'caesar':
                K = x
                dir = random.choice(['l', 'r'])
                K = K + ' ' + dir
                n = random.randint(1, 26)
                K = K + ' ' + str(n)
                new_pass = self.caesar(new_pass, dir, n)
                k = k + K + ' '
            elif x == 'vig':
                K = x
                # creating key of random length (<=len(new_pass)) using random letters from new_pass
                key = []
                num = random.randint(1, len(new_pass))
                a = list(new_pass)
                while len(key) != num:
                    a1 = random.choice(a)
                    if a1 != ' ':
                        key.append(a1)
                key = ''.join(key)
                K = K + ' ' + key
                new_pass = self.vigenere(new_pass, key)
                k = k + K + ' '
        x = random.choice(self.types)
        if x == 'caesar':
            K = x
            dir = random.choice(['l', 'r'])
            K = K + ' ' + dir
            n = random.randint(1, 26)
            K = K + ' ' + str(n)
            new_pass = self.caesar(new_pass, dir, n)
            k = k + K + ' '
        elif x == 'vig':
            K = x
            # creating key of random length (<=len(new_pass)) using random letters from new_pass
            key = []
            num = random.randint(1, len(new_pass))
            a = list(new_pass)
            while len(key) != num:
                a1 = random.choice(a)
                if a1 != ' ':
                    key.append(a1)
            key = ''.join(key)
            K = K + ' ' + key
            new_pass = self.vigenere(new_pass, key)
            k = k + K + ' '
        # else:
        #     K = x
        #     prime = [i for i in range(len(new_pass) + 1)]
        #     p = 3
        #     prime[0] = False
        #     prime[1] = False
        #     while p * p <= len(new_pass) + 1:
        #         if prime[p] != False:
        #             for d in range(p * p, len(new_pass) + 1, p):
        #                 prime[d] = False
        #         p = p + 2
        #     a = []
        #     for j in range(len(prime)):
        #         if prime[j] != False:
        #             if prime[j] % 2 != 0 or prime[j] == 2:
        #                 a.append(prime[j])
        #     # choosing two random prime numbers
        #     x = random.choice(a)
        #     K = K + ' ' + str(x)
        #     a.remove(x)
        #     y = random.choice(a)
        #     K = K + ' ' + str(y)
        #     k = k + K + ' '
        #     new_pass = self.rsa(new_pass, x, y)
        cd.append(self.name)
        cd.append(new_pass)
        cd.append(k)
        # appending to a file
        file = open('file-1.txt', 'a')
        file.write(' '.join(cd))
        file.write('\n')
        file.close()
   
