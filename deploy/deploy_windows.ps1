echo "Adding to Git"
git add .
git commit -m "'$1'"
git push

ssh -i C:\Users\DavidMcCreery\Downloads\althris.pem ubuntu@ec2-54-78-114-97.eu-west-1.compute.amazonaws.com "sudo su; cd /var/www/54.78.114.97/public_html/althris_tutor_bot; pm2 stop flask_api; pm2 stop analytics_api; git pull; source env/bin/activate; env/bin/python3 -m pip install -r requirements.txt; pm2 start src/flask_api.py --interpreter env/bin/python3; pm2 start src/analytics_api.py --interpreter env/bin/python3; pm2 save" 