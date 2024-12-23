import pyautogui
import time
import pyscreeze
import os

# Resim yolları

image_paths = [
    os.path.join(os.path.dirname(__file__), "düsman.png")
]

# Bekleme süresi (ekranın yüklenmesini beklemek için)
time.sleep(10)

# Resimleri sırayla kontrol et
found = False
for image_path in image_paths:
    print(f"Aranıyor: {image_path}")
    
    try:
        # Resmi ekranın üzerinde bulmaya çalış
        button_location = pyautogui.locateOnScreen(image_path)
        
        # Eğer resim bulunursa
        if button_location:
            print(f"Resim bulundu! Koordinatlar: {button_location}")

            # Resmin merkezi koordinatlarını al
            button_center = pyautogui.center(button_location)

            # Koordinatlara gitmek için fareyi taşı
            pyautogui.moveTo(button_center, duration=1)

            # Tıklama işlemi
            pyautogui.click()
            found = True
            time.sleep(10)
            pyautogui.click(800, 400)

            pyautogui.click(800, 450)
            

            pyautogui.click(860, 450)

            pyautogui.click(739, 450)
            
            pyautogui.click(739, 400)

            pyautogui.click(739, 500)
            
   
            pyautogui.click(860, 500)
       
            pyautogui.click(700, 500)
            
  
            pyautogui.click(860, 550)
         
            pyautogui.click(900, 500)
         
         
            pyautogui.click(739, 550)
        
            pyautogui.click(739, 600)
            
        
            pyautogui.click(700, 600)
       
            pyautogui.click(860, 600)
            
           
            pyautogui.click(800, 600)
            pyautogui.press("ctrl")


    except pyautogui.ImageNotFoundException:
        print(f"{image_path} bulunamadı.")
    except Exception as e:
        print(f"Hata oluştu: {e}")

if not found:
    print("Hiçbir resim bulunamadı!")
exit_key = 'esc'