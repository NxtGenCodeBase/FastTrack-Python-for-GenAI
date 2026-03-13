# Day 21: Isolated Environments
To avoid "Dependency Hell" in AI, always use venvs.
- Create: `python -m venv ai_env`
- Activate (Windows): `.\ai_env\Scripts\activate`
- Activate (Mac/Linux): `source ai_env/bin/activate`
- Freeze requirements: `pip freeze > requirements.txt`