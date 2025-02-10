## backend 
python --version
pip --version
cd .\backend\
python -m venv venv
.\venv\Scripts\activate

pip install uvicorn fastapi pymongo weasyprint requests pydantic

uvicorn main:app --reload

If that still doesn’t work, try:

python -m uvicorn main:app --reload


## frontend
cd .\frontend\
npm cache clean --force

Remove-Item -Recurse -Force node_modules
Remove-Item -Force package-lock.json

npm install

npm start