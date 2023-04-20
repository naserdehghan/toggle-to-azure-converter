# Convert toggle export to azure devops task items import
1. Copy exported csv file from toggle to `files/source.csv` path.
2. Copy `.env.example` to `.env`
3. Fill `.env` variables
4. Run `python src/app.py`
5. Azure devops import file is `files/result.csv`
6. Done