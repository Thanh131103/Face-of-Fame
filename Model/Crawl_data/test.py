from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome webdriver
wd = webdriver.Chrome()

# Load the page containing the image thumbnails
wd.get('https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q=serenawilliam&oq=serenawilliam&gs_l=img')

# Wait for the thumbnails to be present
thumbnails_present = WebDriverWait(wd, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img.YQ4gaf"))
)

print("Number of thumbnails found:", len(thumbnails_present))

# Loop through the thumbnail results
for thumbnail in thumbnails_present:
    # Get the image source URL
    image_src = thumbnail.get_attribute('src')
    print("Image Source URL:", image_src)
