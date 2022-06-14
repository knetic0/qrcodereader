import cv2
import qrcode
import webbrowser

cap = cv2.VideoCapture(0)

while True:
    deger, kare = cap.read()

    detect = cv2.QRCodeDetector()
    val, pts, st_code = detect.detectAndDecode(kare)

    if val:
        webbrowser.open_new_tab(val)
        cv2.putText(kare, "QR Code is found. Redirecting...", (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 2, cv2.LINE_AA)
        cap.release()
        cv2.destroyAllWindows()


    cv2.rectangle(kare, (400, 400), (30, 30), (0, 255, 0), thickness = 2) 

    cv2.imshow("Ekran", kare)

    if cv2.waitKey(1) & 0xff == ord('q'):
        print(val)
        break

cap.release()
cv2.destroyAllWindows()
