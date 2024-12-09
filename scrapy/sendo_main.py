import time
import json
from sendo_session import fetch_product_links
from sendo_extractor import fetch_product_details

# URL of the main page
url = 'https://www.sendo.vn/cong-nghe?'

# List to store scraped product data
product_data = []

# Fetch product links
product_urls = fetch_product_links(url)  # Renamed to clarify it's a list of URLs

# Process individual products
for index, product_url in enumerate(product_urls[:3]):  # Limit to 1 for testing
    try:
        # Ensure the URL starts with "http"
        if not product_url.startswith("http"):
            product_url = f"https://www.sendo.vn{product_url}"

        print(f"\nFetching product {index + 1}: {product_url}")
        product_details = fetch_product_details(product_url)
        product_data.append(product_details)

        # Print product details for debugging
        print(product_details)
        time.sleep(2)  # Avoid overloading the server
    except Exception as e:
        print(f"Error processing product {index + 1}: {e}")

# Save the data to a JavaScript file
js_file_path = "product_data.js"
with open(js_file_path, "w", encoding="utf-8") as js_file:
    js_file.write("const productData = ")
    json.dump(product_data, js_file, ensure_ascii=False, indent=4)
    js_file.write(";")  # End JavaScript variable definition

print(f"Data saved successfully to {js_file_path}")