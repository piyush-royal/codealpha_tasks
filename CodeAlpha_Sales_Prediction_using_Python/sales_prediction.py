import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("advertising.csv")

print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)
print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

df.drop("Unnamed: 0", axis=1, inplace=True)

print(df.head())
X = df[['TV', 'Radio', 'Newspaper']]
y = df['Sales']
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Data:", X_train.shape)
print("Testing Data:", X_test.shape)
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)

print("Model Trained Successfully!")
y_pred = model.predict(X_test)

print("\nFirst 5 Predictions:")
print(y_pred[:5])
from sklearn.metrics import mean_absolute_error, r2_score

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation")
print("MAE:", mae)
print("R2 Score:", r2)
importance = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_
})

print("\nAdvertising Impact:")
print(importance)

plt.figure(figsize=(6,4))
plt.bar(
    importance['Feature'],
    importance['Coefficient']
)

plt.title("Advertising Impact on Sales")
plt.xlabel("Advertising Platform")
plt.ylabel("Impact Coefficient")

plt.tight_layout()

plt.savefig("advertising_impact.png")

plt.show()