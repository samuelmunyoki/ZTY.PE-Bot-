from PIL import ImageGrab, ImageOps
import pyautogui
from pytesseract import pytesseract
import numpy as
import cv2
import string
import random

pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

while 1:
    print("Capturing Image")
    screenshot = ImageGrab.grab(bbox=(13, 129, 644, 3217))
    # gray_image = ImageOps.grayscale(screenshot)
    img = cv2.resize(screenshot, None, fx=2, fy=2)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    sentence = pytesseract.image_to_string(gray_image).split()
    words = []
    for word in sentence:
        word = word.translate(str.maketrans('', '', string.punctuation))
        words.append(word)
    print("Words extracted\n"
          "=====================================\n{}\n=====================================".format(words))

    if len(words) > 0:
        for word in words:
            random_click = random.uniform(0.05, 0.1)
            pyautogui.write(word, interval=random_click)
