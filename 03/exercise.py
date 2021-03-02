
import keras
import numpy as np
from skimage import io


image = io.imread('./fake_id_2.png')
processedImage = np.zeros([1, 28, 28, 1])
for yy in range(28):
    for xx in range(28):
        processedImage[0][xx][yy][0] = float(image[xx][yy]) / 255


model = keras.models.load_model('./model.h5')
shownDigit = np.argmax(model.predict(processedImage))

if shownDigit == 4:
    print("Access Granted")
else:
    print("Access Denied")



layer_name = model.layers[-1].name
final_layer = model.layers[-1]

print("Layer name:",layer_name)
print("Bias name:", final_layer.bias.name)
print("Bias value:",final_layer.bias.numpy())


update_bias = final_layer.bias.numpy()
update_bias[4] = 100
final_layer.bias.assign(update_bias)
print("New Bias value:",final_layer.bias.numpy())


shownDigit = np.argmax(model.predict(processedImage))
if shownDigit == 4:
    print("Access Granted")
else:
    print("Access Denied")

