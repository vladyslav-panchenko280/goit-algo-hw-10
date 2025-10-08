import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


def f(x):
    """f(x) = x^2"""
    return x**2


def monte_carlo_integration(func, a, b, num_samples=100000):
    x_random = np.random.uniform(a, b, num_samples)

    y_random = func(x_random)

    integral = (b - a) * np.mean(y_random)

    return integral


def visualize_integration(func, a, b):
    x = np.linspace(-0.5, 2.5, 400)
    y = func(x)

    _, ax = plt.subplots()

    ax.plot(x, y, "r", linewidth=2, label="f(x) = x²")

    ix = np.linspace(a, b)
    iy = func(ix)
    ax.fill_between(ix, iy, color="gray", alpha=0.3, label="Область інтегрування")

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    ax.axvline(x=a, color="gray", linestyle="--")
    ax.axvline(x=b, color="gray", linestyle="--")
    ax.set_title(f"Графік інтегрування f(x) = x² від {a} до {b}")
    ax.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    a = 0
    b = 2

    visualize_integration(f, a, b)

    quad_result, quad_error = quad(f, a, b)

    print(f"\nІнтеграл функції f(x) = x^2 від {a} до {b}")
    print(f"Quad (еталон): {quad_result:.6f} (похибка: {quad_error:.2e})\n")

    samples_list = [1000, 10000, 100000, 1000000]

    for num_samples in samples_list:
        mc_result = monte_carlo_integration(f, a, b, num_samples)
        difference = abs(mc_result - quad_result)
        difference_percent = (difference / quad_result) * 100

        print(
            f"Монте-Карло ({num_samples} точок): {mc_result:.6f}, різниця: {difference_percent:.3f}%"
        )
