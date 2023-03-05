#
# class point:
#     def __init__(self,x1,x2):
#         self.x1 =x1
#         self.x2 =x2
#     x = 10
#     y = 20
#     def average(self,other):
#         if(other):
#             return ((other.x1+other.x2)/2)
#         else:
#             return ((self.x1+self.x2)/2)
#
#
#     def setval(self,mx,my):
#         self.x1 = mx
#         self.x2 = my
#     def getval(self):
#         print(self.x,self.y)
#
#
#
#
# p = point(10,20)
# p2 = point(20,30)
# print(p.x1,p.x2)
# p.setval(100,200)
# res = p2.average(p)
# print(res)
# print(p.x1,p.x2)
#
#
# import math
#
#
# class point:
#     '''
#     hello guys this is  a long comment
#     '''
#     def __init__(self):
#         self.x = 0
#         self.y = 0
#     def read_point(self,x,y):
#         self.x = x
#         self.y = y
#     def distance(self,point1,point2):
#         dist = math.sqrt((point1.x-point2.x)**2+(point1.y-point2.y)**2)
#         return dist
#     def print_point(self):
#         print(self.x,self.y)
#
#
# p1 = point()
# p2 = point()
# p1.read_point(10,12)
# p2.read_point(11,12)
# print(p1.distance(p1,p2))
# p1.print_point()
# p2.print_point()



# class rectangle

# class point:
#     def __init__(self):
#         print("point class")
#         self.x = 0
#         self.y = 0
#     def setPoints(self,x,y):
#         self.x = x
#         self.y = y
#     def getpoints(self):
#         print(0,0)
#         print(self.x,self.y)
#         print(self.y,self.x)
#         print(self.y,self.y)
#
# class rectangle:
#
#     p = point()
#     def __init__(self,height,width):
#         self.height = height
#         self.width = width
#
#
#     def find_center(self,rect):
#         self.p.setPoints(rect.width/2,rect.height/2)
#         print(f"The center of the rectangle is :{self.p.y},{self.p.y}")
#
#     def print_corners(self):
#         self.p.getpoints()
#
#     def resize(self,new_height,new_width):
#         self.height = new_height
#         self.width = new_width
#
#
# r1 = rectangle(100,200)
# r1.find_center(r1)
# r1.print_corners()


str = "pavan studies at sahyadri"
list = []
sentance = str.split()
max = 0
for words in sentance:
    if(len(words)>max):
        max = len(words)
        modifiedstr = words
print(max,modifiedstr)

# 9/5+celcius+32 convert celcius to farenhite