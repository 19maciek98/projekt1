def rzut_ukosny():

    k = 0

    print('Podaj znane wartości początkowe:')
    print('*możesz wpisać nazwy planet układu słonecznego i księżyc')
    g = input('przyspiesznie g=')

    if ',' in g:
        g = list(g)
        index = g.index(',')
        g.insert(index,'.')
        g.remove(',')
        g = ''.join(g)

    if g == 'ziemia':
        g = '9.81'
    elif g == 'księżyc':
        g ='1.6'
    elif g == 'merkury':
        g ='3.701'
    elif g == 'wenus':
        g ='8.87'
    elif g == 'mars':
        g ='3.934'
    elif g == 'jowisz':
        g ='24.79'
    elif g == 'saturn':
        g ='8.96'
    elif g == 'uran':
        g ='8.69'
    elif g == 'neptun':
        g ='11'

    h = input('wysokość początkowa h=')

    if ',' in h:
        h = list(h)
        index = h.index(',')
        h.insert(index,'.')
        h.remove(',')
        h = ''.join(h)

    v0 = input('prędkość początkowa vp=')

    if ',' in v0:
        v0 = list(v0)
        index = v0.index(',')
        v0.insert(index,'.')
        v0.remove(',')
        v0 = ''.join(v0)

    a = input('kąt rzutu w stopniach a=')

    if ',' in a:
        a = list(a)
        index = a.index(',')
        a.insert(index,'.')
        a.remove(',')
        a = ''.join(a)

    vx = input('prędkość pozioma vx=')

    if ',' in vx:
        vx = list(vx)
        index = vx.index(',')
        vx.insert(index,'.')
        vx.remove(',')
        vx = ''.join(vx)

    vy0 = input('prędkość początkowa pionowa vpy=')

    if ',' in vy0:
        vy0 = list(vy0)
        index = vy0.index(',')
        vy0.insert(index,'.')
        vy0.remove(',')
        vy0 = ''.join(vy0)
    
    hm = False
    t2 = False
    t1 = False
    tc = False
    z = False
    vyk = False
    vk = False
    ak = False

    if bool(a) == True:
        a = float(a)
        a = math.radians(a)
        a = str(a)

    print('\n')

    while k < 6:

        #liczenie a
        if bool(a) == False and bool(vy0) == True and bool(vx) == True and float(vx) > 0:
            vy0 = float(vy0)
            vx = float(vx)
            a = math.atan(vy0/vx)
            print('kąt rzutu w stopniach a=', a)
            vy0 = str(vy0)
            vx = str(vx)
            a = str(a)

        if bool(a) == False and bool(vy0) == True and bool(v0) == True and float(v0) > 0:
            vy0 = float(vy0)
            v0 = float(v0)
            a = math.asin(vy0/v0)
            print('kąt rzutu w stopniach a=', a)
            vy0 = str(vy0)
            v0 = str(v0)
            a = str(a)

        if bool(a) == False and bool(vx) == True and bool(v0) == True and float(v0) > 0:
            vx = float(vx)
            v0 = float(v0)
            a = math.acos(vx/v0)
            print('kąt rzutu w stopniach a=', a)
            vx = str(vx)
            v0 = str(v0)
            a = str(a)

        #liczenie h
        if bool(h) == False:
            h = '0'

        # liczenie v0
        if bool(v0) == False and bool(vy0) == True and bool(vx) == True:
            vy0 = float(vy0)
            vx = float(vx)
            v0 = math.sqrt((vy0*vy0)+(vx*vx))
            print('prędkość początkowa vp=', v0)
            vy0 = str(vy0)
            vx = str(vx)
            v0 = str(v0)

        if bool(v0) == False and bool(a) == True and bool(vx) == True:
            a = float(a)
            vx = float(vx)
            v0 = vx/(math.cos(a))
            print('prędkość początkowa vp=', v0)
            a = str(a)
            vx = str(vx)
            v0 = str(v0)

        if bool(v0) == False and bool(vy0) == True and bool(a) == True:
            vy0 = float(vy0)
            a = float(a)
            v0 = vy0/(math.sin(a))
            print('prędkość początkowa vp=', v0)
            vy0 = str(vy0)
            a = str(a)
            v0 = str(v0)

        #liczenie vy0
        if bool(vy0) == False and bool(v0) == True and bool(vx) == True:
            v0 = float(v0)
            vx = float(vx)
            vy0 = math.sqrt((v0*v0)-(vx*vx))
            print('prędkość początkowa pionowa vpy=', vy0)  
            v0 = str(v0)
            vx = str(vx)
            vy0 = str(vy0)

        if bool(vy0) == False and bool(v0) == True and bool(a) == True:
            v0 = float(v0)
            a = float(a)
            vy0 = v0*(math.sin(a))
            print('prędkość początkowa pionowa vpy=', vy0)
            v0 = str(v0)
            a = str(a)
            vy0 = str(vy0)

        if bool(vy0) == False and bool(a) == True and bool(vx) == True:
            a = float(a)
            vx = float(vx)
            vy0 = vx*math.tan(a)
            print('prędkość początkowa pionowa vpy=', vy0) 
            a = str(a)
            vx = str(vx)
            vy0 = str(vy0)

        #liczenie vx
        if bool(vx) == False and bool(v0) == True and bool(vy0) == True:
            v0 = float(v0)
            vy0 = float(vy0)
            vx = math.sqrt((v0*v0)-(vy0*vy0))
            print('prędkość pozioma vx=', vx)
            v0 = str(v0)
            vy0 = str(vy0)
            vx = str(vx)

        if bool(vx) == False and bool(v0) == True and bool(a) == True:
            v0 = float(v0)
            a = float(a)
            vx = v0*(math.cos(a))
            print('prędkość pozioma vx=', vx)
            v0 = str(v0)
            a = str(a)
            vx = str(vx)

        if bool(vx) == False and bool(a) == True and bool(vy0) == True:
            a = float(a)
            vy0 = float(vy0)
            vx = vy0/(math.tan(a))
            print('prędkość pozioma vx=', vx)
            a = str(a)
            vy0 = str(vy0)
            vx = str(vx)

        #liczenie hm
        if bool(hm) == False and bool(vy0) == True and bool(g) == True:
            h = float(h)
            vy0 = float(vy0)
            g = float(g)
            hm = ((vy0*vy0)/(2*g))+h
            print('maksymalna wysokość H=', hm)
            vy0 = str(vy0)
            g = str(g)
            hm = str(hm)
            h = str(h)

        #liczenie t2 czyli t spadania z hm
        if bool(t2) == False and bool(hm) == True and bool(g) == True:
            hm = float(hm)
            g = float(g)
            t2 = math.sqrt((2*hm)/g)
            print('czas spadania z maksymalnej wysokości wynosi t2=', t2)
            hm = str(hm)
            g = str(g)
            t2 = str(t2)

        #liczenie t1 czyli czasu między h a hm
        if bool(t1) == False and bool(vy0) == True and bool(g) == True:
            vy0 = float(vy0)
            g = float(g)
            t1 = vy0/g
            print('czas wznoszenia t1=', t1)
            vy0 = str(vy0)
            g = str(g)
            t1 = str(t1)

        #liczenie tc
        if bool(tc) == False and bool(t1) == True and bool(t2) == True:
            t1 = float(t1)
            t2 = float(t2)
            tc = t1 + t2
            print('całkowity czas ruchu tc=', tc)
            t1 = str(t1)
            t2 = str(t2)
            tc = str(tc)

        #liczenie z
        if bool(z) == False and bool(tc) == True and bool(vx) == True:
            tc = float(tc)
            vx = float(vx)
            z = vx*tc
            print('zasięg rzutu z=', z)
            tc = str(tc)
            vx = str(vx)
            z = str(z)

        #liczenie vyk
        if bool(vyk) == False and bool(vy0) == True and bool(g) == True and bool(tc) == True:
            vy0 = float(vy0)
            g = float(g)
            tc = float(tc)
            vyk = vy0-(g*tc)
            print('prędkość pionowa końcowa vky=', vyk)
            vy0 = str(vy0)
            g = str(g)
            tc = str(tc)
            vyk = str(vyk)

        #zliczanie końcowego kąta ak
        if bool(ak) == False and bool(vyk) == True and bool(vx) == True and float(vx) > 0:
            vyk = float(vyk)
            vx = float(vx)
            ak = math.atan(math.fabs(vyk)/vx)
            print('kąt nachylenia vk do płaszczyzny ak=', ak)
            vyk = str(vyk)
            vx = str(vx)
            ak = str(ak)

        #zliczanie vk
        if bool(vk) == False and bool(vyk) == True and bool(vx) == True:
            vyk = float(vyk)
            vx = float(vx)
            vk = math.sqrt((vx*vx)+(vyk*vyk))
            print('prędkość końcowa vk=', vk)
            vyk = str(vyk)
            vx = str(vx)
            vk = str(vk)

        #zerwanie pętli
        if bool(g) == True and bool(h) == True and bool(v0) == True and bool(a) == True and bool(vx) == True and bool(vy0) == True and bool(hm) == True and bool(tc) == True and bool(z) == True and bool(vyk) == True and bool(ak) == True and bool(vk) == True:
            print('wszystkie wielkości zostały obliczone')
            break

        k = k + 1

    print('\n')
    print('WYNIKI:\n')
    if bool(g) == True:
        print('przyspiesznie: \ng = ', g, ' m/s2\n')
    if bool(h) == True:
        print('wysokość początkowa: \nh = ', h, ' m\n')
    if bool(v0) == True:
        print('prędkość początkowa: \nvp = ', v0, ' m/s\n')
    if bool(a) == True:
        a = float(a)
        a = math.degrees(a)
        print('kąt rzutu w stopniach: \na = ', a,' *\n')
        a = math.radians(a)
        a = str(a)
    if bool(vx) == True:
        print('prędkość pozioma: \nvx = ', vx, ' m/sv\n')
    if bool(vy0) == True:
        print('prędkość początkowa pionowa: \nvpy = ', vy0, ' m/s\n')
    if bool(hm) == True:
        print('wysokość maksymalna: \nH = ', hm, ' m\n')
    if bool(tc) == True:
        print('czas ruchu: \ntc = ', tc, ' s\n')
    if bool(z) == True:
        print('zasięg rzutu: \nz = ', z, ' m\n')
    if bool(vyk) == True:
        print('prędkość pionowa końcowa: \nvky = ', vyk, ' m/s\n')
    if bool(ak) == True:
        ak = float(ak)
        ak = math.degrees(ak)
        print('kąt nachylenia vk do płaszczyzny: \nak = ', ak, ' *\n')
        ak = math.radians(ak)
        ak = str(ak)
    if bool(vk) == True:
        print('prędkość końcowa: \nvk = ', vk, ' m/s\n')

    #wykres y(x)
    if bool(tc) == True: 

        tc = float(tc)
        tc = tc*1000
        tc = str(tc)
        tc = list(tc)
        a = tc.index('.')
        b = list(tc[:(a)])
        tc = ''.join(b)
        tc = int(tc)

        x = []
        y = []
        w = range(0,tc,1)

        vx = float(vx)
        g = float(g)
        vy0 = float(vy0)
        h = float(h)

        for i in w:
            x.append((vx*i)/1000)
            y.append(h+((vy0*i)/1000)-(((g*i*i)/2)/1000000))

        plt.plot(x, y)
        plt.title('Wykres Y(x)')
        plt.grid(True)
        plt.xlabel('m')
        plt.ylabel('m')
        plt.draw()
        plt.show()