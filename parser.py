from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

def parse_file(fname, points, transform, screen, color ):
    script  = open(fname,"r")
    lines=script.read().split('\n')
    lim=len(lines)
    count=0
    while count<lim:
        i=lines[count]
        if i=="line":
            x=lines[count+1].split(" ")
            add_edge(points, int(x[0]), int(x[1]), int(x[2]), int(x[3]), int(x[4]), int(x[5]))
            count+=1
        if i=="ident":
            ident(transform)
        if i=="scale":
            x=lines[count+1].split(" ")
            m=make_scale(int(x[0]),int(x[1]),int(x[2]))
            matrix_mult(m,transform)
            count+=1
        if i=="move" or i=="translate":
            x=lines[count+1].split(" ")
            m=make_transform(int(x[0]),int(x[1]),int(x[2]))
            matrix_mult(m,transform)
            count+=1
        if i=="rotate":
            x=lines[count+1].split(" ")
            if x[0]=="x":
                m=make_rotX(int(x[1]))
            elif x[0]=="y":
                m=make_rotY(int(x[1]))
            elif x[0]=="z":
                m=make_rotZ(int(x[1]))
            matrix_mult(m,transform)
            count+=1
        if i=="apply":
            matrix_mult(transform,points)
        if i=="display":
            clear_screen(screen)
            draw_lines(points,screen,color)
            display(screen)
        if i=="save":
            clear_screen(screen)
            draw_lines(points,screen,color)
            save_extension(screen,lines[count+1])
            count+=1
        if i=="quit":
            script.close()
        count+=1
    #return           
    #pass

#parse_file("script")
parse_file( 'script', edges, transform, screen, color )
