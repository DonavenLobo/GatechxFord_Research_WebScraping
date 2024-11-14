import pandas as pd
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def setup_driver():
    """Set up and return the Selenium WebDriver with Bright Data proxy"""
    AUTH = 'brd-customer-hl_c1465306-zone-scraping_browser1:mu4m1g5prq30'
    SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'
    
    print('Connecting to Scraping Browser...')
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    driver = Remote(sbr_connection, options=ChromeOptions())
    print('Connected!')
    return driver

def scrape_carfax_listings(model, year_range):
    """
    Scrape CarFax listings for a specific model and year range
    Returns a pandas DataFrame with the results
    """
    driver = setup_driver()
    
    # Initialize empty DataFrame with desired columns
    df = pd.DataFrame(columns=[
        'year', 'make', 'model', 'trim', 'price', 'mileage',
        'location', 'dealer', 'vin', 'url'
    ])
    
    try:
        for year in year_range:
            url = f"https://www.carfax.com/cars-for-sale?make=Ford&model={model}&year={year}"
            print(f"Scraping {year} {model}...")
            
            driver.get(url)
            time.sleep(5)  # Allow page to load
            
            # Find all listing elements
            listings = driver.find_elements(By.CLASS_NAME, "listing-card")
            
            for listing in listings:
                try:
                    # Extract data from each listing
                    data = {
                        'year': year,
                        'make': 'Ford',
                        'model': model,
                        'trim': listing.find_element(By.CLASS_NAME, "trim").text,
                        'price': listing.find_element(By.CLASS_NAME, "price").text,
                        'mileage': listing.find_element(By.CLASS_NAME, "mileage").text,
                        'location': listing.find_element(By.CLASS_NAME, "location").text,
                        'dealer': listing.find_element(By.CLASS_NAME, "dealer-name").text,
                        'vin': listing.find_element(By.CLASS_NAME, "vin").text,
                        'url': listing.find_element(By.TAG_NAME, "a").get_attribute("href")
                    }
                    
                    # Append row to DataFrame
                    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
                    
                except Exception as e:
                    print(f"Error scraping listing: {e}")
                    continue
            
            print(f"Completed {year} {model} - Found {len(df)} listings so far")
            
    except Exception as e:
        print(f"Error during scraping: {e}")
    
    finally:
        driver.quit()
    
    return df

def main():
    # Define models and years to scrape
    models = ['Mustang-Mach-E', 'Edge']
    years = range(2021, 2025)
    
    # Initialize empty DataFrame for all results
    all_results = pd.DataFrame()
    
    # Scrape each model
    for model in models:
        print(f"\nStarting scrape for {model}")
        model_df = scrape_carfax_listings(model, years)
        all_results = pd.concat([all_results, model_df], ignore_index=True)
        
        # Save intermediate results
        model_df.to_csv(f'data/carfax_{model.lower()}_listings.csv', index=False)
        print(f"Saved {len(model_df)} listings for {model}")
    
    # Save all results
    all_results.to_csv('data/carfax_all_listings.csv', index=False)
    print(f"\nCompleted scraping. Total listings found: {len(all_results)}")
    
    return all_results

if __name__ == '__main__':
    main()
