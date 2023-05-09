# SteamVision
Steam Vision is a web application which displays data collected from Steam. The application has functionality for collecting data from steam which can be setup to run or a regualr basis.

## Deployed App
**Link to deployed application:** https://steam-vision.herokuapp.com/

The deploy app uses Heroku and has the Heroku scheduler setup to run the data collection automatcially

## Installing and Running
- Pull the application repository
- Install all requirements in dependecies
- Project can be run by typing "python manage.py runserver" in the console

## Trying out locally
No data will be avaliable in the local version as it will not be connect or have any data

get some data for the game by running "python manage.py getgame --id {game_id_goes_here}"
get some review for the game by running "python manage.py getreviews --id {game_id_goes_here}"
