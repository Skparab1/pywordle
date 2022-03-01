def clearscreen():
    print('\n'*75)

def startup(): # displays start up animation
    import time
    clearscreen(),clearscreen(),clearscreen(),clearscreen()
    i = 0
    toprint = ''
    # create garage door effect
    while i <= 12:
        clearscreen()
        toprint = toprint + ('-'*100 + '\n')
        print(toprint + ('\n'*(30-i)))
        time.sleep(0.0067)
        i += 1
    while i <= 15:
        clearscreen()
        toprint = toprint + ('-'*26 + ' '*48 + '-'*26 + '\n')
        print(toprint + ('\n'*(30-i)))
        time.sleep(0.0067)
        i += 1
    toprint = toprint + '-'*26 + '            Wordle         Starting up          '+'-'*26+'\n'
    i += 1
    while i <= 18:
        clearscreen()
        toprint = toprint + ('-'*26 + ' '*48 + '-'*26 + '\n')
        print(toprint + ('\n'*(30-i)))
        time.sleep(0.0067)
        i += 1
    while i <= 30:
        clearscreen()
        toprint = toprint + ('-'*100 + '\n')
        print(toprint + ('\n'*(30-i)))
        time.sleep(0.0067) 
        i += 1
    stm = 0.09
    j = 0
    # animate dots
    while j <= 1:
        toprint = toprint.replace('up ','up.')
        clearscreen(), print(toprint), time.sleep(stm)
        toprint = toprint.replace('up. ','up..')
        clearscreen(), print(toprint), time.sleep(stm)
        toprint = toprint.replace('up.. ','up...')
        clearscreen(), print(toprint), time.sleep(stm)
        toprint = toprint.replace('up... ','up....')
        clearscreen(), print(toprint), time.sleep(stm)
        toprint = toprint.replace('up.... ','up.....')
        clearscreen(), print(toprint), time.sleep(stm)
        toprint = toprint.replace('up..... ','up......')
        clearscreen(), print(toprint), time.sleep(stm)
        toprint = toprint.replace('up...... ','up.......')
        clearscreen(), print(toprint), time.sleep(stm)
        toprint = toprint.replace('up....... ','up........')
        clearscreen(), print(toprint), time.sleep(0.2)                            
        toprint = toprint.replace('up........','up .......')
        clearscreen(), print(toprint), time.sleep(stm)
        toprint = toprint.replace('up .......','up  ......')
        clearscreen(), print(toprint), time.sleep(stm)
        toprint = toprint.replace('up  ......','up   .....')
        clearscreen(), print(toprint), time.sleep(stm)
        toprint = toprint.replace('up   .....','up    ....')
        clearscreen(), print(toprint), time.sleep(stm)
        toprint = toprint.replace('up    ....','up     ...')
        clearscreen(), print(toprint), time.sleep(stm)
        toprint = toprint.replace('up     ...','up      ..')
        clearscreen(), print(toprint), time.sleep(stm)
        toprint = toprint.replace('up      ..','up       .')
        clearscreen(), print(toprint), time.sleep(stm)
        toprint = toprint.replace('up       .','up        ')
        clearscreen(), print(toprint), time.sleep(stm)
        toprint = toprint.replace('.',' ')
        clearscreen(), print(toprint), time.sleep(stm)
        j += 1
        stm -= 0.02

    i = 0
    while i <= 30:
        print()
        time.sleep(0.0067) 
        i += 1
