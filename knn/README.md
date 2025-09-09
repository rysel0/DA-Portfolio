# Custom k-Nearest Neighbors (KNN)

👨‍💻 Собственная реализация алгоритма **k ближайших соседей** для классификации и регрессии.

## Особенности
- ⚙️ Поддержка выбора числа соседей (`n_neighbors`) и режима: `classification` / `regression`
- 📊 Применение на стандартных датасетах:
  - `Iris` — классификация
  - `Diabetes` — регрессия
- 📈 Визуализация результатов:
  - Confusion Matrix для классификации
  - График предсказаний vs истинные значения для регрессии
  - Прямая \(y = x\) для наглядного сравнения точности предсказаний
- 🔍 Сравнение с `sklearn` KNN для проверки корректности реализации

## Используемые инструменты
- Python
- NumPy
- Matplotlib
- scikit-learn (для сравнения и метрик)

## Пример использования
```python
# Классификация
knn = KNearestNeighbors(n_neighbors=5, regression=False)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

# Регрессия
knn_reg = KNearestNeighbors(n_neighbors=5, regression=True)
knn_reg.fit(X_train, y_train)
y_pred_reg = knn_reg.predict(X_test)
