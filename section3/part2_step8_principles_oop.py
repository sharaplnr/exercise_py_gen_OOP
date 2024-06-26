# Принципы ООП
# Абстракция
# Инкапсуляция
# Наследование
# Полиморфизм

# Абстракция - это использование только тех характеристик объекта, которые с достаточной точностью
# представляют его в системе. Основная идея состоит в том, чтобы представить объект минимальным
# набором атрибутов и методов и при этом с достаточной точностью для решаемой задачи

# Абстракция является основной ООП и позволяет работать с объектами не вдаваясь в особенности
# их реализации. Пользователь типа не имеет прямого доступа к его реализации, но может работать
# с данными через предоставленный набор операций. Преимущество абстракции данных в разделении
# операции над данными и внутреннего представления этих данных, что позволяет изменять реализацию
# не затрагивая пользователей данного типа.

# Принцип абстракции позволяет скрывать детали и раскрывать только основные черты объекта.



# Инкапсуляция имеет два основных смысла. С одной стороны она объединяет атрибуты и методы в одном объекте.
# С другой стороны инкапсуляция обозначает сокрытие данных, то есть невозможность напрямую получить доступ
# к внутренней структуре объекта, тк это может быть небезопасно. (Пример с желудком, напрямую внутрь желудка
# положить еду можно, но это небезопасно, поэтому напрямую доступ к желудку закрыт, чтобы это сделать, можно
# воспользоваться интерфейсом под названием рот.

# Принцип инкапсуляции позволяет объектам содержать как свои данные, так и поведение, а также скрывать то,
# что ему потребуется, от внешнего программного кода.



# Наследование - способ создания класса на основе уже существующего, при котором дочерний класс заимствует
# атрибуты и методы родительского класса, а также добавляет собственные.

# Наследование может быть одиночным, а может быть множественным. При множественном наследование, у класса может
# быть более одного родителя. Это дает большую гибкость, но в то же время это потенциальный источник ошибок.


# Полиморфизм - это множество форм. Однако в понятиях ООП имеется в виду, скорее, обратное. Объекты разных классов,
# с разной внутренней реализацией, могут иметь одинаковые интерфейсы. Пример со знаком "+", для объектов, класса
# чисел, он обозначает сложение, для строк конкатенация. Интерфейс одинаковый, а внутренняя реализация и результат
# операции разная, в этом и проявляется полиморфность.

# Полиморфизм позволяет выполнить одно действие разными способами, другими словами, он позволяет определить один
# интерфейс и иметь множество реализаций.



# Примечание
# Наследование является механизмом повторного использования кода. Установка отношения наследования между классами
# пораждает иерархию.
# При наследовании дочерний класс наследует все атрибуты и методы родительского класса, а также может дополнять(переопределять)
# их собственными.

# Хорошие статьи по основам ООП доступны - https://habr.com/ru/articles/87119/ .