# train_climascout.py
import pandas as pd
import lightgbm as lgb
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import mean_squared_error
import joblib

df = pd.read_csv("era5_local_features.csv", parse_dates=["time"])
# create lags and rolling features
for lag in [1,3,6,24]:
    df[f"temp_lag_{lag}"]=df['temperature'].shift(lag)
df = df.dropna()

X = df.drop(columns=["time","target_temp"])
y = df["target_temp"]

ts = TimeSeriesSplit(n_splits=5)
best_model=None
for tr,te in ts.split(X):
    lgb_train = lgb.Dataset(X.iloc[tr], label=y.iloc[tr])
    lgb_eval = lgb.Dataset(X.iloc[te], label=y.iloc[te], reference=lgb_train)
    params = {"objective":"regression", "metric":"rmse", "verbosity":-1}
    gbm = lgb.train(params, lgb_train, num_boost_round=1000, valid_sets=[lgb_eval], early_stopping_rounds=50)
    preds = gbm.predict(X.iloc[te])
    print("fold rmse", mean_squared_error(y.iloc[te], preds, squared=False))
    best_model = gbm

joblib.dump(best_model, "climascout_lgbm.pkl")
