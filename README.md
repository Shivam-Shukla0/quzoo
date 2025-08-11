# Quiz Management System with AI Generator

A comprehensive Flask-based quiz management system featuring an AI-powered quiz generator using Google's Gemini API.

## Features

### Core Features
- 👨‍🏫 **Professor Dashboard**: Create, edit, and manage quizzes
- 👨‍🎓 **Student Dashboard**: Take quizzes and view results
- 📊 **Results & Analytics**: Detailed quiz results and performance tracking
- 🔐 **User Authentication**: Secure login system with role-based access
- ⏱️ **Timed Quizzes**: Configurable time limits for quizzes
- 🎯 **Scoring System**: Customizable marking schemes

### AI-Powered Features
- 🤖 **AI Quiz Generator**: Generate high-quality multiple-choice questions on any topic
- 🔄 **Smart API Key Rotation**: Automatic rotation of multiple Gemini API keys
- ✅ **Question Validation**: Ensures generated questions meet quality standards
- 🎨 **Topic Flexibility**: Generate quizzes on any subject matter

## Installation

### Prerequisites
- Python 3.8+
- Git

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/quiz-management-system.git
   cd quiz-management-system
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Keys**
   ```bash
   cp api_keys.json.example api_keys.json
   ```
   Edit `api_keys.json` and add your Google Gemini API keys:
   ```json
   {
     "keys": [
       "your-gemini-api-key-1",
       "your-gemini-api-key-2"
     ],
     "key_status": {
       "your-gemini-api-key-1": {
         "is_active": true,
         "last_used": "Never",
         "usage_count": 0
       }
     }
   }
   ```

5. **Set up the database**
   ```bash
   python app1.py
   ```
   The database will be created automatically on first run.

6. **Run the application**
   ```bash
   python app1.py
   ```
   Access the application at `http://127.0.0.1:5100`

## Getting Gemini API Keys

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Add multiple keys for better quota management
4. Add them to your `api_keys.json` file

## Usage

### For Professors
1. Register as a professor
2. Create quizzes manually or use the AI generator
3. Share quiz access codes with students
4. Monitor results and analytics

### For Students
1. Register as a student
2. Enter quiz access codes to take quizzes
3. View your results and performance

### AI Quiz Generator
1. Navigate to "AI Quiz Generator" in the professor dashboard
2. Enter a topic (e.g., "Python Programming", "World History")
3. Select number of questions (5, 10, or 15)
4. Review generated questions and select which to include
5. Configure quiz settings and create

## API Key Management

The system includes intelligent API key rotation:

```bash
# Check key status
python manage_keys.py --status

# Reactivate all keys (useful when quotas reset)
python manage_keys.py --reactivate

# Test AI generation
python test_ai.py
```

## Project Structure

```
quiz-management-system/
├── app1.py                 # Main Flask application
├── api_utils.py           # AI generation and API key management
├── models.py              # Database models
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── manage_keys.py         # API key management utility
├── test_ai.py            # AI functionality test script
├── templates/            # HTML templates
├── static/              # CSS, JS, images
├── migrations/          # Database migrations
└── README.md           # This file
```

## Configuration

### Environment Variables
- `SECRET_KEY`: Flask secret key (optional, defaults to a secure key)
- `GEMINI_API_KEY`: Primary Gemini API key (optional if using api_keys.json)
- `DATABASE_URL`: Database URL (optional, defaults to SQLite)

### Database
The system uses SQLite by default for easy setup. For production, configure PostgreSQL or MySQL in `config.py`.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Troubleshooting

### Common Issues

1. **"No active API keys available"**
   - Check that your `api_keys.json` file contains valid Gemini API keys
   - Ensure keys are marked as `"is_active": true`
   - Run `python manage_keys.py --status` to check key status

2. **Database errors**
   - Delete `app.db` and restart the application to recreate the database
   - Check that you have write permissions in the project directory

3. **Import errors**
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Activate your virtual environment

### Getting Help

- Check the [Issues](https://github.com/yourusername/quiz-management-system/issues) page
- Create a new issue with detailed error messages and steps to reproduce

## Features in Detail

### AI Quiz Generator
- Uses Google's Gemini 1.5 Flash model for question generation
- Supports any topic or subject matter
- Generates diverse question types and difficulty levels
- Validates question format and correctness
- Allows manual review and selection of questions

### API Key Rotation
- Automatically cycles through multiple API keys
- Tracks usage statistics for each key
- Deactivates keys when quota limits are reached
- Easy reactivation for daily quota resets

### User Management
- Role-based access (Professor/Student)
- Secure password hashing
- Session management
- User registration and authentication

### Quiz Features
- Multiple choice questions (4 options each)
- Customizable time limits
- Positive and negative marking
- Access code protection
- Question shuffling
- Automatic scoring

## Recent Updates

- ✅ Fixed AI quiz generator functionality
- ✅ Implemented robust API key rotation system
- ✅ Enhanced error handling and user feedback
- ✅ Improved question validation and parsing
- ✅ Added comprehensive testing utilities
- ✅ Enhanced user interface with better UX