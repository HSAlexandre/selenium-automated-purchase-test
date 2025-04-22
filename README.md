# 🛒 Automated Functional Test Purchase Flow with Selenium

This project demonstrates an automated **end-to-end purchase process** using **Python, Selenium and pytest**. It simulates a user navigating to an e-commerce site, accessing the shop, finding a product ("Blackberry"), adding it to the cart, selecting a country, and finalizing the purchase. This project uses **Page Object Model** design pattern.

---

## 🚀 Features

- Access [website](https://rahulshettyacademy.com/loginpagePractis/) and Sign in
- Navigate to the shop
- Search for a specific product ("Blackberry")
- Add product to cart and proceed to checkout
- Auto-select country (United Kingdom)
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
1. Go to **Login page**
2. Click on **Shop**
3. Find **Blackberry**
4. Click **Add to Cart**
5. Proceed to **Checkout**
6. Select **United Kingdom**
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

The script uses `pytest` to show test result terminal.

Example output:
```
============================= test session starts =============================
collecting ... collected 1 item

test_e2eFramework.py::test_e2e PASSED                                    [100%]

============================= 1 passed in 13.37s ==============================
```

---

## 📝 License
This project is for educational purposes.  
See the [LICENSE](LICENSE) file for more information.