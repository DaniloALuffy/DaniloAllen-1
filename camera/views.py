from django.shortcuts import render

#
#@gzip.gzip_page
def index(request):
    return render(request, "index.html")
#    try:
#        cam = VideoCamera()
#        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
#    except:
#        pass
#    return render(request, 'index.html')
#
##to capture video class
#class VideoCamera(object):
#    def __init__(self):
#        self.video = cv2.VideoCapture(0)
#        (self.grabbed, self.frame) = self.video.read()
#        self.myDataBefore = None  # Inicializa myDataBefore com um valor nulo
#        threading.Thread(target=self.update, args=()).start()
#
#    def __del__(self):
#        self.video.release()
#
#    def get_frame(self):
#        image = self.frame
#        _, jpeg = cv2.imencode('.jpg', image)
#        
#        for barcode in decode(image):
#            myData = barcode.data.decode("utf-8")
#            
#            if myData == self.myDataBefore:
#                myData = myData    
#            else:
#                print(myData)
#                self.myDataBefore = myData  # Atualiza myDataBefore com o valor de myData
#
#            pts = np.array([barcode.polygon],np.int32)
#            pts = pts.reshape((-1,1,2))
#            cv2.polylines(image,[pts],True,(255,0,255),5)
#            pts2 = barcode.rect
#            cv2.putText(image,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX, 0.9,(255,0,255),2)
#            
#        return jpeg.tobytes()
#
#
#
#    def update(self):
#        while True:
#            (self.grabbed, self.frame) = self.video.read()
#
#def gen(camera):
#    while True:
#        frame = camera.get_frame()
#        yield (b'--frame\r\n'
#               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

