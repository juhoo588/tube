from lightgbm import LGBMClassifier

def train_model(training_features, viral_labels):
    model = LGBMClassifier(
     n_estimators=500,
     learning_rate=0.03,
     max_depth=7
    )
    model.fit(training_features, viral_labels)
    return model

def predict_viral(model, features):
    viral_probability = model.predict_proba([features])[0][1]
    return viral_probability
