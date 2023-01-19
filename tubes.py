import string

print(" __________________________________________________")
print("| Tugas Besar Teori Bahasa dan Automata | IF-44-09 |")
print("|          Lexical Analyzer & Parser               |")
print("|==================================================|")
print("|                    Terminal                      |")
print("| noun   : you | we | brother | cat                |")
print("| verb   : read | buy | eat                        |")
print("| object : food | book | bike                      |")
print("|__________________________________________________|")
print()

kata = input("Masukan kalimat: ")
inputKata = kata.lower() + "#"

listAlphabet = list(string.ascii_lowercase)
listState = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10',
            'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20',
            'q21', 'q22', 'q23']


transitionTable = {}

for i in listState:
    for alphabet in listAlphabet:
        transitionTable[(i, alphabet)] = "Error"
    transitionTable[(i, "#")] = "Error"
    transitionTable[(i, " ")] = "Error"

# Start State
transitionTable[("q0", " ")] = "q0"

# Finish State
transitionTable[("q4", "#")] = "Accept"
transitionTable[("q4", " ")] = "q23"
transitionTable[("q23", "#")] = "Accept"
transitionTable[("q23", " ")] = "q23"

# String 'you'
transitionTable[("q0", "y")] = "q17"
transitionTable[("q17", "o")] = "q18"
transitionTable[("q18", "u")] = "q4"
transitionTable[("q4", " ")] = "q23"
transitionTable[("q23", "y")] = "q17"

# String 'we'
transitionTable[("q0", "w")] = "q19"
transitionTable[("q19", "e")] = "q4"
transitionTable[("q4", " ")] = "q23"
transitionTable[("q23", "w")] = "q19"

# String 'brother'
transitionTable[("q0", "b")] = "q7"
transitionTable[("q7", "r")] = "q8"
transitionTable[("q8", "o")] = "q9"
transitionTable[("q9", "t")] = "q10"
transitionTable[("q10", "h")] = "q11"
transitionTable[("q11", "e")] = "q12"
transitionTable[("q12", "r")] = "q4"
transitionTable[("q4", " ")] = "q23"
transitionTable[("q23", "b")] = "q7"

# String 'cat'
transitionTable[("q0", "c")] = "q20"
transitionTable[("q20", "a")] = "q21"
transitionTable[("q21", "t")] = "q4"
transitionTable[("q4", " ")] = "q23"
transitionTable[("q23", "c")] = "q20"

# String 'read'
transitionTable[("q0", "r")] = "q1"
transitionTable[("q1", "e")] = "q2"
transitionTable[("q2", "a")] = "q3"
transitionTable[("q3", "d")] = "q4"
transitionTable[("q4", " ")] = "q23"
transitionTable[("q23", "r")] = "q1"

# String 'buy'
transitionTable[("q0", "b")] = "q7"
transitionTable[("q7", "u")] = "q19"
transitionTable[("q19", "y")] = "q4"
transitionTable[("q4", " ")] = "q23"
transitionTable[("q23", "b")] = "q7"

# String 'eat'
transitionTable[("q0", "e")] = "q22"
transitionTable[("q22", "a")] = "q21"
transitionTable[("q21", "t")] = "q4"
transitionTable[("q4", " ")] = "q23"
transitionTable[("q23", "e")] = "q22"

# String 'food'
transitionTable[("q0", "f")] = "q5"
transitionTable[("q5", "o")] = "q6"
transitionTable[("q6", "o")] = "q3"
transitionTable[("q3", "d")] = "q4"
transitionTable[("q4", " ")] = "q23"
transitionTable[("q23", "f")] = "q5"

# String 'book'
transitionTable[("q0", "b")] = "q7"
transitionTable[("q7", "o")] = "q15"
transitionTable[("q15", "o")] = "q16"
transitionTable[("q16", "k")] = "q4"
transitionTable[("q4", " ")] = "q23"
transitionTable[("q23", "b")] = "q7"

# String 'bike'
transitionTable[("q0", "b")] = "q7"
transitionTable[("q7", "i")] = "q13"
transitionTable[("q13", "k")] = "q14"
transitionTable[("q14", "e")] = "q4"
transitionTable[("q4", " ")] = "q23"
transitionTable[("q23", "b")] = "q7"

idxChar = 0
state = 'q0'
currentToken = ' '

print()
print("Program Lexical Analyzer")

while state != "Accept":
    currentChar = inputKata[idxChar]
    currentToken += currentChar
    state = transitionTable[(state, currentChar)]
    if state == 'q4':
        print("Current token: ", currentToken, " is valid")
        currentToken = " "
    if state == 'Error':
        print("Kesalahan Input.")
        break
    idxChar += 1

if state == 'Accept':
    print('------------------------------------------------------')
    print("semua token yang di input: ", inputKata ," valid")
    print('------------------------------------------------------')
print()
sentence = kata
tokens = sentence.lower().split()
tokens.append('EOS')


print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print("Program Parser")
# Program Parser
# Definisi
non_terminal = ['S', 'NN', 'VB', 'OB']
terminal = ['you', 'we', 'brother', 'cat', 'read', 'buy', 'eat', 'food','book', 'bike']

parse_table = {}

parse_table['S', 'you'] = ['NN', 'VB', 'OB']
parse_table['S', 'we'] = ['NN', 'VB', 'OB']
parse_table['S', 'brother'] = ['NN', 'VB', 'OB']
parse_table['S', 'cat'] = ['NN', 'VB', 'OB']
parse_table['S', 'read'] = ['error']
parse_table['S', 'buy'] = ['error']
parse_table['S', 'eat'] = ['error']
parse_table['S', 'food'] = ['NN', 'VB', 'OB']
parse_table['S', 'book'] = ['NN', 'VB', 'OB']
parse_table['S', 'bike'] = ['NN', 'VB', 'OB']
parse_table['S', 'EOS'] = ['error']

parse_table['NN', 'you'] = ['you']
parse_table['NN', 'we'] = ['we']
parse_table['NN', 'brother'] = ['brother']
parse_table['NN', 'cat'] = ['cat']
parse_table['NN', 'read'] = ['error']
parse_table['NN', 'buy'] = ['error']
parse_table['NN', 'eat'] = ['error']
parse_table['NN', 'food'] = ['error']
parse_table['NN', 'book'] = ['error']
parse_table['NN', 'bike'] = ['error']
parse_table['NN', 'EOS'] = ['error']

parse_table['VB', 'you'] = ['error']
parse_table['VB', 'we'] = ['error']
parse_table['VB', 'brother'] = ['error']
parse_table['VB', 'cat'] = ['error']
parse_table['VB', 'read'] = ['read']
parse_table['VB', 'buy'] = ['buy']
parse_table['VB', 'eat'] = ['eat']
parse_table['VB', 'food'] = ['error']
parse_table['VB', 'book'] = ['error']
parse_table['VB', 'bike'] = ['error']
parse_table['VB', 'EOS'] = ['error']

parse_table['OB', 'you'] = ['error']
parse_table['OB', 'we'] = ['error']
parse_table['OB', 'brother'] = ['error']
parse_table['OB', 'cat'] = ['error']
parse_table['OB', 'read'] = ['error']
parse_table['OB', 'buy'] = ['error']
parse_table['OB', 'eat'] = ['error']
parse_table['OB', 'food'] = ['food']
parse_table['OB', 'book'] = ['book']
parse_table['OB', 'bike'] = ['bike']
parse_table['OB', 'EOS'] = ['error']

# Inisiasi Stack
stack = []
stack.append('#')
stack.append('S')

# Input inisiasi
idx_token = 0
symbol = tokens[idx_token]

# Parsing

while(len(stack) > 0):
    top = stack[len(stack) - 1]
    print('top', top)
    print('symbol', symbol)

    if top in terminal:
        print('top adalah simbol terminal')

        if top == symbol:
            stack.pop()
            idx_token += 1
            symbol = tokens[idx_token]

            if symbol == 'EOS':
                stack.pop()
                print('isi stack: ', stack) 
        else:
            print('error')
            break
    elif top in non_terminal:
        print('top adalah symbol non terminal')
        
        if parse_table[(top, symbol)][0] != 'error':
            stack.pop()
            symbol_pushed = parse_table[(top, symbol)]
            for i in range(len(symbol_pushed)-1, -1, -1):
                stack.append(symbol_pushed[i])
        else:
            print('error')
            break
    else:
        print('error')
        break
    print('isi stack: ', stack)
    print()
    print('------------------------------------------------------')


if symbol == 'EOS' and len(stack) == 0:
    print('input string', '"',  sentence, '"', 'diterima sesuai grammar')
else:
    print('input string error', '"', sentence, '"', 'tidak sesuai grammar')
print('------------------------------------------------------')