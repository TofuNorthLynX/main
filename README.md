# main
порядок выполнения предобработки и разведочного анализа данных:

-

алгоритмы кодирования категориальных признаков:

(LabelEncoder) самый простой способ - нумерация значений (0, 1, 2, 3, ..)
у данного подхода есть существенный недостаток - обычно ведёт к плохому результату, так как алгоритмы начинают учитывать бессмысленную упорядоченность значений признаков. однако имеет преимущество с точки зрения памяти.

(OneHotEncoder) one-hot кодирование. суть заключается в создании дополнительных N признаков, где N - количество уникальных категорий.
новые признаки принимают значения 0 или 1 в зависимости от принадлежности к категории.
значительно увеличивает объем данных, что неэффективно с точки зрения памяти, частично эту проблему решает применение разреженных матриц.

(Mean Encoding) метод среднего кодирования - предполагает кодирование категорий средним арифметическим от суммы целевых меток. велика вероятность переобучения модели.

Алгоритм построения модели линейной регрессии:

импорт библиотек
предоставление данных
создание модели
обучение модели

проверка исходных данных
рачет параметров модели
анализ модели
проверка адекватноси модели
определение меры точности модели
построение прогноза и доверительных интервалов
разработка общих выводов и рекоммендаций по практическому применению построенной модели
