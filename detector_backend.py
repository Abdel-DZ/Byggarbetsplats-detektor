# detector_backend.py
# Backend-funktion som kör YOLO-detektering åt app.py

from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image
import tempfile

# Ladda YOLO-modell EN gång när filen importeras
model = YOLO("runs/detect/train4/weights/best.pt")  


def detect_objects(image):
    """
    Tar en PIL-bild från frontend, kör YOLO-detektering,
    ritar bounding boxes och returnerar:
    - result_image (PIL)
    - stats (dict med antal objekt per klass)
    """

    # Konvertera PIL → OpenCV-format
    img_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Kör YOLO-modellen
    results = model(img_cv, verbose=False)

    stats = {}

    # Loopar igenom alla detekterade objekt (för statistik)
    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])                # klass-ID
            label = model.names[cls]             # klassnamn
            stats[label] = stats.get(label, 0) + 1

    # YOLO ritar automatiskt (samma stil som video)
    annotated = results[0].plot()

    # Konvertera tillbaka till PIL
    result_image = Image.fromarray(cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB))

    return result_image, stats


def detect_video(video_file):
    # Spara videon temporärt
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(video_file.read())
    tfile.flush()

    cap = cv2.VideoCapture(tfile.name)

    # REAL‑TIME YOLO STREAMING
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, verbose=False)
        annotated = results[0].plot()  # YOLO ritar automatiskt

        yield annotated  # STREAMA FRAMES DIREKT

    cap.release()
