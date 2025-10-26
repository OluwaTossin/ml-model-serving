# ML Model Serving API

[![CI/CD Pipeline](https://github.com/OluwaTossin/ml-model-serving/actions/workflows/deploy.yml/badge.svg)](https://github.com/OluwaTossin/ml-model-serving/actions/workflows/deploy.yml)
[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-green.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A production-ready Flask API for serving machine learning models with automated CI/CD deployment to AWS EC2.

## 🚀 Features

- **RESTful API**: Simple and intuitive endpoints for model predictions
- **Production Ready**: Configured for production deployment with proper error handling
- **Automated Deployment**: CI/CD pipeline with GitHub Actions
- **AWS Integration**: Seamless deployment to EC2 instances
- **Model Agnostic**: Works with any scikit-learn compatible model
- **JSON API**: Standard JSON request/response format

## 📋 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Configuration](#configuration)
- [Deployment](#deployment)
- [Development](#development)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## 🛠️ Installation

### Prerequisites

- Python 3.7+
- pip package manager
- Git

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/OluwaTossin/ml-model-serving.git
   cd ml-model-serving
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure model file exists**
   - Place your trained model file as `model.pkl` in the root directory
   - The model should be saved using `joblib.dump()`

## 🚀 Usage

### Starting the Server

```bash
python app.py
```

The server will start on `http://localhost:5000` by default.

### Making Predictions

Send a POST request to the `/predict` endpoint:

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [1.0, 2.0, 3.0, 4.0]}'
```

## 📡 API Endpoints

### `GET /`
**Description**: Health check endpoint

**Response**:
```json
"Hello, World!"
```

### `POST /predict`
**Description**: Make predictions using the loaded ML model

**Request Body**:
```json
{
  "features": [1.0, 2.0, 3.0, 4.0]
}
```

**Response**:
```json
{
  "prediction": [0.85]
}
```

**Error Response**:
```json
{
  "error": "Error description"
}
```

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `FLASK_ENV` | Flask environment | `production` |
| `PORT` | Server port | `5000` |
| `HOST` | Server host | `0.0.0.0` |

### Model Requirements

- Model must be serialized using `joblib`
- Model should implement the scikit-learn estimator interface
- File should be named `model.pkl` and placed in the root directory

## 🚀 Deployment

### AWS EC2 Deployment

This project includes automated deployment to AWS EC2 using GitHub Actions.

#### Prerequisites

1. **AWS Account** with EC2 instance
2. **GitHub Secrets** configured:
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `AWS_REGION`
   - `SSH_PRIVATE_KEY`

#### Deployment Process

The deployment is triggered automatically on push to the `main` branch:

1. Code is checked out
2. Dependencies are installed
3. AWS CLI is configured
4. Application is deployed to EC2
5. Service is restarted

#### Manual Deployment

```bash
# SSH into your EC2 instance
ssh -i your-key.pem ec2-user@your-ec2-ip

# Clone/update the repository
git clone https://github.com/OluwaTossin/ml-model-serving.git
cd ml-model-serving

# Install dependencies
pip3 install -r requirements.txt

# Start the application
nohup python3 app.py &
```

## 💻 Development

### Project Structure

```
ml-model-serving/
├── app.py              # Main Flask application
├── model.pkl           # Trained ML model (joblib format)
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
├── .gitignore         # Git ignore rules
└── .github/
    └── workflows/
        └── deploy.yml  # CI/CD pipeline
```

### Adding New Features

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings for functions and classes
- Include error handling

## 🧪 Testing

### Running Tests Locally

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests
pytest

# Run with coverage
pytest --cov=app
```

### Testing the API

```bash
# Test health endpoint
curl http://localhost:5000/

# Test prediction endpoint
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [1, 2, 3, 4]}'
```

## 📦 Dependencies

- **Flask**: Web framework for the API
- **joblib**: Model serialization/deserialization
- **numpy**: Numerical computations
- **pandas**: Data manipulation
- **scikit-learn**: Machine learning utilities

## 🔧 Troubleshooting

### Common Issues

1. **Model Loading Error**
   - Ensure `model.pkl` exists in the root directory
   - Verify the model was saved using `joblib.dump()`

2. **Import Errors**
   - Install all dependencies: `pip install -r requirements.txt`
   - Check Python version compatibility

3. **Port Already in Use**
   - Change the port in `app.py` or kill the process using port 5000

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) and ensure your PR follows our guidelines.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **OluwaTossin** - *Initial work* - [OluwaTossin](https://github.com/OluwaTossin)

## 🙏 Acknowledgments

- Flask community for the excellent web framework
- scikit-learn team for machine learning utilities
- AWS for reliable cloud infrastructure

## 📞 Support

If you have any questions or run into issues, please:

1. Check the [Issues](https://github.com/OluwaTossin/ml-model-serving/issues) page
2. Create a new issue if your problem isn't already reported
3. Provide detailed information about your environment and the issue

---

**Happy Coding!** 🎉