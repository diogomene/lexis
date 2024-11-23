from typing import Literal
from decision_tree_model import run as run_decision_tree_model
from knn_model import run as run_knn_model
from logistic_regression_model import run as run_logistic_regression_model
from naive_bayes_model import run as run_naive_bayes_model
from neural_mlp_model import run as run_mlp_model
from data_preparator import get_formated_data
MODELS_LITERALS = Literal["decision_tree", "knn", "logistic_regression", "naive_bayes", "mlp", "all"]

def run_model(model: MODELS_LITERALS) -> None:
    X, classes = formatted_data = get_formated_data()
    if(model == "decision_tree"):
        run_decision_tree_model(X, classes)
    elif (model == "knn"):
        run_knn_model(X, classes)
    elif (model == "logistic_regression"):
        run_logistic_regression_model(X, classes)
    elif (model == "naive_bayes"):
        run_naive_bayes_model(X, classes)
    elif (model == "mlp"):
        run_mlp_model(X, classes)
    elif (model == "all"):
        run_decision_tree_model(X, classes)
        run_knn_model(X, classes)
        run_logistic_regression_model(X, classes)
        run_naive_bayes_model(X, classes)
        run_mlp_model(X, classes)
    else:
        raise ValueError("Fonte de catalogo invalida")

run_model("knn")