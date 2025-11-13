## ⚡ nea\_ETL: Nepal Electricity Authority Data Pipeline

A robust **Extract, Transform, Load (ETL)** pipeline designed to automate the process of gathering, cleaning, and structuring data related to the **Nepal Electricity Authority (NEA)** from various sources. This project aims to provide a reliable and consistent dataset for analysis, reporting, and dashboard creation.

***

## ✨ Features

* **Comprehensive Data Transformation:** Cleansing, validation, normalization, and aggregation routines to prepare the data for analytical use.
* **Flexible Data Loading:** Supports loading the structured data into various destinations, such as **PostgreSQL**, **MySQL**, or a data warehouse like Snowflake/BigQuery.
* **Logging and Error Handling:** Built-in logging to monitor the ETL process and mechanisms to handle common extraction or transformation failures.



***

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following installed on your system:

* **Python 3.x**
* **`pip`** (Python package installer)
* **Database access** (e.g., credentials for the target database)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/kirtanshrestha/nea_ETL.git](https://github.com/kirtanshrestha/nea_ETL.git)
    cd nea_ETL
    ```

2.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up Environment Variables:**
    Create a file named **`.env`** in the root directory and fill in your configuration details. This is typically used for sensitive information like database credentials and API keys.

    Example `.env` content:
    ```
    # Database Connection
    DB_HOST=localhost
    DB_NAME=nea_data
    DB_USER=etl_user
    DB_PASS=securepassword123
    
    # Optional: API Keys or other configurations
    # NEA_API_KEY=YOUR_API_KEY
    ```

***

## 💡 Usage

The main ETL process is executed via a single entry script (assuming `run_etl.py` is the main file).

### Running the Pipeline

Execute the following command to run the full Extract, Transform, and Load cycle:

```bash
python run_etl.py
```

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information.

***

## 📞 Contact

Kirtan Shrestha -- kirtanstha02@gmail.com

Project Link: [https://github.com/kirtanshrestha/nea\_ETL](https://github.com/kirtanshrestha/nea_ETL)