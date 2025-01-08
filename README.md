
![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)

# WhatsApp Chatbot 

A Django-based chatbot integrated with Google Dialogflow, deployed on Heroku, and connected to WhatsApp via the 360 Dialog WhatsApp Business API. This project enables seamless communication between users on WhatsApp and your Dialogflow-powered chatbot.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Deployment](#deployment)
- [Usage](#usage)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

## Features

- **WhatsApp Integration**: Communicate with users via WhatsApp using the 360 Dialog WhatsApp Business API.
- **Natural Language Processing**: Powered by Google Dialogflow, providing intelligent responses and intent recognition.
- **Persistent Conversations**: Store user interactions and conversations in a SQLite database.
- **Admin Interface**: Manage users and conversations via Django's admin panel.
- **Deployment**: Hosted on Heroku for scalable and reliable performance.
- **Logging**: Comprehensive logging to monitor chatbot activity and troubleshoot issues.

## Technologies Used

- **Backend Framework**: Django 5.1.4
- **Messaging API**: 360 Dialog WhatsApp Business API
- **Natural Language Processing**: Google Dialogflow
- **Deployment Platform**: Heroku
- **Database**: SQLite3
- **Version Control**: Git
- **Language**: Python 3.13.1

## Prerequisites

Before getting started, ensure you have met the following requirements:

- Python 3.7 or higher installed
- Git installed
- A Heroku account
- A 360 Dialog account with WhatsApp Business API access
- Google Cloud account with Dialogflow enabled
- Knowledge of Django framework

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/whatsapp_chatbot.git
   cd whatsapp_chatbot
   ```
2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

### Set Up Google Cloud Credentials

1. **Download Credentials.json**: Obtain your `Credentials.json` file from your Google Cloud service account.
2. **Place the File**: Add the `Credentials.json` file to the project directory.
3. **Set Environment Variable**:

   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS='path/to/Credentials.json'
   ```

### Configure 360 Dialog WhatsApp API

1. **Sign Up**: Register for an account with 360 Dialog.
2. **Obtain API Credentials**: Acquire `API_URL`, `API_KEY`, and `PHONE_NUMBER_ID` from the 360 Dialog dashboard.

### Update Django Settings

Modify `settings.py` to include your API credentials and other configurations.

```python
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv('SECRET_KEY', 'your-default-secret-key')
DEBUG = False
ALLOWED_HOSTS = ['your-heroku-app.herokuapp.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'chatbot',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# WhatsApp API Settings
WHATSAPP_API_URL = os.getenv('WHATSAPP_API_URL')
WHATSAPP_API_KEY = os.getenv('WHATSAPP_API_KEY')
PHONE_NUMBER_ID = os.getenv('PHONE_NUMBER_ID')
PROJECT_ID = 'handy-muse-339007'
```

### Set Environment Variables

#### Local Setup:

```bash
export WHATSAPP_API_URL='https://waba.360dialog.com/v1/messages'
export WHATSAPP_API_KEY='your_360dialog_api_key'
export PHONE_NUMBER_ID='your_phone_number_id'
export SECRET_KEY='your_django_secret_key'
```

#### Heroku Setup:

```bash
heroku config:set WHATSAPP_API_URL=https://waba.360dialog.com/v1/messages
heroku config:set WHATSAPP_API_KEY=your_360dialog_api_key
heroku config:set PHONE_NUMBER_ID=your_phone_number_id
heroku config:set SECRET_KEY=your_django_secret_key
```

## Deployment

1. **Install Heroku CLI**: Download and install the Heroku CLI.
2. **Login to Heroku**:

   ```bash
   heroku login
   ```

3. **Create a New Heroku App**:

   ```bash
   heroku create your-app-name
   ```

4. **Set Environment Variables on Heroku**:

   ```bash
   heroku config:set GOOGLE_APPLICATION_CREDENTIALS=Credentials.json
   heroku config:set WHATSAPP_API_URL=https://waba.360dialog.com/v1/messages
   heroku config:set WHATSAPP_API_KEY=your_360dialog_api_key
   heroku config:set PHONE_NUMBER_ID=your_phone_number_id
   heroku config:set SECRET_KEY=your_django_secret_key
   ```

5. **Deploy to Heroku**:

   ```bash
   git add .
   git commit -m "Deploying to Heroku"
   git push heroku main
   ```

6. **Run Migrations**:

   ```bash
   heroku run python manage.py migrate
   ```

## Usage

1. **Send a Message**: Send a WhatsApp message to your registered business number.
2. **Chatbot Response**: The chatbot processes your message via Dialogflow and responds accordingly.
3. **Admin Interface**: Access Django's admin panel at `https://your-app-name.herokuapp.com/admin/`.

## License

This project is licensed under the Apache License 2.0. See the LICENSE file for details.

## Contributing

Contributions are welcome!

1. **Fork the Repository**
2. **Create a New Branch**:

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes**:

   ```bash
   git commit -m "Add some feature"
   ```

4. **Push to the Branch**:

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**

## Contact

For any inquiries or support, please contact Chetas Parekh @chetas1208.
