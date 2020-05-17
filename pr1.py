import math
import matplotlib.pyplot as plt

def spadek_swobodny():
    z = 0

    print('Podaj znane wartości:')

    print('*możesz wpisać nazwy planet układu słonecznego i księżyc')
    gs = input('przyspiesznie g = ')

    if ',' in gs:
        gs = list(gs)
        index = gs.index(',')
        gs.insert(index,'.')
        gs.remove(',')
        gs = ''.join(gs)

    if gs == 'ziemia':
        gs = '9.81'
    elif gs == 'księżyc':
        gs ='1.6'
    elif gs == 'merkury':
        gs ='3.701'
    elif gs == 'wenus':
        gs ='8.87'
    elif gs == 'mars':
        gs ='3.934'
    elif gs == 'jowisz':
        gs ='24.79'
    elif gs == 'saturn':
        gs ='8.96'
    elif gs == 'uran':
        gs ='8.69'
    elif gs == 'neptun':
        gs ='11'

    hs = input('wysokość H = ')

    if ',' in hs:
        hs = list(hs)
        index = hs.index(',')
        hs.insert(index,'.')
        hs.remove(',')
        hs = ''.join(hs)

    ts = input('czas spadania t = ')

    if ',' in ts:
        ts = list(ts)
        index = ts.index(',')
        ts.insert(index,'.')
        ts.remove(',')
        ts = ''.join(ts)

    ms = input('masa ciała m = ')

    if ',' in ms:
        ms = list(ms)
        index = ms.index(',')
        ms.insert(index,'.')
        ms.remove(',')
        ms = ''.join(ms)

    vs = input('prędkość w chwili uderzenia w ziemie v = ')

    if ',' in vs:
        vs = list(vs)
        index = vs.index(',')
        vs.insert(index,'.')
        vs.remove(',')
        vs = ''.join(vs)

    es = input('energia potencjalna na maksymalnej wysokości oraz energia kinetyczna na zerowej wysokości Ep = Ek = ')

    if ',' in es:
        es = list(es)
        index = es.index(',')
        es.insert(index,'.')
        es.remove(',')
        es = ''.join(es)

    print('\n')

    while z < 7:

        #liczenie g
        if bool(gs) == False and bool(hs) == True and bool(ts) == True:
            hs = float(hs)
            ts = float(ts)
            gs = (2*hs)/(ts*ts)
            print('przyspieszenie g = ',gs, '\n')
            hs = str(hs)
            ts = str(ts)
            gs = str(gs)

        if bool(gs) == False and bool(es) == True and bool(hs) == True and bool(ms) == True:
            es = float(es)
            hs = float(hs)
            ms = float(ms)
            gs = es/(ms*hs)
            print('przyspieszenie g = ', gs, '\n')
            es = str(es)
            hs = str(hs)
            ms = str(ms)
            gs = str(gs)

        if bool(gs) == False and bool(hs) == True and bool(vs) == True:
            hs = float(hs)
            vs = float(vs)
            gs = (vs*vs)/(2*hs)
            hs = str(hs)
            vs = str(vs)
            gs = str(gs)


        #liczenie h
        if bool(hs) == False and bool(gs) == True and bool(ts) == True:
            gs = float(gs)
            ts = float(ts)
            hs = (gs*ts*ts)/2
            print('wysokość H = ', hs, '\n')
            gs = str(gs)
            ts = str(ts)
            hs = str(hs)

        if bool(hs) == False and bool(es) == True and bool(ms) == True and bool(gs) == True:
            es = float(es)
            gs = float(gs)
            ms = float(ms)
            hs = es/(ms*gs)
            print('wysokość H = ', hs, '\n')
            es = str(es)
            gs = str(gs)
            ms = str(ms)
            hs = str(hs)

        if bool(hs) == False and bool(gs) == True and bool(vs) == True:
            gs = float(gs)
            vs = float(vs)
            hs = (vs*vs)/(2*gs)
            print('wysokość H = ', hs, '\n')
            gs = str(gs)
            vs = str(vs)
            hs = str(hs)

        #liczenie t
        if bool(ts) == False and bool(hs) == True and bool(gs) == True:
            hs = float(hs)
            gs = float(gs)
            ts = math.sqrt((2*hs)/gs)
            print('czas spadania t = ', ts, '\n')
            hs = str(hs)
            gs = str(gs)
            ts = str(ts)

        #liczenie m
        if bool(ms) == False and bool(es) == True and bool(gs) == True and bool(hs) == True:
            es = float(es)
            gs = float(gs)
            hs = float(hs)
            ms = es/(gs*hs)
            print('masa ciała m = ', ms, '\n')
            es = str(es)
            gs = str(gs)
            hs = str(hs)
            ms = str(ms)

        if bool(ms) == False and bool(es) == True and bool(vs) == True:
            es = float(es)
            vs = float(vs)
            ms = (es*vs*vs)/2
            print('masa ciała m = ', ms, '\n')
            es = str(es)
            vs = str(vs)
            ms = str(ms)

        #liczenie v
        if bool(vs) == False and bool(gs) == True and bool(ts) == True:
            gs = float(gs)
            ts = float(ts)
            vs = gs*ts
            print('prędkość w chwili uderzenia w ziemie v = ', vs, '\n')
            gs = str(gs)
            ts = str(ts)
            vs = str(vs)

        if bool(vs) == False and bool(gs) == True and bool(hs) == True:
            gs = float(gs)
            hs = float(hs)
            vs = math.sqrt(2*gs*hs)
            print('prędkość w chwili uderzenia w ziemie v = ', vs, '\n')
            gs = str(gs)
            hs = str(hs)
            vs = str(vs)

        #liczenie energii
        if bool(es) == False :          
            if bool(ms) == True and bool(gs) == True and bool(hs):
                ms = float(ms)
                gs = float(gs)
                hs = float(hs)
                es = ms*gs*hs
                print('energia potencjalna i kinetyczna wynoszą Ep = Ek = ', es, '\n')
                ms = str(ms)
                gs = str(gs)
                hs = str(hs)
                es = str(es)
            elif bool(vs) == True and bool(ms) == bool:
                vs = float(vs)
                ms = float(ms)
                es = (ms*vs*vs)/2
                print('energia potencjalna i kinetyczna wynoszą Ep = Ek = ', es, '\n')
                ms = str(ms)
                vs = str(vs)
                es = str(es)
        
        if bool(gs) == True and bool(hs) == True and bool(ts) == True and bool(ms) == True and bool(vs) == True and bool(es) == True:
            print('Wszystko wartości zostały obliczone')
            break
        
        z = z + 1

    print('\n')
    print('WYNIK: \n')
    if bool(gs) == True:
        print('przyspiesznie: \ng = ', gs, ' m/s2\n')
    if bool(hs) == True:
        print('wysokość: \nH = ', hs, ' m\n')
    if bool(ts) == True:
        print('czas spadania: \nt = ', ts, ' s\n')
    if bool(ms) == True:
        print('masa ciała: \nm = ', ms, ' kg\n')
    if bool(vs) == True:
        print('prędkość w chwili uderzenia w ziemie: \nv = ', vs, ' m/s\n')
    if bool(es) == True:
        print('energia potencjalna na maksymalnej wysokości oraz energia kinetyczna na zerowej wysokości: \nEp = Ek = ', es ,' J\n')

    if bool(ts) == True and bool(gs) == True:
        #zamiana wartości na int
        ts = float(ts)
        ts = ts*1000
        ts = str(ts)
        ts = list(ts)
        a = ts.index('.')
        b = list(ts[:(a)])
        ts = ''.join(b)
        ts = int(ts)

        #tworzenie wykresu
        w = range(0, ts, 1)
        y = []
        x = []

        for i in w:
            y.append(((float(gs)*i*i)/2)/1000000)
            x.append(i/1000)

        plt.plot(x, y)
        plt.title('Wykres drogi od czasu')
        plt.grid(True)
        plt.xlabel('s')
        plt.ylabel('m')
        plt.draw()
        plt.show()











