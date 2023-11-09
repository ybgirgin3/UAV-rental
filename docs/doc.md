## Getting Started

### Prerequisites

- Python (3.7+)
- Django (3.2+)
- Django Rest Framework
- djangorestframework-simplejwt
- Other dependencies mentioned in the `requirements.txt`

### Installation

1. Clone the repository:

```sh
git clone https://github.com/yourusername/your-django-api-project.git
```

1. Create a virtual environment (optional but recommended):

```sh
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

2.Install the required packages

```sh
pip install -r requirements.txt
```

3. Migrate the database

```sh
python manage.py migrate
```

4. Create a superuser

```sh
python manage.py createsuperuser
```

5. Start the development server

```sh
python manage.py runserver

```

The API should now be running locally at http://localhost:8000/.

## API Endpoints

- UAV: `/api/uav/`,
- Category: `/api/category/`,
- Reservation: `/api/reservation/`
- Register User: `/api/register/`
- Obtain Token: `/api/token/`
- Refresh Token: `/api/token/refresh/`
- Logout: `/api/logout/`
