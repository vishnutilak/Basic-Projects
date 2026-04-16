import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import lightgbm as lgb

train_customers = pd.read_csv("train_customers.csv")
train_locations = pd.read_csv("train_locations.csv")
train_orders = pd.read_csv("orders.csv")
vendors = pd.read_csv("vendors.csv")

test_customers = pd.read_csv("test_customers.csv")
test_locations = pd.read_csv("test_locations.csv")

train = train_orders.merge(train_customers, on="customer_id", how="left")
train = train.merge(train_locations, on=["customer_id", "LOCATION_NUMBER"], how="left")
train = train.merge(vendors, left_on="vendor_id", right_on="id", how="left")

train["distance"] = np.sqrt(
    (train["latitude_x"] - train["latitude_y"])**2 +
    (train["longitude_x"] - train["longitude_y"])**2
)

user_features = train.groupby("customer_id").agg({
    "order_id": "count",
    "grand_total": "mean"
}).rename(columns={
    "order_id": "user_order_count",
    "grand_total": "user_avg_order_value"
}).reset_index()

train = train.merge(user_features, on="customer_id", how="left")

vendor_features = train.groupby("vendor_id").agg({
    "order_id": "count",
    "vendor_rating": "mean"
}).rename(columns={
    "order_id": "vendor_popularity",
    "vendor_rating": "vendor_avg_rating"
}).reset_index()

train = train.merge(vendor_features, on="vendor_id", how="left")

train["target"] = 1  # all are positive samples for now

all_vendors = train["vendor_id"].unique()

neg_samples = []

for cust in train["customer_id"].unique():
    ordered = train[train["customer_id"] == cust]["vendor_id"].unique()
    not_ordered = np.setdiff1d(all_vendors, ordered)

    sampled = np.random.choice(not_ordered, size=min(5, len(not_ordered)), replace=False)

    for v in sampled:
        neg_samples.append([cust, v, 0])

neg_df = pd.DataFrame(neg_samples, columns=["customer_id", "vendor_id", "target"])

neg_df = neg_df.merge(train_customers, on="customer_id", how="left")
neg_df = neg_df.merge(train_locations, on="customer_id", how="left")
neg_df = neg_df.merge(vendors, left_on="vendor_id", right_on="id", how="left")

# recompute distance
neg_df["distance"] = np.sqrt(
    (neg_df["latitude_x"] - neg_df["latitude_y"])**2 +
    (neg_df["longitude_x"] - neg_df["longitude_y"])**2
)

train_full = pd.concat([train, neg_df], ignore_index=True)

features = [
    "distance",
    "user_order_count",
    "user_avg_order_value",
    "vendor_popularity",
    "vendor_avg_rating"
]

train_full = train_full.fillna(0)

X = train_full[features]
y = train_full["target"]

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

model = lgb.LGBMClassifier(
    n_estimators=100,
    learning_rate=0.05,
    max_depth=6
)

model.fit(X_train, y_train)

test = test_customers.merge(test_locations, on="customer_id", how="left")

# create candidate pairs
test["key"] = 1
vendors["key"] = 1

test_candidates = test.merge(vendors, on="key").drop("key", axis=1)

# compute distance
test_candidates["distance"] = np.sqrt(
    (test_candidates["latitude_x"] - test_candidates["latitude_y"])**2 +
    (test_candidates["longitude_x"] - test_candidates["longitude_y"])**2
)

# merge features
test_candidates = test_candidates.merge(user_features, on="customer_id", how="left")
test_candidates = test_candidates.merge(vendor_features, on="vendor_id", how="left")

test_candidates = test_candidates.fillna(0)

# predict
test_candidates["score"] = model.predict_proba(test_candidates[features])[:, 1]

recommendations = test_candidates.sort_values(
    ["customer_id", "score"], ascending=[True, False]
)

top_recs = recommendations.groupby("customer_id").head(5)
