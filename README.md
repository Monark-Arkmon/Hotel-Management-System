# Hotel Management System

## 🏨 Project Overview
The **Hotel Management System** is a Python-based console application for managing hotel operations, including room booking, restaurant orders, payments, and record management. It leverages **MySQL** for efficient data storage and retrieval.

---

## Features
- **Room Booking**: Reserve rooms with customer details and duration.
- **Room Information**: Display details and prices of available rooms.
- **Menu Orders**: Order food items from the hotel's menu.
- **Payments**: Process customer payments and generate receipts.
- **Record Management**: Export booking records to CSV files.
- **Booking Cancellation**: Handle cancellations with dynamic refund policies.
- **Search**: Find bookings using Customer ID or Aadhaar Number.

---

## Requirements
### Software Requirements
1. **Python 3.x**
2. **MySQL** Server
3. Python Libraries:
   - `mysql-connector-python`
   - `datetime`, `csv`, `os` (part of Python's standard library)

Install dependencies with:
```bash
pip install mysql-connector-python
```

---

## Setup Instructions
### 1. Clone the Repository
Download or clone the project folder:
```bash
git clone git@github.com:Monark-Arkmon/Hotel-Management-System.git
```

### 2. Set Up MySQL
- Start the MySQL server.
- Ensure a MySQL user with:
  - **Username**: `root`
  - **Password**: `amity`
- Update credentials in the code if necessary.

### 3. Database Creation
The application automatically creates the required database (`hotel`) and table (`booking`) during the first run.

### 4. Run the Application
Navigate to the project directory and execute:
```bash
python Project.py
```

---

## File Structure
```
hotel_management/
├── Project.py         # Main script of the application
```

---

## Usage
1. Launch the application by running `Project.py`.
2. Use the interactive menu to:
   - Book rooms.
   - View room details.
   - Place restaurant orders.
   - Process payments.
   - Search and manage records.
3. Exported booking records are available as CSV files in the project directory.

---

## Admin Notes
- Default admin password for accessing records: **0**.
- Cancellation refund policy:
  - **10+ days before check-in**: 80% refund.
  - **5-10 days before check-in**: 50% refund.
  - **1-5 days before check-in**: No refund.

---

## Example Menu
```text
1  - Room Booking
2  - Room Information
3  - Menu Card
4  - Payment
5  - View Records
6  - Cancel Booking
7  - Search Booking
0  - Exit
```

---

## 📌 Additional Notes
- This project can be extended with a graphical interface or additional features.
- To contribute or report issues, feel free to open a pull request or create an issue in the repository.
