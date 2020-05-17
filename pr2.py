import math
import matplotlib.pyplot as plt
def ruch_postepowy():

    z = 0

    print('Podaj znane wartości:')

    ap = input('przyspiesznie a=')

    if ',' in ap:
        ap = list(ap)
        index = ap.index(',')
        ap.insert(index,'.')
        ap.remove(',')
        ap = ''.join(ap)

    v0p = input('prędkość początkowa vp=')

    if ',' in v0p:
        v0p = list(v0p)
        index = v0p.index(',')
        v0p.insert(index,'.')
        v0p.remove(',')
        v0p = ''.join(v0p)

    vp = input('prędkość końcowa v=')

    if ',' in vp:
        vp = list(vp)
        index = vp.index(',')
        vp.insert(index,'.')
        vp.remove(',')
        vp = ''.join(vp)

    x0p = input('położenie początkowe xp=')

    if ',' in x0p:
        x0p = list(x0p)
        index = x0p.index(',')
        x0p.insert(index,'.')
        x0p.remove(',')
        x0p = ''.join(x0p)

    xp = input('położenie końcowe x=')

    if ',' in xp:
        xp = list(xp)
        index = xp.index(',')
        xp.insert(index,'.')
        xp.remove(',')
        xp = ''.join(xp)

    fp = input('wypadkowa siła działająca na ciało F=')

    if ',' in fp:
        fp = list(fp)
        index = fp.index(',')
        fp.insert(index,'.')
        fp.remove(',')
        fp = ''.join(fp)

    mp = input('masa ciała m=')

    if ',' in mp:
        mp = list(mp)
        index = mp.index(',')
        mp.insert(index,'.')
        mp.remove(',')
        mp = ''.join(mp)

    tp = input('czas ruchu t=')

    if ',' in tp:
        tp = list(tp)
        index = tp.index(',')
        tp.insert(index,'.')
        tp.remove(',')
        tp = ''.join(tp)

    sp = input('pokonana droga s=')

    if ',' in sp:
        sp = list(sp)
        index = sp.index(',')
        sp.insert(index,'.')
        sp.remove(',')
        sp = ''.join(sp)

    print('\n')

    while z < 8:

        #liczenie F
        if bool(fp) == False and bool(mp) == True and bool(ap) == True:
            mp = float(mp)
            ap = float(ap)
            fp = mp*ap
            print('wypadkowa siła działająca na ciało F = ', fp, '\n')
            mp = str(mp)
            ap = str(ap)
            fp = str(fp)

        #liczenie m
        if bool(mp) == False and bool(fp) == True and bool(ap) == True:
            fp = float(fp)
            ap = float(ap)
            mp = fp/ap
            print('masa ciała m = ', mp, '\n')
            mp = str(mp)
            ap = str(ap)
            fp = str(fp)

        #liczenie a
        if bool(ap) == False and bool(fp) == True and bool(mp) == True:
            fp = float(fp)
            mp = float(mp)
            ap = fp/mp
            print('przyspieszenie a = ', ap, '\n')
            mp = str(mp)
            ap = str(ap)
            fp = str(fp)

        #liczenie x
        if bool(xp) == False and bool(sp) == True and bool(x0p) == True :
            sp = float(sp)
            x0p = float(x0p)
            xp = x0p + sp
            print('położenie końcowe x = ', xp, '\n')
            sp = str(sp)
            x0p = str(x0p)
            xp = str(xp)

        #liczenie xp
        if bool(x0p) == False and bool(xp) == True and bool(sp) == True:
            sp = float(sp)
            xp = float(xp)
            x0p = xp - sp
            print('położenie początkowe xp = ', x0p, '\n')
            sp = str(sp)
            xp = str(xp)
            x0p = str(x0p)
    
        #liczenie a
        if bool(ap) == False and bool(vp) == True and bool(tp) == True and bool(v0p) == True:
            vp = float(vp)
            tp = float(tp)
            v0p = float(v0p)
            ap = (vp - v0p)/tp
            print('przyspieszenie a = ', ap, '\n')
            vp = str(vp)
            tp = str(tp)
            v0p = str(v0p)
            ap = str(ap)
   
        if bool(ap) == False and bool(xp) == True and bool(x0p) == True and bool(v0p) == True and bool(tp) == True:
            xp = float(xp)
            x0p = float(x0p)
            v0p = float(v0p)
            tp = float(tp)
            ap = ((2*xp) - (2*x0p) - (2*v0p*tp))/(tp*tp)
            sp = xp - x0p
            print('przyspieszenie a = ', ap, '\n')
            xp = str(xp)
            x0p = str(x0p)
            v0p = str(v0p)
            tp = str(tp)
            ap = str(ap)
        
        #liczenie x
        if bool(xp) == False and bool(xp) == False and bool(ap) == True and bool(x0p) == True and bool(v0p) == True and bool(tp) == True:
            ap = float(ap)
            x0p = float(x0p)
            v0p = float(v0p)
            tp = float(tp)
            xp = x0p + (v0p*tp) + ((ap*tp*tp)/2)
            print('położenie końcowe x = ', xp, '\n')
            ap = str(ap)
            x0p = str(x0p)
            v0p = str(v0p)
            tp = str(tp)
            xp = str(xp)

        #liczenie s
        if bool(sp) == False:
            if bool(x0p) == True and bool(xp) == True:
                x0p = float(x0p)
                xp = float(xp)
                sp = xp - x0p
                sp = math.fabs(sp)
                print('przebyta droga s = ', sp, '\n')
                x0p = str(x0p)
                xp = str(xp)
                sp = str(sp)
            elif bool(v0p) == True and bool(tp) == True and bool(ap) == True:
                v0p = float(v0p)
                tp = float(tp)
                ap = float(ap)
                sp = (v0p*tp)+((ap*tp*tp)/2)
                print('przebyta droga s = ', sp, '\n')
                v0p = str(v0p)
                tp = str(tp)
                ap = str(ap)
                sp = str(sp)

        #liczenie t
        if bool(tp) == False and bool(vp) == True and bool(v0p) == True and bool(ap) == True and float(ap) != 0:
            vp = float(vp)
            v0p = float(v0p)
            ap = float(ap)
            tp = (vp - v0p)/ap
            print('Czas ruchu t = ', tp, '\n')
            vp = str(vp)
            v0p = str(v0p)
            ap = str(ap)
            tp = str(tp)

        if bool(tp) == False and bool(sp) == True and bool(v0p) == True and float(ap) == 0:
            sp = float(sp)
            v0p = float(v0p)
            tp = sp/v0p
            print('Czas ruchu t = ', tp, '\n')
            sp = str(sp)
            v0p = str(v0p)
            tp = str(tp)

        #liczenie t z równania kwadratowego
        if  bool(tp) == False and bool(ap) == True and bool(v0p) == True and bool(xp) == True and bool(x0p) == True:
            x0p = float(x0p)
            xp = float(xp)
            v0p = float(v0p)
            ap = float(ap)
            c = x0p - xp
            b = v0p
            a = ap/2
            delta = (b*b) - (4*a*c)
            x0p = str(x0p)
            xp = str(xp)
            v0p = str(v0p)
            ap = str(ap)
            tp = str(tp)
            if delta > 0:
                pdelta = math.sqrt(delta)
                tp1 = (-b + pdelta)/(2*a)
                tp2 = (-b - pdelta)/(2*a)
                if tp1 > 0:
                    tp = tp1
                    print('czas ruchu t = ', tp, '\n')
                elif tp2 > 0:
                    tp = tp2
                    print('czas ruchu t = ', tp, '\n')
                else:
                    print('Nie da się obliczyć czasu trwania ruchu', '\n')
            elif delta == 0:
                tp = (-b)/(2*a)
                print('czas ruchu t = ', tp, '\n')
            else:
                print('Nie da się obliczyć czasu trwania ruchu', '\n')

        #liczenie v
        if bool(vp) == False and bool(v0p) == True and bool(ap) == True and bool(tp) == True:
            v0p = float(v0p)
            ap = float(ap)
            tp = float(tp)
            vp = v0p + (ap * tp)
            print('prędkość końcowa V = ', vp, '\n')
            v0p = str(v0p)
            ap = str(ap)
            tp = str(tp)
            vp = str(vp)

        #liczenie vp
        if bool(v0p) == False and bool(vp) == True and bool(ap) == True and bool(tp) == True:
            vp = float(vp)
            ap = float(ap)
            tp = float(tp)
            v0p = vp - (ap * tp)
            print('prędkość początkowa Vp = ', v0p, '\n')
            vp = str(vp)
            ap = str(ap)
            tp = str(tp)
            v0p = str(v0p)

        if bool(v0p) == False and bool(xp) == True and bool(x0p) == True and bool(tp) == True and bool(ap) == True:
            xp = float(xp)
            x0p = float(x0p)
            tp = float(tp)
            ap = float(ap)
            v0p = ((xp - x0p)/tp)-((ap*tp)/2)
            print('prędkość początkowa Vp = ', v0p, '\n')
            xp = str(xp)
            x0p = str(x0p)
            tp = str(tp)
            ap = str(ap)
            v0p = str(v0p)

        #liczenie xp
        if bool(x0p) == False and  bool(sp) == True and bool(xp) == True:
            xp = float(xp)
            sp = float(sp)
            x0p = xp - sp
            print('położenie początkowe xp = ', x0p, '\n')
            xp = str(xp)
            sp = str(sp)
            x0p = str(x0p)


        if bool(ap) == True and bool(xp) == True and bool(x0p) == True and bool(v0p) == True and bool(tp) == True and bool(vp) == True and bool(sp) == True and bool(fp) == True and bool(mp) == True:
            print('wszystkie wartości są policzone', )
            break

        z = z + 1
    
    print('\n')
    print('WYNIK:\n ')
    if bool(ap) == True:
        print('przyspiesznie: \na = ', ap , " m/s2\n")
    if bool(v0p) == True:
        print('prędkość początkowa: \nvp = ', v0p , ' m/s\n')
    if bool(vp) == True:
        print('prędkość końcowa: \nv = ', vp ,' m/s\n')
    if bool(x0p) == True:
        print('położenie początkowe: \nxp = ', x0p ,' m\n')
    if bool(xp) == True:
        print('położenie końcowe: \nx = ', xp ,' m\n')
    if bool(fp) == True:
        print('wypadkowa siła działająca na ciało: \nF = ', fp , ' N\n')
    if bool(mp) == True:
        print('masa ciała: \nm = ', mp , ' kg\n')
    if bool(tp) == True:
        print('czas ruchu: \nt = ', tp , ' s\n')
    if bool(sp) == True:
        print('pokonana droga: \ns = ', sp , ' m\n')

    if bool(tp) == True and bool(ap) == True: 
        #zamiana wartości na int
        tp = float(tp)
        tp = tp*1000
        tp = str(tp)
        tp = list(tp)
        a = tp.index('.')
        b = list(tp[:(a)])
        tp = ''.join(b)
        tp = int(tp)

        #tworzenie wykresu
        w = range(0, tp, 1)
        y = []
        x = []

        for i in w:
            y.append(((float(ap)*i*i)/2)/1000000)
            x.append(i/1000)

        plt.plot(x, y)
        plt.title('Wykres x(t)')
        plt.grid(True)
        plt.xlabel('s')
        plt.ylabel('m')
        plt.draw()
        plt.show()

