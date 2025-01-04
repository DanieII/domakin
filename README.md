# Domakin

Domakin is a web application designed to encourage family members to complete daily tasks. Built with Django, HTMX, and TailwindCSS, Domakin allows users to create an account, form a family group, invite family members, and manage tasks collaboratively.

## Features

- **User Accounts**: Create an account to start using Domakin. (Google authentication supported)
- **Family Groups**: Form a family group and invite members using invitation links.
- **Task Management**: Add and manage tasks within your family group.
- **Task Completion**: Family members can mark tasks as completed.
- **Weekly Resets**: Tasks reset at the end of each week, and the member with the most completed tasks is rewarded with a win.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTMX, TailwindCSS, HTML, JavaScript

## Installation

To run this project locally using Docker, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/DanieII/domakin.git
    cd domakin
    ```

3. **Run the application using Docker Compose**:
    ```bash
    docker-compose up --build
    ```

4. **Run database migrations**:
    ```bash
    docker compose exec web python manage.py migrate
    ```

5. **Create a superuser** (optional, for admin access):
    ```bash
    docker compose exec web python manage.py createsuperuser
    ```

6. **Open your browser and navigate to**:
    ```
    http://localhost:8000
    ```

## Prerequisites

Ensure you have the following installed:
- Docker
- Docker Compose

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
