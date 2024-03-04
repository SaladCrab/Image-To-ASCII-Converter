from PIL import Image

# File that will get converted
imag = Image.open("Picture.png")
WIDTH, HEIGHT = imag.size
imag = imag.convert('RGB')

# File that the program will write to clear it after opening
fw = open("FileToWriteTo.txt", "a")
fw.truncate(0)

for i in range(HEIGHT):
    fw.write("\n")     
    for j in range(WIDTH):
        
        #----------------------------------
        # Gets the pixel by location then gets the color values then calculates the brightness of said pixel
        pixelRGB = imag.getpixel([j, i])
        R, G, B = pixelRGB
        brightness = float(sum([R, G, B]) / 3) # value of 0 = black --- value of 255 = white
        brightness = brightness * 4 #turns the value from 255 to a easier to understand number 1020
        #----------------------------------
        
        if brightness < 100:
            fw.write("@ ")
        elif brightness >= 100.0 and brightness < 200.0:
            fw.write("# ")
        elif brightness >= 200 and brightness < 300:
            fw.write("& ")
        elif brightness >= 300 and brightness < 400:
            fw.write("? ")
        elif brightness >= 400 and brightness < 500:
            fw.write(") ")
        elif brightness >= 500 and brightness < 600:
            fw.write("/ ")
        elif brightness >= 600 and brightness < 700:
            fw.write("^ ")
        elif brightness >= 700 and brightness < 800:
            fw.write("* ")
        elif brightness >= 800 and brightness < 900:
            fw.write(", ")
        elif brightness >= 900 and brightness < 1000:
            fw.write(". ")
        else:
            fw.write(".")
fw.close()
        
            

            
            
            
        
        
        