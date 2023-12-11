# Awesome YouTube Video Search with Flask

Welcome to the Awesome YouTube Video Search repository! This project provides a cool web application built with Flask that allows you to search for YouTube videos and view the results in a neat interface.

## Getting Started

### Prerequisites

Make sure you have [Python](https://www.python.org/) installed on your machine.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/developerlight/scrapping_youtube_flask.git
   ```

2. Navigate to the project directory:

   ```bash
   cd scrapping_youtube_flask
   ```

3. Install the required dependencies:

   ```bash
   pip install Flask google-api-python-client
   ```

4. Set up your YouTube Data API key:

   Obtain an API key from the [Google Cloud Console](https://console.cloud.google.com/) and replace `API_KEY` in `app.py` with your actual API key.

### Usage

1. Start the Flask app:

   ```bash
   python app.py
   ```

2. Open your browser and go to [http://localhost:5000](http://localhost:5000).

3. Enter a keyword in the search bar and discover awesome YouTube videos!

## Features

- Utilizes the YouTube Data API to fetch video information
- Sleek Flask web interface for a delightful user experience
- Dynamic search results with video thumbnails

## File Structure

- **`app.py`**: Main Flask application.
- **`templates/index.html`**: HTML template for rendering the search interface.

## Contributing

Contributions are welcome! Please check out the [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Hat tip to Flask and the YouTube Data API for making this project possible.

Enjoy searching for awesome YouTube videos! 🎉
