import logging
from typing import Callable

type number = int | float
type SquareRootFunction = Callable[[number], number]
type InnerCreationStepFunction = Callable[[number], number]
type DistanceFunction = Callable[[number, number], number]


def configure_logging(
    *, format_specifier_string: str = "%(asctime)s - %(levelname)s - %(message)s"
) -> None:
    logging.basicConfig(level=logging.INFO, format=format_specifier_string)


def approximate_plastic_ratio(
    *,
    previous_approximation: float = 1.0,
    current_approximation: float = 1.0,
    step_count: int = 100,
    tolerance: float = 1e-20,
    square_root_function: SquareRootFunction = lambda x: x**0.5,
    inner_creation_step: InnerCreationStepFunction = lambda x: 1 + 1 / x,
    distance_function: DistanceFunction = lambda x, y: abs(x - y),
    number_of_digits: int = 20,
) -> None:
    for current_step in range(step_count):
        previous_approximation = current_approximation
        current_approximation = square_root_function(
            inner_creation_step(previous_approximation)
        )
        if distance_function(previous_approximation, current_approximation) < tolerance:
            logging.info(
                f"Approximation converged in {current_step} steps with tolerance {tolerance}..."
            )
            logging.info(
                f"Plastic ratio approximation: {current_approximation:.{number_of_digits}f}"
            )
            return
    logging.info(
        f"Approximation did not converge in {step_count} steps with tolerance {tolerance}..."
    )


def main(*args, **kwargs) -> None:
    """
    Approximating the plastic ratio via nested radicals.
    https://en.wikipedia.org/wiki/Plastic_ratio
    """
    configure_logging()
    approximate_plastic_ratio()


if __name__ == "__main__":
    main()
