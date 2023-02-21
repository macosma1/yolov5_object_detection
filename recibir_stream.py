import cv2

# in_rtp = "udpsrc port=5200 ! application/x-rtp,\ encoding-name=JPEG,payload=26 ! rtpjpegdepay ! jpegdec ! autovideosink"
# cap = cv2.VideoCapture(in_rtp, cv2.CAP_GSTREAMER)

gstreamer_str='udpsrc port=8650 caps = "application/x-rtp, media=(string)video, clock-rate=(int)90000, \
        encoding-name=(string)H264,\
         payload=(int)96" ! rtph264depay ! decodebin ! videoconvert ! appsink'

cap = cv2.VideoCapture(gstreamer_str, cv2.CAP_GSTREAMER)

if not cap.isOpened():
    print("Cannot capture test src. Exiting.")
    quit()

while True:
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imshow("CVtest",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



# #--------------------------------------------MACM
# #1,2,3 video
# #gstreamer_str = 'udpsrc port=8554 auto-multicast=0 ! application/x-rtp, media=video, encoding-name=H264 ! rtpjitterbuffer latency=300 ! rtph264depay ! decodebin ! videoconvert ! video/x-raw,format=BGR ! appsink drop=1'

# #sirve  #4to video
# # gstreamer_str = 'udpsrc port=8554 ! application/x-rtp, media=video, encoding-name=H264 ! rtpjitterbuffer ! rtph264depay ! decodebin ! videoconvert ! appsink drop=1'

# #sirve     #5to video
# #gstreamer_str = 'udpsrc port=8554 ! application/x-rtp, media=video, encoding-name=H264 ! rtpjitterbuffer latency=0 buffer-mode=auto ! rtph264depay ! decodebin ! videoconvert ! appsink drop=1'

# #original:
# # gstreamer_str = 'udpsrc port=8554 caps = "application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264, payload=(int)96" ! rtph264depay ! decodebin ! videoconvert ! appsink drop=1'


# # cap = cv2.VideoCapture(gstreamer_str, cv2.CAP_GSTREAMER)

# #sirve mejor
# #6to y 7mo
# cap = cv2.VideoCapture(
#     'udpsrc port=8554 caps = "application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264"'
#     ' ! rtph264depay'
#     ' ! avdec_h264'
#     ' ! videoconvert'
#     ' ! appsink drop=1', cv2.CAP_GSTREAMER)

# ## otro que no tengo en video , es del 7 feb
# # cap = cv2.VideoCapture(
# #         "udpsrc port=8554 "
# #         "! application/x-rtp, payload=96 ! rtph264depay ! h264parse ! avdec_h264 "
# #         "! decodebin ! videoconvert ! video/x-raw,format=(string)BGR ! videoconvert "
# #         "! appsink max-buffers=1 drop=true",cv2.CAP_GSTREAMER)




# #prueba de recibir por terminal
# ##gst-launch-1.0 -e -v udpsrc port=8554 ! application/x-rtp, payload=96 ! rtpjitterbuffer ! rtph264depay ! h264parse ! avdec_h264 ! autovideosink fps-update-interval=1000 sync=false


# #--------------------------------------------------------------------------------------envio pruebas-----------------------------------------------------------------------------------------------------------

# #usa el summit
#  # gst-launch-1.0 -v v4l2src device=/dev/video6 ! video/x-raw,width=1280,height=720 ! autovideoconvert ! x264enc name=videoEnc threads=0 bitrate=3000 tune=zerolatency speed-preset=ultrafast key-int-max=30 qp-min=8 qp-max=51 qp-step=1 ! video/x-h264, profile=baseline ! rtph264pay config-interval=0 mtu=1200 name=pay0 ! udpsink host=192.168.18.13 port=8554 sync=true 

# ##tenia este como opcion para mejorar la velocidad de transmision del summit
#   ## gst-launch-1.0 -v v4l2src device=/dev/video6 ! video/x-raw, width=1280,height=720! videoconvert ! videoscale ! x264enc bitrate=3000 tune=zerolatency speed-preset=fast ! rtph264pay ! udpsink host=192.168.18.13 port=8554 sync=true

# ##otros que sirven, pero debo ver tiempo
#     ##gst-launch-1.0 v4l2src device=/dev/video6 ! "video/x-raw,latency=0", width=1280,height=720! videoconvert ! videoscale  ! x264enc bitrate=3000 tune=zerolatency speed-preset=fast ! "video/x-h264" ! rtph264pay name=pay0 pt=96 ! udpsink host=192.168.18.13 port=8554 sync=false
#     ##gst-launch-1.0 -v v4l2src device=/dev/video6 num-buffers=1500 ! video/x-raw,format=YUY2,width=640,height=480,framerate=30/1 ! autovideoconvert ! ximagesink

# #no me sirven 7 feb
#     ## gst-launch-1.0 -v v4l2src device=/dev/video6 ! video/x-raw, format=I420,width=1280,height=720,framerate=20/1 ! videoconvert ! x264enc tune=zerolatency bitrate=3000 speed-preset=superfast ! rtph264pay ! udpsink host=10.236.26.210 port=8554 sync=true 
#     ## gst-launch-1.0 -v v4l2src device=/dev/video6 ! video/x-raw, width=1280,height=720, framerate=30/1 ! videoconvert ! videoscale ! x264enc bitrate=3000 tune=zerolatency speed-preset=superfast ! rtph264pay mtu=900 ! udpsink host=10.236.26.210 port=8554 sync=true 

# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------