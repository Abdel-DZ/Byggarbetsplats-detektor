1. Byggarbetsplats‑detektor (YOLOv8)
Detta projekt implementerar ett detekteringssystem för byggarbetsplatser baserat på YOLOv8. Systemet identifierar personer samt säkerhetsrelaterade objekt som hjälm och huvud (utan hjälm). Projektet inkluderar träningsdata, annoteringar, träningsresultat och en körbar applikation för att analysera bilder och videofiler.

2. Funktioner
- Detekterar följande klasser:

--Person

--Helmet

--Head

- Stöd för analys av bilder och videofiler

- Backend för modellkörning

- Visualisering av detekteringar med bounding boxes och confidence‑värden

- Fullständiga träningsresultat inkluderade i projektet

- Systemet är förberett för vidare utveckling, exempelvis stöd för live‑kamera‑input samt utökning av detekteringsklasser som skyddsväst, maskiner och andra säkerhetsrelaterade objekt.

3. Teknisk stack
- Python 3.10+

- Ultralytics YOLOv8

- OpenCV

- Flask eller Streamlit

- PyTorch (används av YOLOv8)

- Numpy och Pandas

4. Projektstruktur
Byggarbetsplats-detektor/
│
├── app.py                     # Frontend / användargränssnitt
├── detector_backend.py        # Backend för YOLO-modellen
├── data.yaml                  # Dataset-konfiguration
│
├── images/                    # Tränings- och valideringsbilder
├── labels/                    # YOLO-annoteringar
│
├── runs/                      # YOLOv8 träningsresultat (plots, weights, metrics)
│   ├── detect/train/
│   ├── detect/train2/
│   └── detect/train4/
│
├── test_results_train4/       # Modellens prediktioner på testbilder
│
└── yolov8n.pt                 # Modellvikt (YOLOv8n)
5. Träning av modellen

Modellen tränades med YOLOv8 på ett dataset med tre klasser:
0	Person
1	Helmet
2	Head

Efter träningen analyserades modellens prestanda genom att läsa in YOLO:s results.csv och visualisera följande:

- Träningsförluster:

--train/box_loss

--train/cls_loss

--train/dfl_loss

- Valideringsförluster:

--val/box_loss

--val/cls_loss

--val/dfl_loss

-Utvärderingsmetrik över epoker:

--Precision

--Recall

--mAP50

--mAP50‑95

Dessa grafer genererades manuellt med Matplotlib baserat på YOLO:s loggfil.

Modellvikter (best.pt och last.pt)

Resultaten finns i katalogerna runs/detect/train*.

6- Installation och körning
- Installera beroenden
pip install -r 
--ultralytics
--opencv-python
--flask
--numpy
--pandas
--torch

- Starta applikationen (Streamlit)
-- streamlit run app.py
  eller
-- py -m streamlit run app.py


7- Exempelresultat
Projektet innehåller färdiga prediktioner i:

test_results_train4/
Dessa visar modellens prestanda på testbilder.

8- Kontakt
Skapad av Abdel/Abbe
GitHub: https://github.com/Abdel-DZ
