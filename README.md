# SpaceX Launches Visual Dashboard

This web application visualises past and upcoming SpaceX launches, categorizing them into successful, failed, and upcoming missions. It fetches data from the SpaceX API and displays it in an interactive format.

## Features
* Categorized launches: View successful, failed, and upcoming launches separately.
* Visually appealing cards: Each launch is presented in an informative card with key details.
* Easy navigation: Tabs allow you to switch between launch categories effortlessly.
* Upcoming launches: Stay informed about upcoming SpaceX missions.

![image](https://github.com/gappeah/Visualizing-SpaceX/assets/114095068/8d647a08-ed54-49f2-a16b-5d7de9a30b3c)
![image](https://github.com/gappeah/Visualizing-SpaceX/assets/114095068/00770016-5fc3-4af1-95c7-657f07356a08)
![image](https://github.com/gappeah/Visualizing-SpaceX/assets/114095068/bd67cc54-4b8b-488d-87c2-8505e84ff2ab)


https://github.com/gappeah/Visualizing-SpaceX/assets/114095068/572239e0-eb93-4d2f-b74a-1a6173398fd2


## Technologies Used
* Python: Back-end development using the Flask framework.
* Flask: Lightweight and flexible web framework for Python
* Requests: Library for making HTTP requests to the SpaceX API
* Jinja2: Templating engine for rendering dynamic HTML content
* Bootstrap: Front-end framework for styling and layout.

## Setup
* Clone this repository: git clone https://github.com/your-username/SpaceX-Visual-Dashboard
* Install dependencies: pip install -r requirements.txt
* Run the application: python app.py
* Access the dashboard in your browser at http://127.0.0.1:5000/

## File Structure
* app.py: Main Python file containing the Flask application logic.
* templates/: Directory containing HTML templates.
* index.html: Main template for the dashboard.
* launch_card.html: Template for individual launch cards.
* static/css/: Directory containing CSS stylesheets.
* styles.css: Custom CSS styles for the application.
