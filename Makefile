# Makefile for setting up and running the multimodal search application

# Setup: Make the setup script executable and run it
setup:
	chmod +x ./setup.sh &&\
		./setup.sh

# Install: Upgrade pip and install required Python packages
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

# Test: Run pytest for both Python scripts and Jupyter notebooks
test:
	python -m pytest -vv --cov=main test_*.py &&\
	python -m pytest --nbval notebook.ipynb

# Format: Format the Python code using the Black formatter
format:
	black *.py

# Lint: Run pylint on the Python code
lint:
	pylint --disable=R,C *.py

# Refactor: Run both formatting and linting
refactor: format lint

# Deploy: Add deployment commands here
deploy:
	# deploy goes here

# Run: Run the Streamlit app
run:
	streamlit run app.py

# RunAPI: Make the main script executable and run it
runapi:
	chmod +x ./main.py &&\
		./main.py

run-docker:
	docker build -t multimodal-search . &&\
		docker run -p 80:80 multimodal-search

# All: Run all of the above commands
all: install lint test format deploy
