
temp = 1
from gluonts.dataset import common
from gluonts.model.deepar import DeepAREstimator
from gluonts.mx.trainer import Trainer

trainer = Trainer(epochs=10)
estimator = DeepAREstimator(freq='5min', prediction_length=12, trainer=trainer)



temp = 1


