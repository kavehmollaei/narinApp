import time
## sathe mokhtalef morede barresi

x1,x2,y1,y2 = -1.8,1.8,-1.8,1.8
c_real,c_imag= -0.62772,-0.42193

def calc_pure_python(desired_width,max_iterations):
    """ sakhatn list mokhtasate mokhtalef(zs)  va parametrhaye mokhtalet (cs)
            sakhtam julia set va namayes"""
    x_step= float(x2-x1)/float(desired_width)
    y_step= float(y1-y2)/float(desired_width)
    x = []
    y = []
    ycoord = y2

    while ycoord > y1:
        y.append(ycoord)
        ycoord += y_step

    xcoord = x1

    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step

    # sakhtan list az mokhtasat ha va sharayete avalie

    zs = []
    cs = []
    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord,ycoord))
            cs.append(complex(c_real,c_imag))

    print('Length of x:',len(x))
    print('total Elements:',len(zs))
    start_time = time.time()
    output = calculate_z_serial_purepython(max_iterations,zs,cs)
    end_time = time.time()
    secs = end_time -start_time
    print(calculate_z_serial_purepython.__name__+" took",secs,"secends")

def calculate_z_serial_purepython(maxiter,zs,cs):
    """ mohasebe list khooriji ba estefade az hulia update rule"""
  
    output = [0]* len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        while abs(z) < 2 and n < maxiter:
            z = z*z + c
            n+=1
        output[i] 
        return output

calc_pure_python(desired_width=1000,max_iterations=300)           
