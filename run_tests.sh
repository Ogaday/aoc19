# flake8 && \
mypy *.py && \
python -m doctest -o NORMALIZE_WHITESPACE *.py && \
python -m unittest
