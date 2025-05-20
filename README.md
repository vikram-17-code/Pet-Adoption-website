# Pet Adoption Web Application

This is a Django-based web application for managing pet adoptions. It allows users to browse available pets, apply for adoption, and for staff to manage pets, adoptions, and breeds.

## Features

- User registration, login, and profile management
- Browse and search available pets by name, breed, age, size, and gender
- Detailed pet pages with health and adoption information
- Adoption application workflow with approval and pickup notifications
- Staff dashboard for managing pets, adoptions, and breeds
- Breed recommendation system based on user preferences
- Adoption statistics and report generation with charts

## Project Structure

```
.
├── manage.py
├── db.sqlite3
├── Pipfile / Pipfile.lock
├── images/
├── media/
├── static/
├── webpage/
│   ├── migrations/
│   ├── templates/
│   ├── forms.py
│   ├── models.py
│   ├── utils.py
│   ├── views.py
│   └── ...
└── ...
```

## Setup Instructions

1. **Clone the repository**  
   ```sh
   git clone <your-repo-url>
   cd pet_adopt
   ```

2. **Create and activate a virtual environment**  
   ```sh
   python -m venv virtuakenviron
   source virtuakenviron/bin/activate  # On Windows: virtuakenviron\Scripts\activate
   ```

3. **Install dependencies**  
   ```sh
   pip install -r requirements.txt
   # or if using Pipenv:
   pipenv install
   ```

4. **Apply migrations**  
   ```sh
   python manage.py migrate
   ```

5. **Create a superuser (for admin access)**  
   ```sh
   python manage.py createsuperuser
   ```

6. **Run the development server**  
   ```sh
   python manage.py runserver
   ```

7. **Access the application**  
   - Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Usage

- **Users** can register, log in, update their profile, browse/search pets, and apply for adoption.
- **Staff/Admin** can log in via the staff/admin login, manage pets, breeds, and adoptions, and generate reports.

## Customization

- Add pet and breed images to the `images/` or `media/` folder as needed.
- Update static files (CSS/JS) in the `static/` directory for custom styling.


## Screenshots
* Home page for users
![Screenshot 2025-05-20 230134](https://github.com/user-attachments/assets/ddf22133-b942-48ed-9122-651752d4ccc0)
* Home page with a display for dogs to adopt
![Screenshot 2025-05-20 230148](https://github.com/user-attachments/assets/1b2c3f2c-3c8a-418e-b849-223c9cb1f248)
* Pet Search page for searching pets suitable for our preference
![Screenshot 2025-05-20 230210](https://github.com/user-attachments/assets/825457b3-4fbd-415c-80c5-77c9c40d671d)
* Breed recommendation page for suggesting user what breed is suitable for them
![Screenshot 2025-05-20 230225](https://github.com/user-attachments/assets/a5312488-8fea-4887-8570-061213a1fa56)
* Login page for user
![Screenshot 2025-05-20 230225](https://github.com/user-attachments/assets/30a43d0a-6115-4b52-a22f-0b3fabba89e1)
* Login page for Staffs
![Screenshot 2025-05-20 230225](https://github.com/user-attachments/assets/7def7873-3a77-4f01-8dd7-5ca5198b1a60)
* Home page for staffs
![Screenshot 2025-05-20 230225](https://github.com/user-attachments/assets/26c9a3e1-7335-48b6-89c3-cc6b2b09def1)
* Report page
![Screenshot 2025-05-20 230225](https://github.com/user-attachments/assets/c7aa88ca-fd2e-4633-accc-21f459f7c9d2)
* Report page with charts for better visualization
![Screenshot 2025-05-20 230225](https://github.com/user-attachments/assets/95d134e0-25c8-4efa-b3d6-3145e95513cc)
