Automating LinkedIn Connections with Python

Overview:
This Python script automates sending LinkedIn connection requests using Selenium. It logs into a LinkedIn account, searches for professionals based on a given keyword, filters results to display individual profiles, and sends connection requests efficiently.

Project Template:
For more details, refer to the original project template: https://www.geeksforgeeks.org/automate-linkedin-connections-using-python/

Author:
Kristian Tokos  
Date: March 25, 2025

Dependencies:
Ensure you have the following Python packages installed:
- selenium
- webdriver-manager

To install them, run:  
pip install selenium webdriver-manager

Setup and Execution:
1. Install Google Chrome and ChromeDriver.
2. Update the login credentials in the script (username and password).
3. Run the script:  
python linkedin_connect.py

Features:
- Logs into LinkedIn automatically
- Searches for profiles based on a keyword (e.g., "Software Engineer")
- Scrolls and dynamically loads additional search results
- Sends connection requests with a single click
- Handles errors gracefully to ensure smooth execution

Notes:
- Modify the search keyword to target specific professionals.
- Use responsibly: Automating LinkedIn connections should comply with LinkedIn's terms of service.
- The script may need adjustments if LinkedIn updates its UI or elements.

License:
This project is for educational purposes and should be used ethically.

Disclaimer:
The script requires valid LinkedIn credentials. Do not hard-code sensitive information in production.
