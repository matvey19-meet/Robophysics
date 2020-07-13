import cv2
import xlsxwriter
from a_star_custom import check
from model_predictive_speed_and_steer_control import main as model_main
from a_star_custom import main
from rrt_star_custom import main2
from matplotlib import pyplot as plt
from lqr_speed_steer_control import main as mainLqr
from informed_rrt_star import informed_main
import multiprocessing

##paramaters
car_width=0.2 #(m)
track_width=0.6 #(m)


def init(path):

    img=cv2.imread(path,2)
    
    scale_percent=10
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim=(width,height)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

    blur= cv2.blur(resized,(5,5))
    thresh = cv2.threshold(blur,127, 255,cv2.THRESH_BINARY)[1]
    edges=cv2.Canny(thresh,50,50)

    return resized,edges

# main algoryth
def plot_coordinates(img1,edges1):
    ox, oy=[], []
    height=img1.shape[0]-1
    width=img1.shape[1]-1

    for x in range(width,):
        for y in range(height):
            if edges1[y,x]==255:
                
                ox.append(x)
                oppositey=height+1-y
                oy.append(oppositey)

    
    return ox,oy


def printXY(X1,Y1,x):
    print(X1[x])
    print(Y1[x])

def create_excel(X1,Y1):

    workbook = xlsxwriter.Workbook('new_data_set.xlsx')
    worksheet = workbook.add_worksheet()
    x_data=X1
    row = 0
    col = 0
    for item in (x_data):
        worksheet.write(row, col,item)
        # worksheet.write(row, col + 1, cost)
        row += 1
    y_data=Y1
    row = 0
    col = 1
    for item in (y_data):
        worksheet.write(row, col,item)
        # worksheet.write(row, col + 1, cost)
        row += 1
    workbook.close()

def getFarstuff(X1,Y1):
    smallest_y=min(Y1)
    biggest_x=max(X1)

    #entry points
    Entry_y_indexes=[i for i, j in enumerate(Y1) if j == smallest_y]
    
    Entry_x1= Entry_y_indexes[0]
    Entry_x2=Entry_y_indexes[1]




    Entry1= [X1[Entry_x1],Y1[Entry_y_indexes[0]]]
    Entry2= [X1[Entry_x2],Y1[Entry_y_indexes[1]]]


    entry_points=[Entry1,Entry2]

    #exit points
    exit_points = [[X1[-1],Y1[-1]],[X1[-2],Y1[-2]]]


    return entry_points, exit_points

def runAll(path):
    img,edges=init(path)
    ox,oy=plot_coordinates(img,edges)
    entry,exits=getFarstuff(ox,oy)
    check()
    pX,pY=main2(ox,oy,entry,exits,img.shape[0],img.shape[1])
    print(pX)
    print(pY)
    t,cyaw=mainLqr(pX,pY,img)
    return t,cyaw


def main(path):
    p=multiprocessing.Process(target=runAll,args=(path,))
    p.start()
    p.join()
if __name__ == "__main__": 
    path="C:/Users/matve/Desktop/pythonrtt/robo/Custom/path4.jpg"
    img=cv2.imread(path,2)
    cv2.imshow('image', img) 
    t, cyaw=runAll(path)
    create_excel(t,cyaw)
