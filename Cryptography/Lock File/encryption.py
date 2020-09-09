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
      
