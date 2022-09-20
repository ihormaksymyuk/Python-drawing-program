

from email.mime import image
from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd
from tkinter.colorchooser import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk, ImageOps, ImageFilter, EpsImagePlugin, ImageGrab
import io
from tkinter.filedialog import askdirectory, asksaveasfilename
from random import *






color_w="white"

window = tk.Tk()
window.title("Простий графічний редактор")
window.iconbitmap(r'palitra.ico')
#window.geometry("750x250")
frame1 = tk.Frame(master=window, height=50, bg="light gray")
frame1.pack(fill=tk.X)
frame2 = tk.Frame(master=window, height=200, bg="gray")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
c = Canvas(master=frame2, width=1200, height=850, bg=color_w)

c1 = Canvas(master=c, width=1, height=1, bg=color_w,highlightbackground=color_w)
c1.place(x=1,y=1,anchor=CENTER)
frame3 = tk.Frame(master=frame2,width=100, bg="light gray", relief=tk.RIDGE)
frame3.pack(fill=tk.Y, side=tk.LEFT)
c.pack( side=tk.LEFT,  padx=15, pady=10)
#img= ImageTk.PhotoImage(Image.open("QIP Shot - Screen 013.png"))
#c.create_image(10,10,anchor=NW,image=img)

#global photo


            


def open_new_images():
    
    global photo
    image_path = fd.askopenfilename()
    
    photo = ImageTk.PhotoImage(Image.open(image_path))
    
    photo1 = Image.open(image_path)
    c1.create_image(0, 0, image=photo, anchor=NW)
    c1.image = photo
    photo_size=photo1.size
    c1.configure(width=photo_size[0], height=photo_size[1])
    print(photo_size)
def drag_image(e):
    e.widget.place(x=e.x,y=e.y,anchor=CENTER)
    
    #c.image = photo
c1.bind("<B1-Motion>",drag_image)  

def change_color_b():
    global color_w
    colors = askcolor(title="Tkinter Color Chooser")
    window.configure(bg=colors[1])
    color_w = colors[1]
    c.configure(bg=color_w)
    c1.configure(bg=color_w,highlightbackground=color_w)
    return color_w

def set_bg():
   
    image_path = fd.askopenfilename()
    bg = ImageTk.PhotoImage(Image.open(image_path))
    bg1 = Image.open(image_path)
    bg_size=bg1.size
    c.configure(width=bg_size[0], height=bg_size[1])
    c.create_image(0,0, image = bg, anchor=NW)
    c.image = bg
   


def crop():
    global photo
    c1.configure(photo.filter(ImageFilter.EMBOSS))



def save_as_eps():
    filepath = asksaveasfilename(
            defaultextension="eps",
           filetypes=[("Зображення", "*.eps"), ("Всі файли", "*.*")],)
    if not filepath:
        return
    
    with open(filepath, "w"):
        c.postscript(file = filepath)
    window.title(f"Простий графічний редактор - {filepath}")
    
  
    
    #img.show()
    #img1 = img.convert("RGB")
    #img.save("my_image.bmp")
    #ps = c.postscript(colormode='color')
    #img = img.EpsImagePlugin()
    #img.save('my_image.jpg')

    #defaultextension=["jpg", "png", "bmp"],


def save_as_jpg():
        print(c.winfo_rootx(), c.winfo_x())
        filepath = asksaveasfilename(
            defaultextension="jpg",
            filetypes=[("Формат JPG", "*.jpg"),])
        if not filepath:
            return
        
        with open(filepath, "w") as output_file:
            box = (c.winfo_rootx(),c.winfo_rooty(),c.winfo_rootx()+c.winfo_width(),c.winfo_rooty() + c.winfo_height())
            grab = ImageGrab.grab(bbox = box)
            grab.save(output_file)
            #x=c.winfo_rootx()-c.winfo_x()
            #x=c.winfo_x()
            #y=c.winfo_rooty()-c.winfo_y()
            #y=c.winfo_y()
            #x1=x+c.winfo_width()
            #y1=y+c.winfo_height()
            #ImageGrab.grab(include_layered_windows=True).crop((x,y,x1,y1)).save(output_file)
        window.title(f"Простий графічний редактор - {filepath}")
        print(c.winfo_rootx(), c.winfo_x())
    

menubar = Menu(window)
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Відкрити зображення", command= open_new_images)
file_menu.add_command(label="Експорт .eps", command= save_as_eps)
file_menu.add_command(label="Експорт .jpg", command= save_as_jpg)
file_menu.add_separator()
file_menu.add_command(label="Вийти",command=lambda: c.delete("all"))
menubar.add_cascade(label="Файл", menu=file_menu)

edit_menu = Menu(menubar, tearoff=0)
edit_menu.add_command(label="Змінити колір фону", command= change_color_b)
edit_menu.add_command(label="Змінити зображення фону", command= set_bg)
menubar.add_cascade(label="Редагувати", menu=edit_menu)
window.configure(menu=menubar)


color_lab = tk.Label(master=frame1, text="Товщина лінії: ", bg="light gray")  # створюєм назву повзунка для товщини лінії
color_lab.pack (side='left')
brush_size = 1
color = "black"

def changeW(e):
     #change Width of pen through slider
    brush_size = e

def set_brush_size(value):
    global brush_size
    brush_size = int(value)
    return brush_size
    #print(brush_size)

scale1 = Scale(master=frame1,orient=HORIZONTAL,length=300,from_=1,to=100,tickinterval=10,resolution=1, command=set_brush_size) # створюєм повзунок для товщини лінії
scale1.pack(side='left')


# функція зміни кольору фону
def change_color():
    global color
    colors = askcolor(title="Tkinter Color Chooser")
    window.configure(bg=colors[1])
    color = colors[1]
    return color

def del_all():
    c.delete("all")
    c1.delete("all")
    c1.configure(width=0, height=0)

# функція малювання ліні
def line():
    global n
    n=0
    global x
    x=[]
    global line2
    line2=[]
    line1 = None
    global spline
    spline = False
    global line
    line = True
    global flower
    flower = False
    global polygon
    polygon = False
    global polygon_fill
    polygon_fill = False
    global oval
    oval = False
    global oval_fill
    oval_fill = False
    class Point:
        def xy1(self,e):
            self.x1 = e.x
            self.y1 = e.y

        def poly3(self,e):
            self.x1 = e.x
            self.y1 = e.y
            self.x0 = self.x1
            self.y0 = self.y1
            if line:
                c.create_line(self.x1,self.y1,self.x1,self.y1,width=brush_size,fill=color,capstyle=ROUND)
                #print('line is...')

        def xy2(self,e):
            self.x2 = e.x
            self.y2 = e.y
            if line:
                c.create_line(self.x0,self.y0,self.x2,self.y2,width=brush_size,fill=color,capstyle=ROUND)

        def xy3(self,e):
            global line2
            global x
            global n
          
            self.x2 = e.x
            self.y2 = e.y
            if line:
                line1 = c.create_line(self.x0,self.y0,self.x2,self.y2,width=brush_size,fill=color,capstyle=ROUND)
            x.append(self.x2)
            line2.append(line1)
            n=n+1
            #print(n)
            #print(line2)

                
            if n > 1:
                c.delete(line2[n-2])
               
    p = Point()
    c.bind("<B1-Motion>", p.xy3)
    c.bind("<Button-1>",p.poly3)
    c.bind("<ButtonRelease-1>", p.xy2)


# функція малювання квітки
def flower():
    global flower
    flower = True
    colors=['deep sky blue', 'gold', 'deep pink', 'orange red', 'firebrick1', 'magenta2', 'red2', 'orchid1']
    leef1=[60,70,80,90,100]
    petal1 = [60, 50, 40]
    class Point1:
        def xy1(self,e):
            if flower:
                c.create_line(self.x1,self.y1,e.x,e.y,width=4,fill="green",capstyle=ROUND)
            self.x1 = e.x
            self.y1 = e.y
            print('flower:',flower)

        def poly1(self,e):
            leef=choice(leef1)
            self.x1 = e.x
            self.y1 = e.y
            self.x0 = self.x1
            self.y0 = self.y1
            if flower:
                c.create_polygon(self.x1,self.y1,self.x1+20,self.y1-(leef),self.x1+70,self.y1-(leef),self.x1+30,self.y1-40,fill="green",outline="black",smooth=1)
                c.create_polygon(self.x1,self.y1,self.x1-20,self.y1-(leef),self.x1-70,self.y1-(leef),self.x1-30,self.y1-50,fill="green",outline="black",smooth=1)
            

        def xy2(self,e):
            color=choice(colors)
            petal=choice(petal1)
            self.x2 = e.x
            self.y2 = e.y
            if flower:
                c.create_line(self.x1,self.y1,self.x2,self.y2,width=20,fill="yellow",capstyle=ROUND)
                c.create_oval(self.x2+10,self.y2-10,self.x2+petal,self.y2+10,fill=color,outline=color)
                c.create_oval(self.x2-10,self.y2+10,self.x2+10,self.y2+petal,fill=color,outline=color)
                c.create_oval(self.x2-petal,self.y2-10,self.x2-10,self.y2+10,fill=color,outline=color)
                c.create_oval(self.x2-10,self.y2-petal,self.x2+10,self.y2-10,fill=color,outline=color)
            

    p = Point1()
    c.bind("<B1-Motion>", p.xy1)
    c.bind("<Button-1>",p.poly1) 
    c.bind("<ButtonRelease-1>", p.xy2) 
    

def spline():
    global spline
    spline = True
    global line
    line = False
    global flower
    flower = False
    global oval
    oval = False
    global oval_fill
    oval_fill = False
    class Point2:
        def xy1(self,e):
            if spline:
                c.create_line(self.x1,self.y1,e.x,e.y,width=brush_size,fill=color,capstyle=ROUND)
            self.x1 = e.x
            self.y1 = e.y

        def poly2(self,e):
            self.x1 = e.x
            self.y1 = e.y
            self.x0 = self.x1
            self.y0 = self.y1
            
        def xy2(self,e):
            self.x2 = e.x
            self.y2 = e.y
        
    p = Point2()
    c.bind("<B1-Motion>", p.xy1)
    c.bind("<Button-1>",p.poly2) 
    c.bind("<ButtonRelease-1>", p.xy2)

def oval():
    global oval
    oval = True
    global n1
    n1=0
    global oval2
    oval2=[]
    global spline
    spline = False
    global line
    line = False
    global flower
    flower = False
    global rect_fill
    rect_fill = False
    global oval_fill
    oval_fill = False
    class Oval:
        def poly(self, e):
            self.x1 = e.x
            self.y1 = e.y

        def poly2(self, e):
            self.x2 = e.x
            self.y2 = e.y
            if oval:
                c.create_oval(self.x1, self.y1, self.x2, self.y2,
                              fill='',  outline=color,width = brush_size)

        def poly3(self, e):
            global n1
            self.x2 = e.x
            self.y2 = e.y
            if oval:
                oval1 = c.create_oval(self.x1, self.y1, self.x2, self.y2,
                              fill='',  outline=color,width = brush_size)
                oval2.append(oval1)
                n1 = n1+1
                if n1 > 1:
                    c.delete(oval2[n1-2])
    p1 = Oval()
    c.bind("<B1-Motion>", p1.poly3)
    c.bind("<Button-1>", p1.poly)
    c.bind("<ButtonRelease-1>", p1.poly2)

def oval_fill():
    global oval_fill
    oval_fill = True
    global oval
    oval = False
    global n1
    n1=0
    global oval2
    oval2=[]
    global spline
    spline = False
    global line
    line = False
    global flower
    flower = False
    global rect_fill
    rect_fill = False
    class Oval_fill:
        def poly(self, e):
            self.x1 = e.x
            self.y1 = e.y

        def poly2(self, e):
            self.x2 = e.x
            self.y2 = e.y
            if oval_fill:
                c.create_oval(self.x1, self.y1, self.x2, self.y2,
                              fill=color,  outline=color,width = brush_size)

        def poly3(self, e):
            global n1
            self.x2 = e.x
            self.y2 = e.y
            if oval_fill:
                oval1 = c.create_oval(self.x1, self.y1, self.x2, self.y2,
                              fill=color,  outline=color,width = brush_size)
                oval2.append(oval1)
                n1 = n1+1
                if n1 > 1:
                    c.delete(oval2[n1-2])
    p1 = Oval_fill()
    c.bind("<B1-Motion>", p1.poly3)
    c.bind("<Button-1>", p1.poly)
    c.bind("<ButtonRelease-1>", p1.poly2)

def rect():
    global n1
    n1=0
    global rect2
    rect2=[]
    global spline
    spline = False
    global line
    line = False
    global flower
    flower = False
    global rect
    rect = True
    global rect_fill
    rect_fill = False
    global oval
    oval = False
    global oval_fill
    oval_fill = False
    class Rectangle:
        def poly(self, e):
            self.x1 = e.x
            self.y1 = e.y

        def poly2(self, e):
            self.x2 = e.x
            self.y2 = e.y
            if rect:
                c.create_polygon(self.x1, self.y1,self.x1 + (self.x2 - self.x1), self.y1, self.x2, self.y2,
                             self.x1 , self.y1 + (self.y2-self.y1), fill='',  outline=color,width = brush_size,joinstyle = MITER, smooth=0)

        def poly3(self, e):
            global n1
            self.x2 = e.x
            self.y2 = e.y
            if rect:
                rect1 = c.create_polygon(self.x1, self.y1,self.x1 + (self.x2 - self.x1), self.y1, self.x2, self.y2,
                                self.x1 , self.y1 + (self.y2-self.y1), fill='', outline=color, width = brush_size,joinstyle = MITER, smooth=0)
                rect2.append(rect1)
                n1 = n1+1
                if n1 > 1:
                    c.delete(rect2[n1-2])
    p1 = Rectangle()
    c.bind("<B1-Motion>", p1.poly3)
    c.bind("<Button-1>", p1.poly)
    c.bind("<ButtonRelease-1>", p1.poly2)


def rect1():
    global n1
    n1=0
    global rect2
    rect2=[]
    global spline
    spline = False
    global line
    line = False
    global flower
    flower = False
    global rect_fill
    rect_fill = True
    global rect
    rect = False
    global oval
    oval = False
    global oval_fill
    oval_fill = False
    class Rectangle1:
        def poly(self, e):
            self.x1 = e.x
            self.y1 = e.y

        def poly2(self, e):
            self.x2 = e.x
            self.y2 = e.y
            if rect_fill:
                c.create_polygon(self.x1, self.y1,self.x1 + (self.x2 - self.x1), self.y1, self.x2, self.y2,
                             self.x1 , self.y1 + (self.y2-self.y1), fill=color, outline="black",width = brush_size,joinstyle = MITER, smooth=0)


        def poly3(self, e):
            global n1
            self.x2 = e.x
            self.y2 = e.y
            if rect_fill:
                rect1 = c.create_polygon(self.x1, self.y1,self.x1 + (self.x2 - self.x1), self.y1, self.x2, self.y2,
                                self.x1 , self.y1 + (self.y2-self.y1), fill=color, outline="black",width = brush_size,joinstyle = MITER, smooth=0)
                rect2.append(rect1)
                n1 = n1+1
                if n1 > 1:
                    c.delete(rect2[n1-2])
    p1 = Rectangle1()
    c.bind("<B1-Motion>", p1.poly3)
    c.bind("<Button-1>", p1.poly)
    c.bind("<ButtonRelease-1>", p1.poly2)

def grass():
    global rect_fill
    rect_fill = False
    global line
    line = False
    global tree
    tree = False
    global flower
    flower = False
    global grass
    grass = True
    global rect
    rect = False
    global polygon
    polygon = False
    global polygon_fill
    polygon_fill = False
    global oval
    oval = False
    global oval_fill
    oval_fill = False
    height = [30,40,50,60]
    wind = [0, 5, -5]
    colors=['yellow green', 'green yellow', 'forest green']
    class Grass:
        def poly(self, e):
            h=choice(height)
            w = choice(wind)
            color=choice(colors)
            if grass:
                c.create_polygon(e.x, e.y, e.x+5, e.y-20, e.x+w, e.y-h, e.x+2, e.y-20, e.x-2, e.y, fill=color, outline="dark green", smooth=0)
    p1 = Grass()
    c.bind("<B1-Motion>", p1.poly)


def tree():
    global line
    line = False
    global tree
    tree = True
    global flower
    flower = False
    global grass
    grass = False
    global rect
    rect = False
    global polygon
    polygon = False
    global polygon_fill
    polygon_fill = False
    global oval_fill
    oval_fill = False
    height = [50,70,90,100]
    wind = [0, 5, -5]
    colors=['dark green', 'forest green']
    class Tree:
        def poly(self, e):
            h=choice(height)
            w = choice(wind)
            color=choice(colors)
            if tree:
                c.create_polygon(e.x-10, e.y, e.x-5, e.y-h, e.x+5, e.y-h, e.x+10, e.y, fill='saddle brown', outline='saddle brown', smooth=0)
                c.create_polygon(e.x-100, e.y-h, e.x-50, e.y-(h+50), e.x+50, e.y-(h+50), e.x+100, e.y-h, fill=color, outline=color, smooth=0)
                c.create_polygon(e.x-80, e.y-(h+50), e.x-30, e.y-(h+100), e.x+30, e.y-(h+100), e.x+80, e.y-(h+50), fill=color, outline=color, smooth=0)
                c.create_polygon(e.x-50, e.y-(h+100), e.x-20, e.y-(h+150), e.x+20, e.y-(h+150), e.x+50, e.y-(h+100), fill=color, outline=color, smooth=0)
                c.create_polygon(e.x-30, e.y-(h+150), e.x, e.y-(h+220), e.x+30, e.y-(h+150), fill=color, outline=color, smooth=0)

    p1 = Tree()
    c.bind("<Button-1>", p1.poly)


def polygon():
    global polygon
    polygon = True
    global polygon_fill
    polygon_fill = False
    global flower
    flower = False
    global rect_fill
    rect_fill = False
    global rect
    rect = False
    global line
    global grass
    grass = False
    line = False
    global oval
    oval = False
    global oval_fill
    oval_fill = False

    class Poly:
        def __init__(self):
            self.coord=[]
            self.line2 = []
            self.line1 = True
            self.n = 0
            self.n1 = 0

        def points(self, e):
            self.coord.append(e.x)
            self.coord.append(e.y)
            
            if self.n >= 2 :
                if polygon:
                    c.create_line(self.coord[self.n-2],self.coord[self.n-1],self.coord[self.n],self.coord[self.n+1],fill=color,width=brush_size,capstyle=ROUND)
            self.n += 2

        def poly(self, coord):
            if polygon:
                c.create_polygon(self.coord, fill='',  outline=color,width = brush_size,joinstyle = MITER, smooth=0)
            self.coord.clear()
            self.n = 0

        def line(self,e):
                self.x2 = e.x
                self.y2 = e.y
                if polygon:
                    line1 = c.create_line(self.coord[self.n-2],self.coord[self.n-1],self.x2,self.y2,fill=color, dash=(3,5),capstyle=ROUND)
                #print(self.coord, self.n)
                #x.append(self.x2)
                self.line2.append(line1)
                self.n1=self.n1+1
                if self.n > 1:
                    c.delete(self.line2[self.n1-2])
                
    p1 = Poly()
    c.bind("<Button-1>", p1.points)
    c.bind("<Double-Button-1>", p1.poly)
    c.bind("<Motion>", p1.line)

def polygon_fill():
    global polygon_fill
    polygon_fill = True
    global polygon
    polygon = False
    global flower
    flower = False
    global rect_fill
    rect_fill = False
    global rect
    rect = False
    global line
    line = False
    global grass
    grass = False
    global oval
    oval = False
    global oval_fill
    oval_fill = False

    class Poly_fill:
        def __init__(self):
            self.coord=[]
            self.line2 = []
            self.line1 = True
            self.n = 0
            self.n1 = 0

        def points(self, e):
            self.coord.append(e.x)
            self.coord.append(e.y)
            
            if self.n >= 2 :
                if polygon_fill:
                    c.create_line(self.coord[self.n-2],self.coord[self.n-1],self.coord[self.n],self.coord[self.n+1],fill=color,width=brush_size,capstyle=ROUND)
            self.n += 2

        def poly(self, coord):
            if polygon_fill:
                c.create_polygon(self.coord,  outline=color,width = brush_size,fill=color,joinstyle = MITER, smooth=0)
            self.coord.clear()
            self.n = 0

        def line(self,e):
                self.x2 = e.x
                self.y2 = e.y
                if polygon_fill:
                    line1 = c.create_line(self.coord[self.n-2],self.coord[self.n-1],self.x2,self.y2,fill=color, dash=(3,5),capstyle=ROUND)
                #print(self.coord, self.n)
                #x.append(self.x2)
                self.line2.append(line1)
                self.n1=self.n1+1
                if self.n > 1:
                    c.delete(self.line2[self.n1-2])
                
    p1 = Poly_fill()
    c.bind("<Button-1>", p1.points)
    c.bind("<Double-Button-1>", p1.poly)
    c.bind("<Motion>", p1.line)

but_line = PhotoImage(file="line.png")
but_line = but_line.subsample(4,4)
but_spline = PhotoImage(file="spline.png")
but_spline = but_spline.subsample(4,4)
but_oval = PhotoImage(file="oval.png")
but_oval = but_oval.subsample(4,4)
but_oval_fill = PhotoImage(file="oval_fill.png")
but_oval_fill = but_oval_fill.subsample(4,4)
but_rect = PhotoImage(file="rectangle.png")
but_rect = but_rect.subsample(4,4)
but_rect_fill = PhotoImage(file="rectangle_fill.png")
but_rect_fill = but_rect_fill.subsample(4,4)
but_polygon = PhotoImage(file="polygon.png")
but_polygon = but_polygon.subsample(4,4)
but_polygon_fill = PhotoImage(file="polygon_fill.png")
but_polygon_fill = but_polygon_fill.subsample(4,4)
but_grass = PhotoImage(file="grass.png")
but_grass = but_grass.subsample(4,4)
but_tree = PhotoImage(file="tree.png")
but_tree = but_tree.subsample(4,4)
but_flower = PhotoImage(file="flower.png")
but_flower = but_flower.subsample(4,4)
but_colors = PhotoImage(file="colors.png")
but_colors = but_colors.subsample(3,3)


#sel_color = Button(master=frame1, text="Вибрати колір", width=15,height=4,  command=change_color) # створюєм кнопку для вибору кльору
sel_color = Button(master=frame1, image = but_colors,  command=change_color) # створюєм кнопку для вибору кльору
sel_color.pack (side='left')
draw_line = Button(master=frame3,image = but_line,  command=line) # створюєм кнопку для ліній
#draw_line = Button(master=frame3, text="Лінія", width=10,height=4,  command=line) # створюєм кнопку для ліній
draw_line.pack (side='top')
#draw_spline = Button(master=frame3, text="Сплайн", width=10,height=4,  command=spline) # створюєм кнопку для сплайнів
draw_spline = Button(master=frame3, image = but_spline,  command=spline) # створюєм кнопку для сплайнів
draw_spline.pack (side='top')
draw_oval = Button(master=frame3, image = but_oval,  command=oval) # створюєм кнопку для овалу
draw_oval.pack (side='top')
draw_oval_fill = Button(master=frame3, image = but_oval_fill,  command=oval_fill) # створюєм кнопку для овалу залитого
draw_oval_fill.pack (side='top')
#draw_rectangle = Button(master=frame3, text="Прямокутник", width=10,height=4,  command=rect) # створюєм кнопку для прямокутника
draw_rectangle = Button(master=frame3, image = but_rect,  command=rect) # створюєм кнопку для прямокутника прозорого
draw_rectangle.pack (side='top')
draw_rectangle1 = Button(master=frame3, image = but_rect_fill,  command=rect1) # створюєм кнопку для прямокутника залитого
draw_rectangle1.pack (side='top')
draw_polygon = Button(master=frame3, image = but_polygon,  command=polygon) # створюєм кнопку для багатокутника
draw_polygon.pack (side='top')
draw_polygon_fill = Button(master=frame3, image = but_polygon_fill,  command=polygon_fill) # створюєм кнопку для багатокутника залитого
draw_polygon_fill.pack (side='top')
#draw_flower = Button(master=frame3, text="Квітка", width=10,height=4,  command=flower) # створюєм кнопку для квітки
draw_flower = Button(master=frame3, image = but_flower,  command=flower) # створюєм кнопку для квітки
draw_flower.pack (side='top')
#draw_tree = Button(master=frame3, text="Дерево", width=10,height=4,  command=tree) # створюєм кнопку для дерева
draw_tree = Button(master=frame3, image = but_tree,  command=tree) # створюєм кнопку для дерева
draw_tree.pack (side='top')
#draw_grass = Button(master=frame3, text="Трава", width=10,height=4,  command=grass) # створюєм кнопку для трави
draw_grass = Button(master=frame3, image = but_grass,  command=grass) # створюєм кнопку для трави
draw_grass.pack (side='top')
clear_btn = Button(master=frame1, text="Стерти все", width=15,height=4 , command=del_all)
clear_btn.pack (side='left')


                         
''' 
def paint(e):
    global old_x
    global old_y
    
    if old_x and old_y:
        c.create_line(old_x,old_y,e.x,e.y,width=brush_size,fill=color,capstyle=ROUND,smooth=True)

    old_x = e.x
    old_y = e.y

def reset(e): 
    global old_x
    global old_y      
    old_x = None
    old_y = None  

c.bind("<B1-Motion>", paint)

c.bind("<ButtonRelease-1>", reset)

'''


def main():
    
    window.mainloop()

if __name__ == "__main__":
    main()