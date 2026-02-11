from ultralytics import YOLO

img = "../../data/test/images/240_F_91026350_ym3XP5q5aCw3OQPXNqyZRn1vUUPOWSrK_jpg.rf.d63d7e386ba0998cc1606bee599ea7ac.jpg"

img1="../../data/test/images/240_F_517319578_YlPijgsTpqStayvRKbzm2xNOwkV4Kk9q_jpg.rf.ff53e92e62318bb1a9e71210778ca8a3.jpg"

img2="../../data/test/images/arbore-1-_webp.rf.641abbd870b9009013b3557b9956d4e4.jpg"

img3="../../data/test/images/arbore-4-_jpg.rf.b0ca0450f059149b2195a7306f95941b.jpg"

img4="../../data/test/images/arbore-10-_jpg.rf.099367e43ee1b8135a8361f384dffba1.jpg"

img5="../../data/test/images/bucsa-1-_jpg.rf.62dc733be890ed03e2689e2b85b6c107.jpg"

img6="../../data/test/images/bucsa-6-_jpg.rf.f39246a462648d30f25159807815fe06.jpg"

img7="../../data/test/images/flansa-2-_png.rf.a7dd1b37ce816f655ef051c7ecccdff4.jpg"

img8="../../data/test/images/flansa-6-_png.rf.512ca4b203e73d8b597080ebab70a330.jpg"

img9="../../data/test/images/flansa-10-_png.rf.48a6d0aad53371ada144045833462bb3.jpg"

img10="../../data/test/images/flansa-11-_png.rf.ec47c9bab581c798e45f6bca8d877aef.jpg"

img11="../../data/test/images/flansa-12-_png.rf.c3dee20dd0488c54a6df396079b9f710.jpg"

img12="../../data/test/images/flansa-19-_png.rf.4589d7d4f69bd809a4353af98a6e7940.jpg"
img13 = "Flanse INOX Pn 16 EN 1092 1 2002-mainthumb.jpg"
custom_clasifier ="runs/detect/train15/weights/best.pt" 
model =YOLO(custom_clasifier)

model.predict(source = img)
model.predict(source = img1)
model.predict(source = img2)
model.predict(source = img3)
model.predict(source = img4)
model.predict(source = img5)
model.predict(source = img6)
model.predict(source = img7)
model.predict(source = img8)
model.predict(source = img9)
model.predict(source = img10)
model.predict(source = img11)
model.predict(source = img12)
model.predict(source = img13)