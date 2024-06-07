import requests
from bs4 import BeautifulSoup
import nmap
import os

# Set the target URL and IP address
url = "https://yourtestwebsite.com"
ip_address = "192.168.1.100"

# Set the scan types (XSS, SQL injection, etc.)
scan_types = ["xss", "sql_injection"]

# Set the scan depth (number of pages to crawl)
scan_depth = 2

# Set the user agent for the requests
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

# Set the nmap scan options
nmap_scan_options = "-sV -sC -p 1-65535"

# Create a nmap object
nm = nmap.PortScanner()

# Perform the nmap scan
nm.scan(ip_address, arguments=nmap_scan_options)

# Parse the nmap results
for host in nm.all_hosts():
    for proto in nm[host].all_protocols():
        for port in nm[host][proto].keys():
            print(f"Port {port}/{proto} is open")

# Perform the web scan
for scan_type in scan_types:
    for page in range(1, scan_depth + 1):
        # Send a GET request to the URL
        response = requests.get(url, headers={"User-Agent": user_agent})

        # Parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all forms on the page
        forms = soup.find_all("form")

        # Iterate over the forms and check for vulnerabilities
        for form in forms:
            # Check for SQL injection
            if scan_type == "sql_injection":
                for input_field in form.find_all("input"):
                    if input_field.get("type") == "text":
                        # Send a POST request with the input field value
                        post_data = {"input_field_name": input_field.get("name"), "input_field_value": input_field.get("value")}
                        response = requests.post(url, data=post_data, headers={"User-Agent": user_agent})

                        # Check if the response contains any SQL injection vulnerabilities
                        if "SQL injection" in response.text:
                            print(f"SQL injection vulnerability found in {input_field.get('name')}")

            # Check for XSS
            if scan_type == "xss":
                for script_tag in soup.find_all("script"):
                    # Check if the script tag contains any XSS vulnerabilities
                    if "alert" in script_tag.text:
                        print(f"XSS vulnerability found in {script_tag.get('src')}")

# Save the scan results to a file
with open("scan_results.txt", "w") as f:
    f.write("Scan Results:\n")
    f.write(f"IP Address: {ip_address}\n")
    f.write(f"URL: {url}\n")
    f.write(f"Scan Types: {', '.join(scan_types)}\n")
    f.write(f"Scan Depth: {scan_depth}\n")
    f.write(f"Nmap Scan Options: {nmap_scan_options}\n")
    f.write("Vulnerabilities Found:\n")
    f.write("\n".join([f"{vulnerability}" for vulnerability in vulnerabilities]))