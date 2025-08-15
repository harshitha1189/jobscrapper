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



## 🌐 API Endpoints

| Endpoint        | Method | Description                                                    |
| --------------- | ------ | -------------------------------------------------------------- |
| `/api/jobs/`    | GET    | JSON API with filtering: `q`, `location`, `source`, pagination |
| `/api/jobs.csv` | GET    | CSV export with same filtering as `/api/jobs/`                 |
| `/jobs/`        | GET    | Web UI for job search, filter, and export                      |

👩‍💻 Tech Stack

Backend: Django
Frontend: HTML, CSS, JavaScript
Database: SQLite (default, can be swapped with PostgreSQL/MySQL)
Scraping: BeautifulSoup, Requests
