
# TONIGHT'S FIGHTS

This project is a web application that scrapes and displays fight schedules for boxing and MMA events. The application is built using Flask and BeautifulSoup, and includes pagination for easy navigation through the events.

## Features

- **Boxing Schedule Scraper**: Scrapes the latest boxing schedules from [Boxing News 24](https://www.boxingnews24.com/boxing-schedule/).
- **MMA Schedule Scraper**: Scrapes the latest MMA schedules from [MMA Fighting](https://www.mmafighting.com/schedule).
- **Pagination**: Allows users to navigate through multiple pages of fight schedules.
- **Support Page**: A dedicated page for support and donations.
- **Custom 404 Page**: Displays a custom 404 error page for non-existent routes.

## Technologies Used

- **Flask**: A micro web framework for Python.
- **BeautifulSoup**: A library for web scraping in Python.
- **Bootstrap**: A CSS framework for building responsive web pages.

## Getting Started

### Requirements:

Ensure you have the following installed:

- Python 3.x
- Flask
- Requests
- BeautifulSoup4

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/jos2ph/tonights-fights.git
    cd tonights-fights
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. **Set the Flask environment variables** (if needed):
    ```bash
    export FLASK_APP=app.py
    export FLASK_ENV=development
    ```

2. **Run the application**:
    ```bash
    flask run
    ```

3. Open your web browser and navigate to `http://127.0.0.1:5000/` to view the application.

## Project Structure

```
tonights-fights/
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── scripts.js
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── boxing.html
│   ├── mma.html
│   ├── support.html
│   └── 404.html
├── app.py
├── requirements.txt
└── README.md
```

## Routes

- `/`: Displays the boxing schedule.
- `/boxing`: Also displays the boxing schedule.
- `/mma`: Displays the MMA schedule.
- `/support`: Displays the support page.
- Custom 404 error page for undefined routes.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

- [Boxing News 24](https://www.boxingnews24.com/)
- [MMA Fighting](https://www.mmafighting.com/)
