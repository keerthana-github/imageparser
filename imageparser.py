import urllib.request
import turtle

#draw black and white pixel
def pixel(size, color):
    #black and white means same value across the board
    turtle.fillcolor(color, color, color)
    turtle.color(color,color,color)
    #begin fill 
    turtle.begin_fill()
    turtle.pendown()
    #make a square the size of pixel
    for i in range(0, 4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(size)

#draw color pixel
def pixel_rgb(size,red,green,blue):
    #given rgb values, input to change color
    turtle.fillcolor(red,green,blue)
    turtle.color(red,green,blue)
    turtle.begin_fill()
    turtle.pendown()
    #make a square the pixel size inputted
    for i in range(0, 4):
        turtle.forward(size)
        turtle.right(90)
    #end fill
    turtle.end_fill()
    turtle.penup()
    turtle.forward(size)
    

#ask for file to open
filename=input("Which file do you want to work with? ")
#add .txt to the end
filename_txt=filename + ".txt"

#try except block to prevent error messages
try:
    # open up the file
    file_pointer=open(filename_txt,"r")
except:
    print("File didn't open correctly!")

else:
    # define a location for our file
    url = "https://cs.nyu.edu/~kapp/python/"+filename_txt
# open a connection to the URL
    response = urllib.request.urlopen(url)
    b_found=False
    colors=False
    
    # read data from URL as a string
    data = response.read().decode('utf-8');
    # grab the data
    # close the file
    #for every character in data
    for i in data:
        #if there is a line break deal with that
        if i == "b":
            b_found=True
        #if there is colors deal with that
        if i =="t":
            colors=True
    #if there are colors
    if colors==True:
        #and if there are multiple lines of code
        if b_found==True:
            #split the lines by b
            lines=data.split("b")
            #create a global list of each list (as a line)
            lines_global=[]
            #for every string in the lines 
            for i in lines:
                #split by ,
                i_split=i.split(",")
                #create a new list to store value of lines
                line=[]
                #for every value in the split list
                for x in i_split:
                    #make sure it's not empty or alpha and add to new list line
                    if x!="" and x!="\n" and x!=" " and not x.isalpha():
                        line+=[x]
                #if it's the first index in all of the lines
                if lines.index(i)==0:
                    #extract thefollowing data
                    for i in range(0,4):
                        if i == 0:
                            #width
                            width=float(line[i])
                        if i == 1:
                            #height
                            height=float(line[i])
                        if i == 2:
                            #bg color
                            bg=float(line[i])
                            
                        if i == 3:
                            #pixel size
                            pixel_size=float(line[i])
                    #delete all 4 values in the list after that to return only colors
                    del line[0]
                    del line[0]
                    del line[0]
                    del line[0]
                #add the new list to global lines
                lines_global+=[line]

            #create lists for each rgb value
            red=[]
            green=[]
            blue=[]
            
            #for every line, extract the rgb value and store in list
            for line in lines_global:
                red+=[line[0::3]]
                green+=[line[1::3]]
                blue+=[line[2::3]]
            

            #setup
            turtle.setup(width,height)
            turtle.tracer(0)
            #turtle.speed(10)
            turtle.penup()
            #draw background
            turtle.goto(-width/2, -height/2)
            turtle.fillcolor(bg, bg, bg)
            turtle.begin_fill()
            turtle.pendown()
            for i in range(0, 4):
                turtle.forward(10000)
                turtle.left(90)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-width/2,height/2)
            #for every line in global
            for line in lines_global:
                #extract index
                index=lines_global.index(line)
                #find the list
                r_list=red[index]
                g_list=green[index]
                b_list=blue[index]
                num_pixels=len(line)//3
                for i in range(0,num_pixels):
                    #for every value in the index
                    r=float(r_list[i])
                    g=float(g_list[i])
                    b=float(b_list[i])
                    #draw the characters
                    pixel_rgb(pixel_size, r,g,b)
                turtle.penup()
                #go to the next line
                turtle.goto(-width/2,(height/2)-(pixel_size*(lines_global.index(line)+1)))
            turtle.update
        else:
            #if the data is a single list of colors
            lines=data.split(",")
            for i in range(0,len(lines)):
                if i == 0:
                    width=float(lines[0])
                if i == 1:
                    height=float(lines[1])
                if i == 2:
                    bg=float(lines[2])
                if i == 3:
                    pixel_size=float(lines[3])
            red=[]
            green=[]
            blue=[]
            for line in lines:
                red+=line[4::3]
                green+=line[5::3]
                blue+=line[6::3]


            #setup
            turtle.setup(width,height)
            turtle.tracer(0)
            turtle.penup()
            #draw background
            turtle.goto(-width/2, -height/2)
            turtle.fillcolor(bg, bg, bg)
            turtle.begin_fill()
            turtle.pendown()
            for i in range(0, 2):
                turtle.forward(width)
                turtle.left(90)
                turtle.forward(height)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-width/2,height/2)
            turtle.right(180)
            for i in lines[4:]:
                location=lines.index(i)
                r=float(red[location])
                g=float(green[location])
                b=float(blue[location])
                pixel_rgb(pixel_size, r,g,b)
            turtle.update

    #IF COLORS NOT FOUND            
    else:
        if b_found==True:
            lines=data.split("b")
            lines_global=[]
            for i in lines:
                i_split=i.split(",")
                line=[]
                
                for x in i_split:
                    if x!="" and x!="\n" and x!=" ":
                        line+=[x]

                if lines.index(i)==0:
                    for i in range(0,4):
                        if i == 0:
                            width=float(line[i])
                        if i == 1:
                            height=float(line[i])
                        if i == 2:
                            bg=float(line[i])
                        if i == 3:
                            pixel_size=float(line[i])
                    del line[0]
                    del line[0]
                    del line[0]
                    del line[0]
                lines_global+=[line]

            #setup
            turtle.setup(width,height)
            turtle.tracer(0)
            turtle.penup()
            #draw background
            turtle.goto(-width/2, -height/2)
            turtle.fillcolor(bg, bg, bg)
            turtle.begin_fill()
            turtle.pendown()
            for i in range(0, 4):
                turtle.forward(10000)
                turtle.left(90)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-width/2,height/2)
            for i in lines_global:
                for c in i:
                    
                    color=float(c)
                    pixel(pixel_size, color)
                turtle.penup()
                turtle.goto(-width/2,(height/2)-(pixel_size*lines_global.index(i)))
            turtle.update
        else:
            lines=data.split(",")
            for i in range(0,len(lines)):
                if i == 0:
                    width=float(lines[0])
                if i == 1:
                    height=float(lines[1])
                if i == 2:
                    bg=float(lines[2])
                if i == 3:
                    pixel_size=float(lines[3])

            #setup
            turtle.setup(width,height)
            turtle.tracer(0)
            turtle.penup()
            #draw background
            turtle.goto(-width/2, -height/2)
            turtle.fillcolor(bg, bg, bg)
            turtle.begin_fill()
            turtle.pendown()
            for i in range(0, 2):
                turtle.forward(width)
                turtle.left(90)
                turtle.forward(height)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-width/2,height/2)
            turtle.right(180)
            for i in lines[4:]:
                color=float(i)
                pixel(pixel_size, color)
            turtle.update
