import cv2

# Загружаем фотографию
image = cv2.imread("photo_2022-03-03_13-15-11.jpg")

# Улучшаем качество фотографии
enhanced_image = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)

# Сохраняем улучшенную фотографию
cv2.imwrite("enhanced_image.jpg", enhanced_image)
