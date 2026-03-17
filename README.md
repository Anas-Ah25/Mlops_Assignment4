# Context

Assignment 4 in Mlops

> Testing the github workflows on a test repo 

## What this includes
- GitHub Actions workflow: `.github/workflows/ml-pipeline.yml`
- Minimal Python file: `app.py`
- Minimal dependencies: `requirements.txt`

## Workflow behavior
- Runs on every push except `main`
- Runs on pull requests
- Installs dependencies
- Performs tiny lint/syntax check
- Runs model dry test (`torch` import)
- Uploads `README.md` as artifact `project-doc`
