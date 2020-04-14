import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
sns.set()


housing_df= pd.read_csv(r'C:\Users\DELL\Python stuffs\HousingData.csv')

"""housing_df['AGE']= housing_df['AGE'].fillna(housing_df.mean())
housing_df['CHAS']= housing_df['CHAS'].fillna(0)
housing_df= housing_df.fillna(housing_df.median())
print(housing_df.isnull().any())"""

x=housing_df['MEDV']
y=housing_df['RM']

"""plt.scatter(x,y)

plt.show()
corr = housing_df.corr()
plt.figure(figsize=(8,6))
sns.heatmap(corr, xticklabels=corr.columns.values,yticklabels=corr.columns.values, cmap="Spectral_r", linewidths=1.25, alpha=0.8)
plt.show()
plt.figure(figsize=(10, 7))
sns.regplot(x,y)
plt.show()
X = sm.add_constant(x)
model = sm.OLS(y, X)
est = model.fit()
print(est.summary())

x = housing_df['RM']
y = housing_df['MEDV']
plt.boxplot(x)
plt.show()"""

x = housing_df['RM']
y = housing_df['MEDV']
plt.violinplot(x)
plt.show()



