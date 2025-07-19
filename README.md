
# 🚧 VERO Python Backend Task

This repository contains the solution to the technical assignment provided by VERO Digital Solutions. The project includes both a backend REST API (built with Django) and a client-side script for processing and converting data into an Excel file.

---


 Project Goal

1. Django REST API (Server)
   - Accepts a CSV file with vehicle information.
   - Fetches vehicle data from Baubuddy API.
   - Filters vehicles with valid `hu` (inspection date).
   - Resolves `labelIds` to their associated `colorCode`.
   - Returns a cleaned JSON response.

2. Client Script
   - Takes CLI parameters:
     - `-k/--keys` for additional columns (e.g., `kurzname`, `info`)
     - `-c/--colored` to enable row coloring by `hu` date
   - Sends the CSV to the backend API.
   - Processes JSON response.
   - Generates a styled Excel file using `openpyxl`.

---

## ⚙️ Technologies Used

- Python 3.x
- Django + Django REST Framework
- Pandas
- Requests
- Openpyxl

---

 Functional Requirements

- [ ] Upload CSV to a Django endpoint
- [ ] Fetch and merge data from `https://api.baubuddy.de`
- [ ] Resolve `labelIds` to color codes
- [ ] Filter vehicles missing `hu`
- [ ] Return structured JSON data
- [ ] Generate an Excel file with:
  - Dynamic columns from `--keys`
  - Colored rows based on `hu` date logic
  - Text color from `labelIds` if provided

---

How to Use

Coming soon – step-by-step setup & usage instructions will be added as the implementation progresses.

---

Timeline & Progress

- [ ] Repo created and initialized
- [ ] Django backend scaffolding
- [ ] API implementation with file upload
- [ ] Client script implementation
- [ ] Full integration and testing
