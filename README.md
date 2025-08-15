
```markdown
# 🕵️‍♀️ Job Scraper Platform

A complete Django-based job scraping platform that collects job postings from [RemoteOK](https://remoteok.com/), stores them in a database, and makes them accessible via API, CSV export, and a professional web interface.

---

## 🚀 Features

- **Idempotent Scraper** — Avoids duplicate entries using `(link, source)` uniqueness.
- **Filterable API** — Search by title, company, location, or source.
- **CSV Export** — Download job data with the same filters as the API.
- **Professional UI** — Responsive, minimal job listings page powered by HTML, CSS, and JavaScript.
- **Django Admin** — Manage and view jobs with built-in filters and search.
- **Pagination Support** — API and UI both support page and page size parameters.

---

## 📂 Project Structure

```

jobscrapper/
│
├── jobs/
│   ├── admin.py          # Django Admin registration
│   ├── models.py         # Job model with uniqueness constraints
│   ├── scraper.py        # RemoteOK scraper (update\_or\_create logic)
│   ├── views.py          # API, CSV, and UI endpoints
│   ├── urls.py           # App-level URL configuration
│   └── templates/
│       └── jobs\_list.html  # Responsive frontend template
│
├── jobscrapper/
│   ├── urls.py           # Project-level URL routing
│   └── settings.py       # Django settings
└── manage.py

````



## 🌐 API Endpoints

| Endpoint        | Method | Description                                                    |
| --------------- | ------ | -------------------------------------------------------------- |
| `/api/jobs/`    | GET    | JSON API with filtering: `q`, `location`, `source`, pagination |
| `/api/jobs.csv` | GET    | CSV export with same filtering as `/api/jobs/`                 |
| `/jobs/`        | GET    | Web UI for job search, filter, and export                      |

**Example:**

```bash
GET /api/jobs/?q=python&location=remote&page=1&page_size=10
```

---




## 🧠 Learning Outcomes

* Enforcing uniqueness in Django models using `UniqueConstraint`
* Building an idempotent scraper with `update_or_create()`
* Creating REST-like endpoints without Django REST Framework
* Implementing CSV export in Django
* Designing a minimal, responsive frontend for API data

---

## 👩‍💻 Tech Stack

* **Backend:** Django
* **Frontend:** HTML, CSS, JavaScript
* **Database:** SQLite (default, can be swapped with PostgreSQL/MySQL)
* **Scraping:** BeautifulSoup, Requests

---


