def rownia_pochyla():

    print('Podaj znane wartości:')
    k = input('kąt między Q a Fx(N) k=')

    if ',' in k:
        k = list(k)
        index = k.index(',')
        k.insert(index,'.')
        k.remove(',')
        k = ''.join(k)

    l = input('kąt między Q a Fy l=')

    if ',' in l:
        l = list(l)
        index = l.index(',')
        l.insert(index,'.')
        l.remove(',')
        l = ''.join(l)

    q = input('siła grawitacji Q=')

    if ',' in q:
        q = list(q)
        index = q.index(',')
        q.insert(index,'.')
        q.remove(',')
        q = ''.join(q)

    fx = input('składowa siła pozioma Qx=')

    if ',' in fx:
        fx = list(fx)
        index = fx.index(',')
        fx.insert(index,'.')
        fx.remove(',')
        fx = ''.join(fx)

    fy = input('nacisk (składowa siła pionowa) N=')

    if ',' in fy:
        fy = list(fy)
        index = fy.index(',')
        fy.insert(index,'.')
        fy.remove(',')
        fy = ''.join(fy)

    print('*możesz wpisać "ziemia"')
    g = input('przyspiesznie grawitacyjne g=')

    if ',' in g:
        g = list(g)
        index = g.index(',')
        g.insert(index,'.')
        g.remove(',')
        g = ''.join(g)

    if g == 'ziemia':
        g = '9.81'

    m = input('masa ciała m=')

    if ',' in m:
        m = list(m)
        index = m.index(',')
        m.insert(index,'.')
        m.remove(',')
        m = ''.join(m)

    ft = input('siła tarcia T=')

    if ',' in ft:
        ft = list(ft)
        index = ft.index(',')
        ft.insert(index,'.')
        ft.remove(',')
        ft = ''.join(ft)

    u = input('współczynnik tarcia u=')

    if ',' in u:
        u = list(u)
        index = u.index(',')
        u.insert(index,'.')
        u.remove(',')
        u = ''.join(u)

    fw = False
    a = False

    d = input("długość równi d=")

    if ',' in d:
        d = list(d)
        index = d.index(',')
        d.insert(index,'.')
        d.remove(',')
        d = ''.join(d)

    h = input ("wysokość równi h=")
    if ',' in h:
        h = list(h)
        index = h.index(',')
        h.insert(index,'.')
        h.remove(',')
        h = ''.join(h)
        
    t = False


    if bool(k) == True:
        k = float(k)
        k = math.radians(k)
        k = str(k)

    if bool(l) == True:
        l = float(l)
        l = math.radians(l)
        l = str(l)

    print('\n')
    z = 0
    
    while z < 8:

        # liczenie l
        if bool(l) == False and bool(k) == True:
            k = float(k)
            l = math.radians(90) - k
            print('kąt między Fx a Q (radiany) k=', k)
            l = float(l)
            k = str(k)

        # liczenie k
        if bool(k) == False and bool(l) == True:
            l = float(l)
            k = math.radians(90) - l
            print('kąt między Fx a Q (radiany) k=', k)
            l = str(l)
            k = str(k)

        if bool(k) == False and bool(fy) == True and bool(fx) == True and float(fx) > 0:
            fy = float(fy)
            fx = float(fx)
            k = math.atan(fy/fx)
            print('kąt między Fx a Q (radiany) k=', k)
            fy = str(fy)
            fx = str(fx)
            k = str(k)

        if bool(k) == False and bool(fy) == True and bool(q) == True and float(q) > 0:
            fy = float(fy)
            q = float(q)
            k = math.asin(fy/q)
            print('kąt między Fx a Q (radiany) k=', k)
            fy = str(fy)
            q = str(q)
            k = str(k)

        if bool(k) == False and bool(fx) == True and bool(q) == True and float(q) > 0:
            fx = float(fx)
            q = float(q)
            k = math.acos(fx/q)
            print('kąt między Fx a Q (radiany) k=', k)
            fx = str(fx)
            q = str(q)
            k = str(k)

        # liczenie q
        if bool(q) == False and bool(m) == True and bool(g) == True:
            m = float(m)
            g = float(g)
            q = m*g
            print('siła grawitacji Q=', q)
            m = str(m)
            g = str(g)
            q = str(q)
            print(bool(q))

        if bool(q) == False and bool(fy) == True and bool(fx) == True:
            fy = float(fy)
            fx = float(fx)
            q = math.sqrt((fy*fy)+(fx*fx))
            print('siła grawitacji Q=', q)
            fy = str(fy)
            fx = str(fx)
            q = str(q)

        if bool(q) == False and bool(k) == True and bool(fx) == True:
            k = float(k)
            fx = float(fx)
            q = fx/(math.cos(k))
            print('siła grawitacji Q=', q)
            k = str(k)
            fx = str(fx)
            q = str(q)

        if bool(q) == False and bool(fy) == True and bool(k) == True:
            fy = float(fy)
            k = float(k)
            q = fy/(math.sin(k))
            print('siła grawitacji Q=', q)
            fy = str(fy)
            k = str(k)
            q = str(q)

        #liczenie fy
        if bool(fy) == False and bool(q) == True and bool(fx) == True:
            q = float(q)
            fx = float(fx)
            fy = math.sqrt((q*q)-(fx*fx))
            print('pionowa składowa siły N=', fy)  
            q = str(q)
            fx = str(fx)
            fy = str(fy)

        if bool(fy) == False and bool(q) == True and bool(k) == True:
            q = float(q)
            k = float(k)
            fy = q*(math.sin(k))
            print('pionowa składowa siły N=', fy) 
            q = str(q)
            k = str(k)
            fy = str(fy)

        if bool(fy) == False and bool(k) == True and bool(fx) == True:
            k = float(k)
            fx = float(fx)
            fy = fx*math.tan(k)
            print('pionowa składowa siły N=', fy)  
            k = str(k)
            fx = str(fx)
            fy = str(fy)

        #liczenie fx
        if bool(fx) == False and bool(q) == True and bool(fy) == True:
            q = float(q)
            fy = float(fy)
            fx = math.sqrt((q*q)-(fy*fy))
            print('pozioma składowa Qx=', fx)
            q = str(q)
            fy = str(fy)
            fx = str(fx)

        if bool(fx) == False and bool(q) == True and bool(k) == True:
            q = float(q)
            k = float(k)
            fx = q*(math.cos(k))
            print('pozioma składowa Qx', fx)
            q = str(q)
            k = str(k)
            fx = str(fx)

        if bool(fx) == False and bool(k) == True and bool(fy) == True:
            k = float(k)
            fy = float(fy)
            fx = fy/(math.tan(k))
            print('pozioma składowa Qx', fx)
            k = str(k)
            fy = str(fy)
            fx = str(fx)

        #liczenie ft
        if bool(ft) == False and bool(u) == True and bool(fy) == True:
            u = float(u)
            fy = float(fy)
            ft = u * fy
            print('siła tarcia T=', ft)
            u = str(u)
            fy = str(fy)
            ft = str(ft)

        #liczenie u
        if bool(u) == False and bool(ft) == True and bool(fy) == True:
            ft = float(ft)
            fy = float(fy)
            u = ft/fy
            print('współczynnik tarcia u=', u)
            ft = str(ft)
            fy = str(fy)
            u = str(u)
        
        #liczenie m
        if bool(m) == False and bool(q) == True and bool(g) == True:
            q = float(q)
            g = float(g)
            m = q/g
            print('masa ciała m=', m)
            q = str(q)
            g = str(g)
            m = str(m)

        #liczenie fw
        if bool(fw) == False and bool(fx) == True and bool(ft) == True:
            fx = float(fx)
            ft = float(ft)
            fw = fx-ft
            print('siła wypadkowa', fw)
            fx = str(fx)
            ft = str(ft)
            fw = str(fw)

        #liczenie a
        if bool(a) == False and bool(fw) == True and bool(m) == True:
            fw = float(fw)
            m = float(m)
            a = fw/m
            print('przyspieszenie a=', a)
            fw = str(fw)
            m = str(m)
            a = str(a)

        #liczenie d
        if bool(d) == False and bool(h) == True and bool(k) == True:
            h = float(h)
            k = float(k)
            d = h/math.cos(h)
            print('długość równi d=', d)
            h = str(h)
            k = str(k)
            d = str(h)

        #licznie h
        if bool(h) == False and bool(d) == True and bool(k) == True:
            d = float(d)
            k = float(k)
            h = d*math.cos(k)
            print('wysokość równi h=', h)
            d = str(d)
            k = str(k)
            h = str(h)

        #liczenie t
        if bool(t) == False and bool(d) == True and bool(a) == True:
            d = float(d)
            a = float(d)
            t = math.sqrt((2*d)/a)
            print('czas zsuwania się z równi t=', t)
            d = str(d)
            a = str(d)
            t = str(t)

        z = z + 1
    print('\n')
    print('WYNIKI:')
    if bool(k) == True:
        k = float(k)
        k = math.degrees(k)
        print('kąt między Q a Fx(N): \nk = ', k,' *\n')
        k = math.radians(k)
        k = str(k)
    if bool(l) == True:
        l = float(l)
        l = math.degrees(l)
        print('kąt między Q a Fy: \nl = ', l,' *\n')
        l = math.radians(l)
        l = str(l)
    if bool(q) == True:
        print('siła grawitacji: \nQ = ', q, ' N\n')
    if bool(fx) == True:
        print('składowa siła pozioma: \nQx = ', fx, ' N\n')
    if bool(fy) == True:
        print('nacisk (składowa siła pionowa): \nN = ', fy, 'N\n')
    if bool(g) == True:
        print('przyspiesznie grawitacyjne: \ng = ', g, ' m/s2\n')
    if bool(m) == True:
        print('masa ciała: \nm = ', m, ' kg\n')
    if bool(ft) == True:
        print('siła tarcia: \nT = ', ft, ' N\n')
    if bool(u) == True:
        print('współczynnik tarcia: \nu = ', u, '\n')
    if bool(fw) == True:
        print('siła wypadkowa: \nfw = ', fw, ' N\n')
    if bool(a) == True:
        print('przyspieszenie: \na = ', a, ' m/s2\n')
    if bool(d) == True:
        print("długość równi: \nd = ", d, ' m\n')
    if bool(h) == True:
        print("wysokość równi: \nh = ", h, ' m\n')
    if bool(t) == True:
        print('czas zsuwania się z równi: \nt = ', t, ' s\n')

