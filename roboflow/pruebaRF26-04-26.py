import cv2
import time
from inference import InferencePipeline
from inference.core.interfaces.camera.entities import VideoFrame

# CONFIG
MODEL_ID = "waste-classification-o-i/2"
API_KEY = "VKQTIN7KpKl5M3jTqtmX"  # ⚠️ cambia esta key (no la expongas)

# CONTROL DE RENDIMIENTO
INTERVALO = 1.0  # segundos entre predicciones (1 = liviano)
ultimo_tiempo = 0

def render_prediction(predictions, video_frame: VideoFrame):
    global ultimo_tiempo

    ahora = time.time()

    # Reducir resolución (MUY importante para rendimiento)
    frame = cv2.resize(video_frame.image, (320, 240))

    # Solo procesar cada X segundos
    if ahora - ultimo_tiempo >= INTERVALO:
        ultimo_tiempo = ahora

        print("DEBUG:", predictions)

        # Manejo de diferentes formatos de respuesta
        if "predictions" in predictions and len(predictions["predictions"]) > 0:
            pred = predictions["predictions"][0]

            label = pred.get("class", "Unknown")
            confidence = pred.get("confidence", 0)

            print(f"Detectado: {label} ({confidence:.2%})")

            # Mostrar texto en pantalla
            cv2.putText(
                frame,
                f"{label} {confidence:.2%}",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

        elif "classification_results" in predictions:
            label = predictions["classification_results"].get("top", "Unknown")
            confidence = predictions["classification_results"].get("confidence", 0)

            print(f"Detectado: {label} ({confidence:.2%})")

            cv2.putText(
                frame,
                f"{label} {confidence:.2%}",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

        else:
            print("No detección")

    # Mostrar cámara
    cv2.imshow("Trash Classifier", frame)

    # Salir con Q
    if cv2.waitKey(1) & 0xFF == ord("q"):
        pipeline.terminate()


# PIPELINE
pipeline = InferencePipeline.init(
    model_id=MODEL_ID,
    video_reference=0,
    on_prediction=render_prediction,
    api_key=API_KEY,
    max_fps=2  # limita FPS (reduce uso CPU)
)

print("Starting trash classifier... Press 'q' to quit.")
pipeline.start()
pipeline.join()