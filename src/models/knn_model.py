from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import StratifiedKFold, cross_validate, GridSearchCV
from sklearn.metrics import make_scorer, accuracy_score, f1_score
from data_preparator import get_formated_data

def run(X, classes):
    print("Início de treino a partir de KNN")
    # Definir os hiperparâmetros a serem testados
    param_grid = {
        'n_neighbors': [3, 5, 7],
        'weights': ['distance'],
        'metric': ['euclidean','cosine']
    }

    # Inicializar o classificador KNN
    clf = KNeighborsClassifier()

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

    # Avaliação com cross_validate
    cv_results = cross_validate(
        best_model, X, classes, cv=StratifiedKFold(n_splits=10), scoring=scoring
    )
    print("\tfim de avaliação de modelo (kFold de 10)")

    # Resultados
    print("Fim de treino a partir de KNN")
    print("====================")
    print(f"Melhores parâmetros: {melhores_params}")
    print("Acurácia Média: {:.4f}".format(cv_results['test_accuracy'].mean()))
    print("Desvio Padrão Acurácia: {:.4f}".format(cv_results['test_accuracy'].std()))
    print("F1-Score Médio: {:.4f}".format(cv_results['test_f1'].mean()))
    print("Desvio Padrão F1-Score: {:.4f}".format(cv_results['test_f1'].std()))
    print("====================")
