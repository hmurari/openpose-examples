import cv2
import time
import datetime

image_capture_enabled = True
display_window_enabled = True 

def test_fps_simple():
    device = "/dev/video0"
    video = cv2.VideoCapture(device)

    fps = video.get(cv2.CAP_PROP_FPS)
    print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

    w, h = video.get(cv2.CAP_PROP_FRAME_WIDTH), video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print("Using default resolution: {}x{}".format(w, h))

    # Number of frames to capture
    num_frames = 120
    print("Capturing {0} frames".format(num_frames))

    # Start time
    start = time.time()

    # Grab a few frames
    frame_idx = 0
    while True:
        frame_idx+=1

        ret, frame = video.read()

        if frame_idx >= num_frames:
            break

        if display_window_enabled:
            try:
                cv2.imshow('Test', frame)
                if cv2.waitKey(10) == 27:
                    break  # esc to quit
            except Exception as ex:
                pass

        if image_capture_enabled and frame_idx % 10 == 0:
            cv2.imwrite(datetime.datetime.now().isoformat() + '.jpg', frame)


    # End time
    end = time.time()

    # Time elapsed
    seconds = end - start
    print("Time taken : {:.2f} seconds, Num Frames Captured: {}".format(seconds, num_frames))

    # Calculate frames per second
    fps = num_frames / seconds
    print("Estimated frames per second : {:.2f}".format(fps))

    # Release video
    video.release()

if __name__ == '__main__':
    test_fps_simple()
