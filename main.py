from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

matrix_mult([[1,2,3,4],[2,3,4,5],[1,2,3,4],[2,3,4,5]],[[1,2,3,4]])
parse_file('script')
#parse_file( 'script', edges, transform, screen, color )
