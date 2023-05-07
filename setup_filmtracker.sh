echo "Thanks for downloading FilmTracker." 
sleep 1
if ! [[ -x "$(command -v python3)" ]]
then
  echo 'Error: 
    FilmTracker requires Python 3 to run, but it looks like Python 3 is not installed.
    To install Python 3, please head to https://www.python.org/downloads/' >&2
  exit 1
fi
echo "Creating the virtual environment..."
python3 -m venv venv
sleep 1
echo "Activating the virtual environment..."
source venv/bin/activate
sleep 1
echo "Installing dependencies required to run PlantApp..."
pip install -r requirements.txt
sleep 1
echo "Setup Complete."