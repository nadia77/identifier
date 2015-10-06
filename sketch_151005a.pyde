from random import randrange as r
# Setup size of the drawing table 
side_a = int(64)
side_b = int(64)
draw_count = 0

n = 7
masterlist = []
for l in range(1,16):
    masterlist.append(0)

def setup():
    size(30*side_a, 16*side_b)
  
      
def draw_square(x,y,is_colored, density):
    d_a = side_a / (n + 1) 
    d_b = side_b / (n + 1)
    offset_x = masterlist[density] * side_a
    offset_y = density * side_b
    if is_colored:
        rect( offset_x + (x * d_a), offset_y + (y * d_b), d_a + 1, d_b + 1)
                

def draw_sim_square(x,y,is_colored, density):
    draw_square(x , y, is_colored, density)
    draw_square(n - x, y, is_colored, density)
    draw_square(x, n - y, is_colored, density)
    draw_square(n - x, n - y, is_colored, density)


def draw():
    #save("pics/pic" + str(r(1000)) + ".jpeg")
    #background(235)
    global draw_count
    if draw_count == 500:
        save("final" + str(r(10000)) + ".png")
    
    noStroke()
    fill(r(255), r(255), r(255))
    ##[draw_square(i,j,r(2)) for i in range(n + 1) for j in range(n + 1)]
   
    density = 0
    size = (n + 1)/2
    description = []
    for i in range(size):
        description.append([])
    
    for i in range(size):
        for j in range(size):
            is_colored = r(2)
            density += is_colored
            description[i].append(is_colored)
    
    masterlist[density] += 1
    delay(1000)
    
    for i in range(size):
        for j in range(size):
            draw_sim_square(i, j, description[i][j], density)
            ##print description
    draw_count += 1
    print draw_count
