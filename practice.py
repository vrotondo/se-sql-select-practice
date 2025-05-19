import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

product_data = pd.read_sql("""
SELECT *
  FROM products;
""", conn)

print(product_data)

# Step 1
product_names_and_codes = pd.read_sql("""
SELECT productName, productCode
  FROM products;
""", conn).tail()

print(product_names_and_codes)

# Step 2
product_codes_and_names = pd.read_sql("""
SELECT productCode, productName
  FROM products;
""", conn).tail()

print(product_codes_and_names)

# Step 3
products_by_line = pd.read_sql("""
SELECT productName, productLine,
       CASE
       WHEN productLine = "Planes" THEN "Planes"
       ELSE "Not Planes"
       END AS Planes
  FROM products;
""", conn)

print(products_by_line)

# Step 4
product_description_lengths = pd.read_sql("""
SELECT length(productDescription) AS description_length
  FROM products;
""", conn).head()

print(product_description_lengths)

# Step 5
product_upper_vendors = pd.read_sql("""
SELECT upper(productVendor) AS caps_vendor
  FROM products;
""", conn).head()

print(product_upper_vendors)

# Step 6
product_names_lower = pd.read_sql("""
SELECT lower(productName) AS lower_name
  FROM products;
""", conn).head()


print(product_names_lower)

# Step 7
product_scales = pd.read_sql("""
SELECT substr(productScale, 3,3) AS non
  FROM products;
""", conn)

print(product_scales)

# Step 8
products_with_vendors = pd.read_sql("""
SELECT productVendor || " " || productName AS fullName
  FROM products;
""", conn)

print(products_with_vendors)

# Step 9
rounded_price_diffs = pd.read_sql("""
SELECT CAST(round(MSRP - buyPrice) AS INTEGER) AS round_diff
  FROM products;
""", conn)

print(rounded_price_diffs)

# Step 10
conn.close()