import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import GradientBoostingClassifier
import joblib



def get_data(path):
    df = pd.read_csv(path)
    return df


def preprocess_data(df):
    target = "Weather Type"
    numeric_cols = [
    'Temperature', 'Humidity', 'Wind Speed', 'Precipitation (%)',
    'Atmospheric Pressure', 'UV Index', 'Visibility (km)'
     ]
    categorical_cols = ['Cloud Cover', 'Season', 'Location']
    X = df.drop(columns=[target])
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
    )
    numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler())
    ])
    categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
     ])
    preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_cols),
        ("cat", categorical_transformer, categorical_cols)
    ]
    )
    return X_train, X_test, y_train, y_test, preprocessor



def train_model(X_train, y_train, preprocessor):
    gb_model = GradientBoostingClassifier(
        learning_rate=0.05,
        max_depth=3,
        n_estimators=100,
        random_state=42
        )  

    clf = Pipeline(steps=[
            ("preprocessor", preprocessor),
            ("classifier", gb_model)
            ])
    clf.fit(X_train, y_train)    
    return clf


def save_model(model, filename):        
    joblib.dump(model, filename)
    print(f"Model saved to {filename}")


df=get_data('data\weather-classification.csv')
X_train, X_test, y_train, y_test, preprocessor= preprocess_data(df)
clf= train_model(X_train, y_train, preprocessor)
save_model(clf, "weather_model.pkl")

 


