from keras.datasets import mnist

(x_train, y_train), (x_test, y_test)=mnist.load_data()
print("y",y_train)
print("x",y_train)
x_train = (x_train.astype(np.float32) -127.5)/127.5

print(x_train.shape)

x_train = x_train.reshape(x_train.shape[0],x_train.shape[1]*x_train.shape[2])
print(x_train.shape)

plt.imshow(x_test[11]), plt.show()