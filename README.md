# 🛒 Automated Functional Test Purchase Flow with Selenium

This project demonstrates an automated **end-to-end purchase process** using Python and Selenium. It simulates a user navigating to an e-commerce site, accessing the shop, finding a product ("Blackberry"), adding it to the cart, selecting a country, and finalizing the purchase.

---

## 🚀 Features

- Access website and navigate to the shop [test website](https://rahulshettyacademy.com/angularpractice/)
- Search for a specific product ("Blackberry")
- Add product to cart and proceed to checkout
- Auto-select country (United Kingdom)
- Agree to terms & conditions and complete the purchase
- Verify success message

---

## 🧰 Tech Stack

- Python 3.x
- [Selenium](https://pypi.org/project/selenium/)
- [WebDriver Manager](https://pypi.org/project/webdriver-manager/)
- ChromeDriver

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
python main.py
```

The script will:
1. Go to homepage
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

## 🧪 Test Output

The script uses `logging` to show step-by-step progress in the terminal.

Example output:
```
2025-04-21 20:25:25,142 INFO Initializing Webdriver
2025-04-21 20:25:31,202 INFO Blackberry found
2025-04-21 20:25:31,348 INFO Checkout confirmed
2025-04-21 20:25:36,480 INFO UK country selected
2025-04-21 20:25:36,572 INFO Completing purchase
2025-04-21 20:25:36,589 INFO PASS: Purchase confirmed
2025-04-21 20:25:36,589 INFO ALL TESTS PASSED!
2025-04-21 20:25:36,589 INFO Closing browser
```

---

## 📝 License
This project is for educational purposes.  
See the [LICENSE](LICENSE) file for more information.