# 🎯 Quzo - AI-Powered Quiz Management System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)
[![Google AI](https://img.shields.io/badge/Google%20AI-Gemini-orange.svg)](https://ai.google.dev/)
[![Railway](https://img.shields.io/badge/Deploy-Railway-purple.svg)](https://railway.app/)

A modern, AI-powered quiz management system built with Flask that allows educators to create, manage, and deploy quizzes with intelligent question generation using Google's Gemini AI.

## ✨ Features

### 🎓 For Educators
- **AI Quiz Generation**: Generate intelligent quiz questions on any topic using Google Gemini AI
- **Manual Quiz Creation**: Create custom quizzes with multiple question types
- **Student Management**: Track student progress and performance
- **Real-time Results**: View quiz results and analytics in real-time
- **Secure Authentication**: Role-based access control for professors and students

### 📚 For Students
- **Interactive Quiz Taking**: Clean, intuitive interface for taking quizzes
- **Progress Tracking**: View your quiz history and performance
- **Instant Feedback**: Get immediate results and explanations
- **Mobile Responsive**: Take quizzes on any device

### 🤖 AI-Powered Features
- **Smart Question Generation**: AI creates contextually relevant questions
- **Multiple Choice Questions**: Automatically generated with plausible distractors
- **Topic Flexibility**: Generate questions on virtually any subject
- **Quality Assurance**: AI ensures question clarity and difficulty balance

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key
- Git

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Shivam-Shukla0/quzoo.git
   cd quzoo
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env and add your Google Gemini API key
   GEMINI_API_KEY=your_gemini_api_key_here
   SECRET_KEY=your_secret_key_here
   ```

5. **Initialize the database**
   ```bash
   python app1.py
   ```

6. **Access the application**
   Open your browser and navigate to `http://localhost:5100`

## 🌐 Deployment

### Railway Deployment (Recommended)

1. **Fork this repository** to your GitHub account

2. **Create a Railway account** at [railway.app](https://railway.app)

3. **Deploy from GitHub**:
   - Connect your GitHub account
   - Select this repository
   - Railway will automatically detect it's a Python project

4. **Set environment variables** in Railway dashboard:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   SECRET_KEY=your_super_secret_key_here
   FLASK_ENV=production
   DEBUG=False
   ```

5. **Deploy** - Railway will automatically build and deploy your application!

### Manual Deployment

For other platforms (Heroku, DigitalOcean, etc.), ensure you:
- Set the required environment variables
- Use the provided `Procfile` for process management
- Configure the database URL if using PostgreSQL

## 📋 Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `GEMINI_API_KEY` | Google Gemini AI API key | Yes | None |
| `SECRET_KEY` | Flask secret key for sessions | Yes | Generated |
| `DATABASE_URL` | Database connection URL | No | SQLite |
| `FLASK_ENV` | Flask environment | No | production |
| `DEBUG` | Enable debug mode | No | False |
| `PORT` | Port number | No | 5000 |

## 🏗️ Project Structure

```
quzoo/
├── app1.py                 # Main Flask application
├── wsgi.py                 # WSGI entry point
├── config.py               # Configuration settings
├── models.py               # Database models
├── api_utils.py            # AI integration utilities
├── requirements.txt        # Python dependencies
├── Procfile               # Railway deployment config
├── railway.json           # Railway configuration
├── .env.example           # Environment variables template
├── templates/             # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── ai_quiz_generator.html
│   └── ...
├── static/               # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── img/
└── migrations/           # Database migrations
```

## 🎯 Usage Guide

### Creating an AI-Generated Quiz

1. **Login** as a professor/educator
2. **Navigate** to "AI Quiz Generator"
3. **Enter** the topic and number of questions
4. **Click** "Generate Quiz" - AI will create questions automatically
5. **Review** and edit questions if needed
6. **Save** and share the quiz code with students

### Taking a Quiz

1. **Register** as a student or login
2. **Enter** the quiz code provided by your instructor
3. **Complete** the quiz questions
4. **Submit** and view your results immediately

### Managing Results

1. **Access** the professor dashboard
2. **View** all quiz results and analytics
3. **Download** individual student reports
4. **Track** class performance over time

## 🔧 API Integration

The system integrates with Google's Gemini AI for intelligent question generation:

```python
from api_utils import generate_quiz_questions

# Generate 5 questions about Python programming
questions = generate_quiz_questions("Python Programming", 5)
```

## 🛠️ Development

### Adding New Features

1. **Database Changes**: Update `models.py` and create migrations
2. **Routes**: Add new routes in `app1.py`
3. **Templates**: Create HTML templates in `templates/`
4. **Styling**: Add CSS in `static/css/`

### Running Tests

```bash
# Test AI functionality
python test_ai.py

# Test API key management
python manage_keys.py
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/Shivam-Shukla0/quzoo/issues) page
2. Create a new issue with detailed information
3. Contact the maintainer

## 🙏 Acknowledgments

- **Google Gemini AI** for intelligent question generation
- **Flask** community for the excellent web framework
- **Railway** for seamless deployment platform
- **Contributors** who help improve this project

## 📊 Stats

- **Languages**: Python, HTML, CSS, JavaScript
- **Framework**: Flask
- **Database**: SQLite (development), PostgreSQL (production)
- **AI**: Google Gemini
- **Deployment**: Railway

---

Made with ❤️ by [Shivam Shukla](https://github.com/Shivam-Shukla0)

[![GitHub stars](https://img.shields.io/github/stars/Shivam-Shukla0/quzoo.svg)](https://github.com/Shivam-Shukla0/quzoo/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Shivam-Shukla0/quzoo.svg)](https://github.com/Shivam-Shukla0/quzoo/network)
[![GitHub issues](https://img.shields.io/github/issues/Shivam-Shukla0/quzoo.svg)](https://github.com/Shivam-Shukla0/quzoo/issues)
