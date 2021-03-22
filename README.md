# ERP Planspiel Dashboard
A dashboard for monitoring the ERPsim game from HEC Montreal.

It allows players to quickly analyze the data that is relevant for the game.
The data is updated every 10 seconds.

![Screenshot of Dashboard](https://i.postimg.cc/xTGyDWJd/Bildschirmfoto-2021-03-22-um-19-07-37.png)

# Viewing the dashboard
## Requirements
A machine running Python3 is needed. Running the application in a [virtual environemnt](https://docs.python.org/3/tutorial/venv.html) is highly recommended.
Install the dependencies via 
```
pip3 install -r requirements.txt
```
## 1. Viewing the dashboard locally
### Set-up environment secrets
Create a file named `.env` in the main folder. Put your credentials and server url in it.
```
SERVICEURL=put_the_url_from_the_sap_system
USERNAME=your_username
PASSWORD=your_password
```
You can find the URL in the OData-Service tab in the SAP system. It is the same one that is required to connect with Excel.

### Run the project
You can run the project via 
```
python3 app.py
```

You will see your dashboard at http://127.0.0.1:8050/ in your browser.

## 2. Deploy via Haroku
In order to access the dashboard outside your local network, you need to deploy it. 
The easiest way and how it is configured currently is to use [Heroku](https://heroku.com/). It is free to use.

The way how to do it is documented [here](https://devcenter.heroku.com/articles/git).

As the username and password are not exposed in the code, it is necessary to configure them as seen [here](https://devcenter.heroku.com/articles/config-vars).

The keys and values are the same as specified in 1. of this readme.
