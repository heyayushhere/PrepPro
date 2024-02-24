# 📘 PrepPRO - Empowering Programmers for Success

PrepPRO is a comprehensive study platform designed to enhance programming skills and prepare individuals for technical interviews. This web application allows users to access curated roadmaps, practice coding with AI-generated interview questions, and visualize algorithms for effective learning.

## ✨ Features

- RoadMaps 🗺️: Clear and structured paths for beginners and experienced developers to master various programming domains.
- AI Interview Preparation 🤖: Dynamic question bank tailored to sharpen skills and prepare for technical interviews.




## 🎥 Demo Video

Check out our demo video to get a sneak peek into how PrepPRO can benefit you:
[Demo Video](https://www.canva.com/design/DAF5g5jJNmA/IxqNhjbMifsrvlpf8KrTRA/watch?utm_content=DAF5g5jJNmA&utm_campaign=designshare&utm_medium=link&utm_source=editor)

## 🛠️ Technologies Used

- Django: Web framework used to build the application.
- Python: Programming language used for backend development.
- HTML/CSS: Frontend markup and styling.
- SQLite: Database for storing user information and platform data.
- OpenAI GPT-3: Integration with ChatGPT for AI-powered interview questions.
- YouTube API: Used for retrieving relevant video content.
- Google Custom Search Engine (CSE) API: Utilized for fetching curated resources and information.
- OpenAI API: Integrated for language processing capabilities.

## 🚀 Getting Started

To run this project locally, follow these steps:

1. Clone the repository: `git clone <repository-url>`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up the database: `python manage.py migrate`
4. Set up the OpenAI API: Obtain an API key and update the `OPENAI_API_KEY` setting in the `settings.py` file.
5. Start the development server: `python manage.py runserver`
6. Access the application in your browser at `http://localhost:8000`

## ⚙️ Configuration

The following configurations can be modified in the `settings.py` file:

- `OPENAI_API_KEY`: Your OpenAI GPT-3 API key.
## ⚙️ Configuration

In the `settings.py` file, you'll find the following key-related configurations:

- `OPENAI_API_KEY`: Your OpenAI GPT-3 API key. This key is required for integrating ChatGPT for AI-powered interview questions.
- `YOUTUBE_API_KEY`: Your YouTube API key. This key is necessary for accessing relevant video content.
- `GOOGLE_CSE_API_KEY`: Your Google Custom Search Engine (CSE) API key. This key is used for fetching curated resources and information.


## 📄 License

This project is licensed under the [MIT License](LICENSE).


Contributions to this project are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.

## 📄 License

This project is licensed under the [MIT License](LICENSE).
