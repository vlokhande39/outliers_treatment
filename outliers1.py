# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 17:19:41 2022

@author: Esha
"""

import pandas as pd
import numpy as np
import seaborn as sns

boston = pd.read_csv(r"C:\Users\SAI\Desktop\practice\boston_data.csv")

boston.info()

boston.dtypes

boston.value_counts()



# let's find outliers in crim
sns.boxplot(boston.crim)

# Detection of Outlier

iqr = boston['crim'].quantile(0.75) - boston['crim'].quantile(0.25)
lower_limit = boston['crim'].quantile(0.25) - (iqr * 1.5)
upper_limit = boston['crim'].quantile(0.75) + (iqr * 1.5)

# lets trim the data.

outliers_boston = np.where(boston['crim'] > upper_limit, True , np.where(boston['crim'] < lower_limit, True, False))
sum(outliers_boston)

boston_trimmed = boston.loc[~(outliers_boston), ]

boston.shape, boston_trimmed.shape

sns.boxplot(boston_trimmed.crim)# oulier is not showing [properly]
**********************************************************************************************************
# let's find outliers in zn
sns.boxplot(boston.zn)

# Detection of Outlier

iqr = boston['zn'].quantile(0.75) - boston['zn'].quantile(0.25)
lower_limit = boston['zn'].quantile(0.25) - (iqr * 1.5)
upper_limit = boston['zn'].quantile(0.75) + (iqr * 1.5)

# lets trim the data.

outliers_boston = np.where(boston['zn'] > upper_limit, True , np.where(boston['zn'] < lower_limit, True, False))
sum(outliers_boston)

boston_trimmed = boston.loc[~(outliers_boston),]

boston.shape, boston_trimmed.shape

sns.boxplot(boston_trimmed.zn)# oulier is not showing [properly]

************************************************************************************************************

# let's find outliers in indus
sns.boxplot(boston.indus)# There is no outlier.

****************************************************************************************************************
# let's find outliers in chas
sns.boxplot(boston.chas)

# Detection of Outlier

iqr = boston['chas'].quantile(0.75) - boston['chas'].quantile(0.25)
lower_limit = boston['chas'].quantile(0.25) - (iqr * 1.5)
upper_limit = boston['chas'].quantile(0.75) + (iqr * 1.5)

# lets trim the data.

outliers_boston = np.where(boston['chas'] > upper_limit, True , np.where(boston['chas'] < lower_limit, True, False))
sum(outliers_boston)

boston_trimmed = boston.loc[~(outliers_boston),]

boston.shape, boston_trimmed.shape

sns.boxplot(boston_trimmed.chas)# Now there is no outlier.

**************************************************************************************************************

# let's find outliers in nox
sns.boxplot(boston.nox)# There is no outlier.

**********************************************************************************************************
# let's find outliers in rm
sns.boxplot(boston.rm)# There is no outlier.

# Detection of Outlier

iqr = boston['rm'].quantile(0.75) - boston['rm'].quantile(0.25)
lower_limit = boston['rm'].quantile(0.25) - (iqr * 1.5)
upper_limit = boston['rm'].quantile(0.75) + (iqr * 1.5)

# lets trim the data.

outliers_boston = np.where(boston['rm'] > upper_limit, True , np.where(boston['rm'] < lower_limit, True, False))
sum(outliers_boston)

boston_trimmed = boston.loc[~(outliers_boston),]

boston.shape, boston_trimmed.shape

sns.boxplot(boston_trimmed.rm)# oulier is not showing [properly]
************************************************************************************************************

# let's find outliers in age
sns.boxplot(boston.age)# There is no outlier.

*********************************************************************************************
# let's find outliers in dis
sns.boxplot(boston.dis)# There is no outlier.

# Detection of Outlier

iqr = boston['dis'].quantile(0.75) - boston['dis'].quantile(0.25)
lower_limit = boston['dis'].quantile(0.25) - (iqr * 1.5)
upper_limit = boston['dis'].quantile(0.75) + (iqr * 1.5)

# lets trim the data.

outliers_boston = np.where(boston['dis'] > upper_limit, True , np.where(boston['dis'] < lower_limit, True, False))
sum(outliers_boston)

boston_trimmed = boston.loc[~(outliers_boston),]

boston.shape, boston_trimmed.shape

sns.boxplot(boston_trimmed.dis)# There is no outlier

**************************************************************************************************************
# let's find outliers in rad
sns.boxplot(boston.rad)# There is no outlier.
*******************************************************************************************************
# let's find outliers in tax
sns.boxplot(boston.tax)# There is no outlier.
****************************************************************************************************

# let's find outliers in ptratio
sns.boxplot(boston.ptratio)# There is no outlier.

# Detection of Outlier

iqr = boston['ptratio'].quantile(0.75) - boston['ptratio'].quantile(0.25)
lower_limit = boston['ptratio'].quantile(0.25) - (iqr * 1.5)
upper_limit = boston['ptratio'].quantile(0.75) + (iqr * 1.5)

# lets trim the data.

outliers_boston = np.where(boston['ptratio'] > upper_limit, True , np.where(boston['ptratio'] < lower_limit, True, False))
sum(outliers_boston)

boston_trimmed = boston.loc[~(outliers_boston),]

boston.shape, boston_trimmed.shape

sns.boxplot(boston_trimmed.ptratio)# There is no outlier
******************************************************************


# letsfind the outliers in the black
sns.boxplot(boston.black)

# detection of outlier
iqr = boston["black"].quantile(0.75) - boston["black"].quantile(0.25)
lower_limit = boston["black"].quantile(0.25) - (iqr * 5)
upper_limit = boston["black"].quantile(0.75) + (iqr *5)

# lets trim the data
outliers_boston = np.where(boston["black"] > upper_limit, True, np.where(boston["black"] < lower_limit, True,False))
sum(outliers_boston)

boston_trimmed = boston.loc[~(outliers_boston),]
boston.shape, boston_trimmed.shape

sns.boxplot(boston_trimmed.black)#There is outlier.

*****************************************************************************************************

# letsfind the outliers in the black
sns.boxplot(boston.lstat)

# detection of outlier
iqr = boston["lstat"].quantile(0.75) - boston["lstat"].quantile(0.25)
upper_limit = boston["lstat"].quantile(0.25) - (iqr * 5)
lower_limit = boston["lstat"].quantile(0.75) + (iqr *5)

# trim the data., 
outliers_boston = np.where(boston["lstat"] > upper_limit, True, np.where(boston["lstat"] < lower_limit, True, False))
sum(outliers_boston)

boston_trimmed = boston.loc[~(outliers_boston),]
boston.shape, boston_trimmed.shape

sns.boxplot(boston_trimmed.lstat)# there is no diagram is coming here.

****************************************************************************************************************

# letsfind the outliers in the medv

sns.boxplot(boston.medv)

# detection of the outlier
iqr = boston["medv"].quantile(0.75) - boston["medv"].quantile(0.25)
upper_limit = boston["medv"].quantile(0.25) - (iqr * 5)
lower_limit = boston["medv"].quantile(0.75) + (iqr * 5)

# trim the data

outliers_boston = np.where(boston["medv"] > upper_limit, True, np.where(boston["medv"] < lower_limit, True, False))
sum(outliers_boston)

boston_trimmed = boston.loc[~(outliers_boston),]
boston.shape, boston_trimmed.shape

sns.boxplot(boston_trimmed.medv)# There is no outlier.

**************************************************************************************************************************

# Replace technique.

sns.boxplot(boston.crim)

iqr = boston['crim'].quantile(0.75) - boston['crim'].quantile(0.25)
lower_limit = boston['crim'].quantile(0.25) - (iqr * 1.5)
upper_limit = boston['crim'].quantile(0.75) + (iqr * 1.5)

boston["boston_crim"] = np.where(boston["crim"] > upper_limit, upper_limit, np.where(boston["crim"] < lower_limit, lower_limit, boston["crim"]))

sns.boxplot(boston.crim)# still outlier is showing.

*********************************************************************************************************************
sns.boxplot(boston.zn)

iqr = boston['zn'].quantile(0.75) - boston['zn'].quantile(0.25)
lower_limit = boston['zn'].quantile(0.25) - (iqr * 1.5)
upper_limit = boston['zn'].quantile(0.75) + (iqr * 1.5)

boston["boston_zn"] = np.where(boston["zn"] > upper_limit, upper_limit, np.where(boston["zn"] < lower_limit, lower_limit, boston["zn"]))

sns.boxplot(boston.zn)# still outlier is showing.

*********************************************************************************************************************
# let's find outliers in chas
sns.boxplot(boston.chas)

# Detection of Outlier

iqr = boston['chas'].quantile(0.75) - boston['chas'].quantile(0.25)
lower_limit = boston['chas'].quantile(0.25) - (iqr * 1.5)
upper_limit = boston['chas'].quantile(0.75) + (iqr * 1.5)

boston["boston_chas"] = np.where(boston["chas"]  > upper_limit, upper_limit, np.where(boston["chas"] < lower_limit,lower_limit,boston["chas"]))

sns.boxplot(boston.chas)# outlier is showing.

*******************************************************************************************************************
# let's find outliers in rm
sns.boxplot(boston.rm)# There is no outlier.

# Detection of Outlier

iqr = boston['rm'].quantile(0.75) - boston['rm'].quantile(0.25)
lower_limit = boston['rm'].quantile(0.25) - (iqr * 1.5)
upper_limit = boston['rm'].quantile(0.75) + (iqr * 1.5)

boston["boston_rm"] = np.where(boston["rm"]  > upper_limit, upper_limit, np.where(boston["rm"] < lower_limit,lower_limit,boston["rm"]))

sns.boxplot(boston.rm) # outlier is coming.

*************************************************************************************************************************

sns.boxplot(boston.dis)

# Detection of Outlier

iqr = boston['dis'].quantile(0.75) - boston['dis'].quantile(0.25)
lower_limit = boston['dis'].quantile(0.25) - (iqr * 1.5)
upper_limit = boston['dis'].quantile(0.75) + (iqr * 1.5)

boston["boston_dis"] = np.where(boston["dis"]  > upper_limit, upper_limit, np.where(boston["dis"] < lower_limit,lower_limit,boston["dis"]))

sns.boxplot(boston.dis) # outlier is coming.  

******************************************************************************************************************
sns.boxplot(boston.ptratio)

# Detection of Outlier

iqr = boston['ptratio'].quantile(0.75) - boston['ptratio'].quantile(0.25)
lower_limit = boston['ptratio'].quantile(0.25) - (iqr * 1.5)
upper_limit = boston['ptratio'].quantile(0.75) + (iqr * 1.5)

boston["boston_ptratio"] = np.where(boston["ptratio"]  > upper_limit, upper_limit, np.where(boston["ptratio"] < lower_limit,lower_limit,boston["dis"]))

sns.boxplot(boston.ptratio) # outlier is coming.

*********************************************************************************************************************
sns.boxplot(boston.black)

# detection of outlier
iqr = boston["black"].quantile(0.75) - boston["black"].quantile(0.25)
lower_limit = boston["black"].quantile(0.25) - (iqr * 5)
upper_limit = boston["black"].quantile(0.75) + (iqr *5)

boston["boston_black"] = np.where(boston["black"]  > upper_limit, upper_limit, np.where(boston["black"] < lower_limit,lower_limit,boston["black"]))

sns.boxplot(boston.black)# still outlier is coming.


****************************************************************************************************************
# letsfind the outliers in the black
sns.boxplot(boston.lstat)

# detection of outlier
iqr = boston["lstat"].quantile(0.75) - boston["lstat"].quantile(0.25)
upper_limit = boston["lstat"].quantile(0.25) - (iqr * 5)
lower_limit = boston["lstat"].quantile(0.75) + (iqr *5)

boston["boston_lstat"] = np.where(boston["lstat"]  > upper_limit, upper_limit, np.where(boston["lstat"] < lower_limit,lower_limit,boston["lstat"]))

sns.boxplot(boston.lstat)# still outlier is coming.

********************************************************************************************************

sns.boxplot(boston.medv)

# detection of the outlier
iqr = boston["medv"].quantile(0.75) - boston["medv"].quantile(0.25)
upper_limit = boston["medv"].quantile(0.25) - (iqr * 5)
lower_limit = boston["medv"].quantile(0.75) + (iqr * 5)

boston["boston_medv"] = np.where(boston["medv"]  > upper_limit, upper_limit, np.where(boston["medv"] < lower_limit,lower_limit,boston["medv"]))

sns.boxplot(boston.medv)# still outlier is coming.
****************************************************************************************************************************

