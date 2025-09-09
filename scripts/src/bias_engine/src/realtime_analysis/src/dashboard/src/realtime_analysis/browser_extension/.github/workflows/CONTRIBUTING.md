# Contributing to CBDA

We welcome contributions! Please follow these guidelines:

## Development Setup

1. Fork the repository
2. Clone your fork
3. Create a virtual environment
4. Install dependencies: `pip install -r requirements.txt`
5. Install pre-commit hooks: `pre-commit install`

## Code Style

- Follow PEP 8 guidelines
- Use type hints where appropriate
- Write docstrings for all functions and classes
- Include tests for new features

## Pull Request Process

1. Create a feature branch
2. Make your changes
3. Add or update tests
4. Update documentation
5. Submit a pull request

## Adding New Bias Types

1. Update the bias taxonomy in `data/bias_taxonomy.csv`
2. Modify the detection logic in `src/bias_engine/inference.py`
3. Add test cases in `tests/test_bias_detection.py`
