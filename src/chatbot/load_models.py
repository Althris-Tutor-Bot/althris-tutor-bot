"""--------------------
Tries to load DNN. If one does not exist then will create a new one and fit it.
Out:
    model - The neural net model that will be used to predict responses.
--------------------"""


import tensorflow as tf
import tflearn as tfl
import os


def load_model(self):
    tf.compat.v1.reset_default_graph()
    net = tfl.input_data(shape=[None, len(self.training[0])])
    net = tfl.fully_connected(net, 8)
    net = tfl.fully_connected(net, 8)
    net = tfl.fully_connected(net, len(self.output[0]), activation="softmax")
    net = tfl.regression(net)

    self.model = tfl.DNN(net)

    try:
        self.model.load(os.path.join(os.path.dirname(__file__), "..", "..", "Data", "model.tfl"))  # Tries to load the model
    except Exception:  # If the model couldn't load, it trains a new one and saves it in a "Data" folder
        tf.compat.v1.reset_default_graph()
        net = tfl.input_data(shape=[None, len(self.training[0])])
        net = tfl.fully_connected(net, 8)
        net = tfl.fully_connected(net, 8)
        net = tfl.fully_connected(net, len(self.output[0]), activation="softmax")
        net = tfl.regression(net)
        model = tfl.DNN(net)

        model.fit(self.training, self.output, n_epoch=1000, batch_size=8, show_metric="true")  # Trains the model
        model.save(os.path.join(os.path.dirname(__file__), "..", "..", "Data", "model.tfl"))

        self.model = model
