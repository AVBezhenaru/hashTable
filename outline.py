9. Хэширование
1. Хэш-таблицы и хэш-функции

Когда мы будем знакомиться с алгоритмами поиска, то узнаем, что в общем случае сложность поиска нужного элемента в упорядоченном массиве (когда есть возможность обращаться к произвольным элементам по индексу) можно снизить с O(n) до O(log n). Однако существуют структуры данных, которые ориентированы на максимально быстрый поиск нужной информации (проверку её наличия в хранилище), буквально за время O(1). Такие структуры называются хэш-таблицы.

Идея хэш-таблицы в том, что по значению содержимого i-го элемента таблицы мы можем быстро и однозначно определить сам индекс i (говорят - слот). Такое вычисление слота выполняет специальная хэш-функция.

Если диапазон значений, хранимых в таблице, не превышает её размер, то хэш-функция элементарна. Например, мы хотим хранить байты (значения от 0 до 255) в таблице размером 256 элемента. В таком случае хэш-функция f(x) = x : само значение элемента и есть его индекс в таблице. Мы просто смотрим, имеется ли значение N в таблице по индексу N.

Но идея хэш-таблиц в другом: мы хотим хранить значения потенциально очень широкого диапазона (например, строки) в таблице маленького размера (например, 128 элементов). При этом мы исходим из того, что и хранимые данные по своей уникальности примерно близки своим количеством размеру хэш-таблицы. Мы можем, например, суммировать байты каждой строки, брать остаток от деления суммы на 128, и таким образом получать уникальный индекс.

Большая проблема в том, что идеальную хэш-функцию придумать подчас очень трудно или невозможно. В нашем случае самые разные строки могут выдавать один и тот же слот -- такая ситуация называется коллизией. Решается эта проблема, во-первых, подбором оптимальной хэш-функции, которая минимизирует количество коллизий, и во-вторых, так называемым разрешением коллизий, когда несколько разных значений претендуют на один слот.

2. Методы разрешения коллизий

Существует довольно много методов разрешения коллизий. Один из самых простых, не требующих дополнительного объёма памяти -- это метод линейного разрешения, частным случаем которого считается метод последовательных проб.

Значение, попадающее в слот, который уже занят, перемещается к следующему слоту (в общем случае, "перепрыгивает" через N слотов), где проверяется, свободен ли он. Такой поиск продолжается циклически, и желательно продумывать размер хэш-таблицы и размер шага такими, чтобы при длительном поиске в конечном итоге охватывалось бы всё её пространство -- с неоднократным прохождением по таблице. Или как минимум, чтобы индекс, дойдя до конца таблицы, продолжал бы с её начала, пока не превысил бы исходно выбранный слот. Шаг N может быть не фиксированным, а например, растёт квадратично: 1,2,4,8,...

Недостаток данного метода в том, что подчас эффективность поиска может быть очень плохой, когда коллизий много и приходится многократно пробегать по всей таблице, которая сильно заполнена. А когда в ней вообще нету свободных слотов, добавление элемента становится невозможным, в таких случаях обычно используют динамические массивы. Кроме того, в линейном разрешении нередко проявляется проблема кластеризации -- занятые слоты группируются в кластеры, которые замедляют поиск свободных ячеек.

Полностью снимает эти проблемы метод цепочек. Он подразумевает хранение в каждом слоте не одного значения, а целого списка значений. В него записываются все значения, для которых хэш-функция его выбрала. Недостаток -- необходимость ведения таких списков и ощутимое замедление работы, если коллизии возникают часто, и приходится дополнительно сканировать длинные списки. Более того, если все значения будут попадать в одну ячейку, мы получим среднее время выборки, пропорциональное O(N). В таком случае использование хэш-таблицы вообще теряет смысл, можно просто задействовать связанные списки например.

В качестве компромиссного был придуман метод двойного хэширования, когда используются две совершенно разные хэш-функции h1() и h2(). Если слот k = h1(v) занят, тогда вычисляется h1(v) + i * h2(v) по модулю длины таблицы, где i принимает значения от 1 до длины таблицы - 1. Особое требование к h2(), чтобы она возвращала индексы слотов, взаимно простые с длиной таблицы. Например, эту длину можно взять простым числом, тогда h2() будет возвращать натуральные числа, меньшие этой длины.

3. Реализация

В классе хэш-таблицы потребуются два параметра: размер хэш-таблицы (желательно простое число, для экспериментов можно например брать 17 или 19), и длину шага (количество слотов) для поиска следующего свободного слота (например, 3).

class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
В этом классе требуется реализовать четыре метода:

- хэш-функцию hash_fun(value), которая по входному значению вычисляет индекс слота;

- функцию поиска слота seek_slot(value), которая по входному значению сперва рассчитывает индекс хэш-функцией, а затем отыскивает подходящий слот для него с учётом коллизий, или возвращает None, если это не удалось;

- put(value), который помещает значение value в слот, вычисляемый с помощью функции поиска;

- find(value), который проверяет, имеется ли в слотах указанное значение, и возвращает либо слот, либо None.

Напишите тесты, которые проверяют работу этих четырёх методов.


class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        # в качестве value поступают строки!

        # всегда возвращает корректный индекс слота
        return 0

    def seek_slot(self, value):
        # находит индекс пустого слота для значения, или None
        return None

    def put(self, value):
        # записываем значение по хэш-функции

        # возвращается индекс слота или None,
        # если из-за коллизий элемент не удаётся
        # разместить
        return None

    def find(self, value):
        # находит индекс слота со значением, или None
        return None