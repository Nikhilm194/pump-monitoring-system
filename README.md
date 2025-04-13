# pump-monitoring-system
This project focuses on developing a real-time industrial device monitoring and control system using HTML/CSS/JavaScript for the frontend and Python/Flask for the backend. The system integrates with REST APIs to fetch dynamic data from simulated devices (Pump1, Pump2, Pump3) and displays it via an interactive dashboard. Key features include real-time data visualization (charts and tables), device state management via Modbus protocol (using Python libraries like pymodbus), and seamless communication with a Modbus server (port 5001). The backend handles API interactions and Modbus write operations, while the frontend ensures a responsive and intuitive UI. Bonus tasks like historical data playback and CSV export were also explored.
## Frontend System 
This web-based dashboard provides real-time monitoring and control for industrial pump systems, built with modern web technologies. The frontend features a responsive interface using Bootstrap CSS, interactive pump control switches, and dynamic charts (via Chart.js) displaying performance metrics and status overviews. It communicates with a Flask backend through RESTful API endpoints to fetch live pump states (simulated data), toggle pump operations, and handle system resets. The interface auto-updates every 2 seconds, includes visual feedback for user actions, and offers emergency controls. Designed as a single-page application, it uses pure JavaScript for DOM manipulation and async/await for seamless API integration. Requires pairing with the provided Flask backend server for full functionality and demonstrates industrial IoT concepts through simulated pump interactions.
## Backend System 
This repository features a Flask web server with CORS support that serves a static index.html page and provides several simulated APIs. It offers endpoints for random device states, generating historical data for water and lime pumps (maintaining a 20-point data window), toggling pump states via POST requests, and resetting the system’s data. Although a Modbus client is initialized for potential hardware integration, the current setup uses simulated data for testing and demonstration purposes.
![image alt](https://github.com/Nikhilm194/pump-monitoring-system/blob/main/pump%20monitoring%20system.png?raw=true)
