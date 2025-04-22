# 🛒 Automated Functional Test Purchase Flow with Selenium

This project demonstrates an automated **end-to-end purchase process** using **Python, Selenium and pytest**.

It simulates a user navigating to an e-commerce site, accessing the shop, finding a product (You can add a product in test_e2eFramework.json file), adding it to the cart, selecting a country (You can add a country in test_e2eFramework.json file), and finalizing the purchase.

This project uses **Page Object Model** design pattern.

---

## 🚀 Features

- Access [website](https://rahulshettyacademy.com/loginpagePractis/) and Sign in
- Navigate to the shop
- Search for a specific product ("Blackberry" and "Nokia Edge) - by default, but you can change it
- Add product to cart and proceed to checkout
- Auto-select country ("United Kingdom" and "Bangladesh) - by default, but you can change it
- Agree to terms & conditions and complete the purchase
- Verify success message

---

## 🧰 Tech Stack

- Python 3.x
- [Selenium](https://pypi.org/project/selenium/)
- Pytest
- [WebDriver Manager](https://pypi.org/project/webdriver-manager/)
- ChromeDriver
- GeckoDriver
- EdgeDriver

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/HSAlexandre/selenium-automated-purchase-test.git
cd selenium-automated-purchase-test
```

2. Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```
3. Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

This is a simplified version of the flow being automated:

Run the script:

```bash
pytest test_e2eFramework --browser_name chrome -v -s
OR
pytest test_e2eFramework --browser_name firefox -v -s
OR
pytest test_e2eFramework --browser_name edge -v -s
```

The script will:

Scenario 1:
1. Go to **Login page**
2. Click on **Shop**
3. Find **Blackberry**
4. Click **Add to Cart**
5. Proceed to **Checkout**
6. Select **United Kingdom**
7. Submit the order ✅

Scenario 2:
1. Go to **Login page**
2. Click on **Shop**
3. Find **Nokia Edge**
4. Click **Add to Cart**
5. Proceed to **Checkout**
6. Select **Bangladesh**
7. Submit the order ✅

---

## 📝 Requirements
- Ensure Google Chrome is installed and up-to-date.
- This script uses a temporary user profile to avoid session issues.
- Change the URL or product name if the website changes.
- If you're using a custom Chrome profile, you can update the path in `main.py` with:

```python
user_data_dir = r'C:\Users\your_user\AppData\Local\Google\Chrome\User Data'
```

## 🧪 Pytest Output

The script uses `pytest` and `allure` to show test results.

For allure report generation, run:

```
pytest .\test_e2eFramework.py --alluredir=..\reports

```

And then:

```
allure generate ..\reports -o ..\reports\allure-report --clean
```

HTML report will be generated for test result visualization

Example output in terminal:
```
============================================================ test session starts ========================================
platform win32 -- Python 3.10.0, pytest-8.3.5, pluggy-1.5.0
rootdir: C:\Users\<user>\PycharmProjects\selenium-automated-purchase-test\tests
plugins: allure-pytest-2.14.0, html-4.1.1, metadata-3.1.1
collected 2 items                                                                                                                                                                                                                   

test_e2eFramework.py
DevTools listening on ws:/devtools/browser/dd9cf6e8-5123-4f20-9045-6afdf1d27d9c
.
DevTools listening on ws:/devtools/browser/bdb3dbc1-da2d-4619-9345-896a3bbedb9a
.                                                                                                                                                                                                      [100%]
=========================================================== 2 passed in 28.17s ==========================================
```

---

## 📝 License
This project is for educational purposes.  
See the [LICENSE](LICENSE) file for more information.