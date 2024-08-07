import cv2
import face_recognition as fr

# cargar imagenes
foto_A = fr.load_image_file("FotoA.jpg")
foto_B = fr.load_image_file("FotoB.jpg")

# pasar imagenes a RGB
foto_A = cv2.cvtColor(foto_A, cv2.COLOR_BGR2RGB)
foto_B = cv2.cvtColor(foto_B, cv2.COLOR_BGR2RGB)

# localizar cara A
lugar_cara_A = fr.face_locations(foto_A)[0]
cara_codificacada_A = fr.face_encodings(foto_A)[0]

# mostar rectangulo A
cv2.rectangle(foto_A,
              (lugar_cara_A[3], lugar_cara_A[0]),
              (lugar_cara_A[1], lugar_cara_A[2]),
              (0, 255, 0),
              2)

# localizar cara B
lugar_cara_B = fr.face_locations(foto_B)[0]
cara_codificacada_B = fr.face_encodings(foto_B)[0]

# mostar rectangulo B
cv2.rectangle(foto_B,
              (lugar_cara_B[3], lugar_cara_B[0]),
              (lugar_cara_B[1], lugar_cara_B[2]),
              (0, 255, 0),
              2)

# realizar comparación
resultado = fr.compare_faces([cara_codificacada_A], cara_codificacada_B)

# medida de la distancia
distancia = fr.face_distance([cara_codificacada_A], cara_codificacada_B)

# mostrar resultados
cv2.putText(foto_B,
            f"{resultado} {distancia.round(2)}",
            (50, 50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0, 255, 0),
            2)

# mostar imagenes
cv2.imshow("Foto control", foto_A)
cv2.imshow("Foto prueba", foto_B)

# mantener el programa abierto
cv2.waitKey(0)
