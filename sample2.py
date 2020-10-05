import time
from PIL import Image

import array


x1,x2,y1,y2 = -1.8,1.8,-1.8,1.8
c_real,c_imag= -0.877444,-0.8445577

def show_grayscale(output_raw,width,height,max_iterations):
    """ tabdile list be array va namayesh tasvir """
    max_iterations = float(max(output_raw))
    scale_factor = float(max_iterations)
    scaled = [int(o / scale_factor * 255) for o in output_raw]
    output = array.array("B",scaled)
    im = Image.new("L",(width,width))
    im.frombytes(output.tobytes(),"raw","L",0,-1)
    im.show()



## sathe mokhtalef morede barresi




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
        output[i] = n 
    return output

def calc_pure_python(draw_output,desired_width,max_iterations):
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
    width = len(x)
    height = len(y)    

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

    if draw_output:
    
        show_grayscale(output,width,height,max_iterations)

if __name__ == "__main__":

    calc_pure_python(draw_output=True,desired_width=1000,max_iterations=300)

           

