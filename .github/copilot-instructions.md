# AI Coding Agent Instructions

## Project Overview
This is a Python project with a virtual environment setup. The project structure is being established, and this file serves as the definitive guide for AI agents to be productive in this codebase.

## Environment Setup

### Python Virtual Environment
- **Location**: `./venv/` (Python virtual environment)
- **Activation**: `D:\Project\venv\Scripts\activate` (Windows)
- **Python Version**: Check with `python --version` within activated environment
- **Package Management**: Use `pip` for installing dependencies
- **Requirements Format**: Store dependencies in `requirements.txt` or `pyproject.toml` (to be created)

### Initial Setup Steps
1. Activate the virtual environment: `.\venv\Scripts\activate`
2. Install project dependencies: `pip install -r requirements.txt` (once created)
3. Verify setup: `python -c "import sys; print(sys.executable)"`

## Project Structure (To Be Established)

When creating files, follow this structure:
- `src/` or `./` - Main application code
- `tests/` - Test files (use pytest)
- `docs/` - Documentation
- `.github/` - GitHub workflows and configurations
- `requirements.txt` - Project dependencies

## Development Conventions

### Code Style
- Python version: Target Python 3.8+ compatibility
- Formatting: Use consistent indentation (4 spaces)
- Naming: Follow PEP 8 conventions
  - Functions/variables: `snake_case`
  - Classes: `PascalCase`
  - Constants: `UPPER_SNAKE_CASE`

### Import Organization
When adding imports, organize in this order:
1. Standard library imports
2. Third-party imports
3. Local application imports
(Separate each group with a blank line)

### Documentation
- Add docstrings to all public functions/classes using triple quotes
- Format: Use consistent docstring style (Google or NumPy style recommended)
- Include type hints for function parameters and return values

## Common Commands

### Running Code
```bash
# Activate environment
.\venv\Scripts\activate

# Run a Python script
python script.py

# Run tests (when pytest is available)
pytest tests/
```

### Managing Dependencies
```bash
# Create requirements file
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt

# Install new package
pip install package_name
```

## Integration Points & Dependencies
- **External APIs**: Document any external service integrations in `./docs/integrations.md` (to be created)
- **Database**: Define database connections in a central config module
- **Environment Variables**: Use `.env` file (excluded from git) for sensitive configuration

## Testing & Quality

### When Adding Tests
- Create test files in `tests/` directory matching source structure
- Test files should be named `test_*.py` or `*_test.py`
- Use pytest as the testing framework
- Aim for meaningful test coverage of core business logic

### Before Committing
- Run tests to ensure nothing is broken
- Fix any import organization issues
- Verify code follows conventions

## Debugging Tips

- Use Python's built-in `pdb` debugger: `import pdb; pdb.set_trace()`
- For IDE debugging, VS Code: Use the Python extension with debugpy
- Check virtual environment is activated when issues occur with package imports
- Use `python -m` to run modules directly: `python -m module_name`

## Future Considerations

As the project grows:
1. Set up a `pyproject.toml` for modern Python packaging
2. Add pre-commit hooks for code quality
3. Configure GitHub Actions for CI/CD
4. Document architectural decisions in `docs/ADRs/` (Architecture Decision Records)
