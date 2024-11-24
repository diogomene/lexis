from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score, GridSearchCV
from sklearn.metrics import make_scorer, accuracy_score, f1_score
from models.data_preparator import get_formated_data

def run(X, classes):
    print("Início de treino de Rede Neural MLP")

    # Definir os hiperparâmetros a serem testados
    param_grid = {
        'hidden_layer_sizes': [(100,), (50, 50)],
        'activation': ['relu', 'tanh']
    }

    # Inicializar o classificador MLP
    clf = MLPClassifier(max_iter=300)

    # Otimização de hiperparâmetros com GridSearchCV
    grid_search = GridSearchCV(clf, param_grid, cv=StratifiedKFold(n_splits=10))

    # Realizar a busca em grid
    grid_search.fit(X, classes)

    # Melhor modelo encontrado
    best_model = grid_search.best_estimator_
    melhores_params = grid_search.best_params_
    # Definir métricas
    print("\tinício de avaliação de modelo (kFold de 10)")
    scoring = {
        'accuracy': make_scorer(accuracy_score),
        'f1': make_scorer(f1_score, average='weighted')
    }


    # Avaliação com cross_val_score
    cv_results = cross_val_score(
        best_model, X, classes, cv=StratifiedKFold(n_splits=10), scoring=scoring, n_jobs=-1
    )
    print("\tfim de avaliação de modelo (kFold de 10)")

    # Resultados
    print("Fim de treino de Rede Neural MLP")
    print("====================")
    print(f"Melhores parâmetros: {melhores_params}")
    print("Acurácia Média: {:.4f}".format(cv_results['test_accuracy'].mean()))
    print("Desvio Padrão Acurácia: {:.4f}".format(cv_results['test_accuracy'].std()))
    print("F1-Score Médio: {:.4f}".format(cv_results['test_f1'].mean()))
    print("Desvio Padrão F1-Score: {:.4f}".format(cv_results['test_f1'].std()))
    print("====================")