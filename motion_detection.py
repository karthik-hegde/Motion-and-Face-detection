from SimpleCV import *
cam=Camera()
threshold=5.0

disp=Display()
#capture the first image
previous=cam.getImage()

count=0
count_face=0
while not disp.isDone():
    current=cam.getImage() #capture another frame
    img=cam.getImage()
    diff=current-previous#get difference b/w the images
    matrix=diff.getNumpy()#get a array with width x height x RGB dimensions
    mean = matrix.mean()#get mean to compare with threshold
    if mean>=threshold :
        img.dl().selectFont('pursia')
        img.drawText("motion detected",x=10,y=10)
        print "motion detected"
        count= count +1
        path="C:\Users\karthik\Motion_detect\ " +str(count) +".png"
        if count==1 :
            img.save(path)
        elif count%3==0 :
            img.save(path)
        
        
    previous=current
    img=cam.getImage().flipHorizontal()  # change from mirrored image
    face_segment=HaarCascade("face.xml")# load the face definations included in the SimpleCV
    gray=img.grayscale()
    autoface=gray.findHaarFeatures(face_segment) #variable to check for all face like features
    if(autoface is not None):                   #if face is detected do the following
        face=autoface[-1].boundingBox()         #rectangle box for the largest face detected
        x=face[0]
        y=face[1]
        w=face[2]
        h=face[3]
        facelayer=DrawingLayer(img.size())      #draw a layer on the face

        facebox=facelayer.rectangle((x,y),(w,h),color=Color.GREEN,width=2,filled=False,) #adds a rectangle in the given co ordinate
        img.addDrawingLayer(facelayer)
        img.applyLayers()                       #applies the layer to be visible on the output
        img.dl().selectFont('pursia')           #font for text
        count_face= count_face + 1
        img.drawText("face detected",x=5,y=5)   #text on left corner, face detected
        cropped = img.crop(x,y,w+10,h+10)
        path2="C:\Users\karthik\Face_detect\ " +str(count) +".png"
        if count_face==1 :
            cropped.save(path2)
        elif count%2==0 :
            cropped.save(path2)
    img.show()
