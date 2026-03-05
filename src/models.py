from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, export_text

from sklearn.metrics import classification_report

from build_logger import get_logger
from format_to_cpp import export_arduino_params

logger= get_logger(__name__)

def train_models(X_train, X_test, y_train, y_test):

    try:
        logger.info('starting model training')
        models= {
            "LR": LogisticRegression(class_weight= 'balanced', random_state= 7),
            "DT": DecisionTreeClassifier(max_depth=3, class_weight= 'balanced',random_state= 7)
        }


        for name,model in models.items():
            print(name)

            model.fit(X_train, y_train)
            preds= model.predict(X_test)

            logger.info(f"classification report for {name}\n{classification_report(y_test, preds)}")
            print(classification_report(y_test, preds))


        logger.info(f"Coefficients: {models["LR"].coef_}\nIntercept: {models["LR"].intercept_}")
        with open("../exports/lr_params.txt", "w") as f:
            f.write("coefficients:\n")
            f.write(",".join(map(str, models["LR"].coef_[0])))
            f.write("\n")

            f.write("intercept:\n")
            f.write(str(models["LR"].intercept_[0]))

        export_arduino_params("Coefficients", models["LR"].coef_[0], "a")
        export_arduino_params("Intercept", models["LR"].intercept_, "a")

        logger.info(f"{export_text(models["DT"])}")

        with open("../exports/dt_rules.txt", "w") as f:
            f.write(export_text(models["DT"]))

    except Exception as e:
        logger.exception('failed to train models')
        raise
    