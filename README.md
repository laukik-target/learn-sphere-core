# Learn-Sphere Backend

This is the backend for the Learn-Sphere project, built with Django and Django REST Framework. It provides APIs for user authentication, managing courses, and scheduling courses to be available at specified times.

## Prerequisites

- Python 3.x
- Git (for cloning the repository)
- Virtual environment package (optional but recommended)

## Setup Instructions

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone <repository_url>
cd learn-sphere-core
```

### Step 2: Create and Activate a Virtual Environment

It’s recommended to use a virtual environment to keep dependencies isolated.

1. **Create a virtual environment**:

   On Windows:
   ```bash
   python -m venv venv
   ```

   On macOS/Linux:
   ```bash
   python3 -m venv venv
   ```

2. **Activate the virtual environment**:

   On Windows:
   ```bash
   venv\Scripts\activate
   ```

   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

   When activated, you should see `(venv)` at the start of your command line.

### Step 3: Install Dependencies

With the virtual environment activated, install the required packages using `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Step 4: Set Up the Database

Run migrations to set up the initial database schema:

```bash
python manage.py migrate
```

### Step 5: Create a Superuser (Optional)

To access the Django admin panel, you can create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up a username, email, and password.

### Step 6: Run the Django Development Server

Start the Django development server to test the application locally:

```bash
python manage.py runserver
```

The server will start, and you can access it at `http://127.0.0.1:8000/`.

### API Endpoints

Here are some key endpoints for interacting with the backend:

- **Signup**: `POST /api/users/signup/`
- **Login**: `POST /api/users/login/`
- **Add Course** (Admin): `POST /api/courses/add/`
- **View Available Courses** (Student): `GET /api/courses/view/`

### Additional Notes

- Use the `Authorization` header with Basic Authentication when making requests to endpoints requiring authentication.
- Remember to activate the virtual environment each time you work on the project:

  - Windows: `venv\Scripts\activate`
  - macOS/Linux: `source venv/bin/activate`

- To deactivate the virtual environment, simply run:

  ```bash
  deactivate
  ```

### License

This project is licensed under the MIT License.
