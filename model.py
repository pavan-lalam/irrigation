from sklearn.linear_model import LinearRegression
import pandas as pd

data = pd.DataFrame({
    'moisture':[40,50,60,70],
    'temp':[25,30,35,28],
    'humidity':[60,65,70,75],
    'yield':[50,60,75,85]
})

X = data[['moisture','temp','humidity']]
y = data['yield']

model = LinearRegression()
model.fit(X,y)
