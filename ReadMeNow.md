# Front end has Tailwind and Svelte Mui installed
## Run npm install in FE
## Run pipenv shell, then pipenv install -r requirements.txt in the BE
## BE main app is todos
## BE apis can check with localhost:8000/swagger or localhist:8000/redoc

https://madewithsvelte.com/svelte-mui

There is no CORS issue, if settings.py is specified which local host will be used

How to start FE? 
```bash
npm run dev
```

How to start BE?
```bash
pipenv shell
pipenv install -r requirements.txt
python manage.py runserver
```
Exit out from pipenv?
```bash
exit
```