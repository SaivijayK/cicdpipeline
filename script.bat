cd ..
cd Flask-application-One
git pull
kill -9 $(lsof -t -i:5000)
python App.py