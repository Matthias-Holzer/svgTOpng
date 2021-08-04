import os
import glob
import time
start = time.time()

x=512
y=512
new_folder = 'png'+str(x)+'x'+str(y)+'/'
os.mkdir(new_folder)

#path for inkscape
path='/Applications/Inkscape.app/Contents/MacOS/inkscape'

#path for input files
files = glob.glob('/Users/matthiasholzer/PycharmProjects/imgResize/svg/*')


for file in files:
    print(file)
    os.system(path + " " +file+ " -w "+str(x)+" -h "+str(y)+" -o "+ new_folder + file.split("svg/")[1].split(".")[0] +".png")


#os.system(path + " 'svg/1fac0.svg' -w 128 -h 128 -o 'png128/1fac0.png'")
#os.system(path + " 'svg/1fac0.svg' -w 512 -h 512 -o 'png512/1fac0.png'")

end = time.time()
print("The Program took "+str(end-start)+"seconds to convert all the files")