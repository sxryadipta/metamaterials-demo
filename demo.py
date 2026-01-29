import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor


np.random.seed(42)

N_SAMPLES = 20
N_FREQ = 100


X = np.random.uniform(
    low=[8, 6, 0.8],
    high=[14, 12, 2.0],
    size=(N_SAMPLES, 3)
)


Y = np.random.rand(N_SAMPLES, N_FREQ)


model = RandomForestRegressor(
    n_estimators=300,
    random_state=42
)

model.fit(X, Y)


idx = np.random.randint(0, N_SAMPLES)
prediction = model.predict(X[idx].reshape(1, -1))[0]


freq = np.linspace(5, 15, N_FREQ)

plt.plot(freq, Y[idx], label="True Spectrum")
plt.plot(freq, prediction, "--", label="Predicted Spectrum")
plt.xlabel("Frequency (GHz)")
plt.ylabel("Absorption")
plt.title("ML Forward Model (Random Forest)")
plt.legend()
plt.show()
