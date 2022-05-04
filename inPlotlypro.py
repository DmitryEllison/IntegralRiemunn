import math

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class IntegralRiemunn():
    def __init__(self, a, b, f, N, type="mid"):
        self.a = a
        self.b = b
        self.f = f
        self.N = N
        self.type = type
        self.X = np.linspace(a, b, N)  # дробление отрезка
        self.Y = f(self.X)  # вычисление значение в точках

    def calculate_integral(self, n):
        w = (b - a) / n  # наша пси
        result = 0
        if self.type == "mid":
            result = sum([f(a + i * w + 0.5 * w) for i in range(0, n)])
        elif self.type == "left":
            result = sum([f(a + i * w) for i in range(0, n)])
        elif self.type == "right":
            result = sum([f(a + (i + 1) * w) for i in range(0, n)])
        else:
            result = 0
            print("Incorrect type of integrate")
        return result * w

    # анимация
    # Создание i графика
    def animate(self, i):
        plt.cla()  # очистить оси

        # создание новых осей x = [a, b] и y = [от округленного минимума, до окргуленного максимума]
        ax = plt.axes(xlim=(self.a, self.b), ylim=(math.floor(min(self.Y)), math.ceil(max(self.Y))))

        ax.set_xticks(np.linspace(a, b, 11))  # ось Ox
        ax.set_xlabel('X-axis', fontsize=30)

        ax.set_yticks(np.linspace(0, 1, 11))  # ось Oy
        ax.set_ylabel('Y-axis', fontsize=30)

        ax.tick_params(labelsize=22)  # редактируем размер делений

        num_trapezoids = (i + 1) * factor  # вычисляем количество трапеций

        x = np.linspace(self.a+(self.b-self.a)/(2*self.N), self.b, num_trapezoids + 1)  # создание интервалов на оси абцисс
        y = f(x)  # генерация значений функций

        y_int = self.calculate_integral(num_trapezoids)  # вычисление интегралов
        err = (1 - 1 / np.e) - y_int  # ошибка между правильным и истинным значением

        # левые точки без последней точки
        x_points = []
        y_points = []
        if self.type == "mid":
            x_points = [i + (a+b)/(2*num_trapezoids) for i in x[:-1]]
            y_points = [self.f(i) for i in x_points]
        elif self.type == "left":
            x_points = x[:-1]
            y_points = y[:-1]
        elif self.type == "right":
            x_points = x[1:]
            y_points = y[1:]

        ax.plot(x_points, y_points, c='#2CBDFE', marker='.', markersize=10)  # построение точек для ступенчатой функции
        ax.plot(self.X, self.Y, c='#2CBDFE')  # построение функции

        x_points_bar = x_points
        if self.type == "mid":
            x_points_bar = [x - (b-a)/(2*num_trapezoids) for x in x_points]
        elif self.type == "right":
            x_points_bar = [x - (b-a)/num_trapezoids for x in x_points]

        bar = ax.bar(x_points_bar, y_points, width=1.0 * (b - a) / num_trapezoids, alpha=0.3, align='edge', color='#47DBCD',
                     edgecolor='#2CBDFE', lw=2)
        prediction = math.e / (24*(i+1)^2) if type == "mid" else math.e / (2*(i+1))

        ax.set_title('Интеграл $\int_{{0}}^{{1}} \\ e^{-x}dx$. \n' +
                     '{0} Трапеций: Значение: {1:.9f} \n Ошибка {2:.9f} и ее оценка {3:.9f}'.format(num_trapezoids, y_int, err, prediction), fontsize=30)
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)

        print((i+1)*factor, err)
        return bar

    def show_mistake(self, n, type):
        ...

    def show(self):
        fig = plt.figure(figsize=(21, 14))
        plt.axis('off')
        anim = animation.FuncAnimation(fig, self.animate, frames=40, interval=120, blit=True)
        anim.save('e_x_left.gif', writer="Pillow")


f = lambda x: np.exp(-x)  # наша замечательная функция
a, b = 0, 1  # отрезок интегрирования
N = 200  # количество точек деления
factor = 5  # увеличение количеств точек деления

int = IntegralRiemunn(a, b, f, N, type="left")
int.show()
