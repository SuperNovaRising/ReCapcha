# Chrome Driver: https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/119.0.6045.105/mac-x64/chromedriver-mac-x64.zip

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the web driver (in this case, Chrome)
driver = webdriver.Chrome()

# Navigate to a webpage
driver.get('https://www.google.com/recaptcha/api/fallback?k=6LdAvUIUAAAAAHjrjmjtNTcXyKm0WKwefLp-dQv9')

# Find Caption Text
caption_text = driver.find_element(By.CLASS_NAME, 'fbc-imageselect-message-without-candidate-image').text
#caption_text = driver.find_element(By.CLASS_NAME, 'rc-imageselect-instructions').text

print(caption_text)

captcha_image = driver.find_element(By.CLASS_NAME, 'fbc-imageselect-payload').get_attribute('src')
# captcha_image = driver.find_element(By.CLASS_NAME, 'rc-image-tile-33').get_attribute('src')

print(captcha_image)

# Split image into individual images
# input into langchain to match again caption_text
# automate checkbox selection and submit form


time.sleep(2)

from PIL import Image
import requests
# Open the original image
# https://www.google.com/recaptcha/api2/payload?c=03AFcWeA7HuqHsAZlvSjs0B-VNmP-FoTak4rOkHfGMpXusMLV5RBJ1c11xY61HNYbQGQ91-0IfbaNTmZ0iKGVXnMIvTH1hO0SUYnpcJAYryF4ho-8juIi7ntUl811-Hq3Zjw5nPyskZd_20UeC5YgWoPM6Rs6580QbaBRmIB7tssjLZ0FxDFuJ-Zvpf5XMuz7DF7wOeN64JtxOoNyKF56i8iHZtPEWsBHkCA8NQGZvmQxiVcYuZwVtNUS7t7bLny3GaNyBzZhgWSgUnVpvxKuuYP1tPIqpbZgBbz9No26YKdqkoHeiFRk_56JOaM0p2DczA6jEq3K-nzpXvYss9Ax2ooVHjrv8PalwV6co4JN-jQc0b0VtZg5vne8id7lLfUXSdvG6QgN61PbpSXAsT6UnmjIyEk5RuJSmjnuwQc-NVlHf9Pm2kEpU4YUgbQp-mw3ZWWvomF-Osn2mofJzdt-KJKbhgUc87x4ZlKDgrsGaPSgPKBYZS5jSUDN7MfEqf1IWiBjzDjaUlBiFiIXOXXE3kvz9f_AuesG3huNPYwH8a_qcT4qVBvyTe85KJQSMqkhg_ICNjw9wj61VQ059-cLDqGErdzYsjXfu-0YcE1Csd5EY0PVLeelaYgPjncpxt6Vsb6UIKmGFD9_dKcYZQ6HMnXj7_T4tRom_cFbbj-vIJs4mTlseb5FlIMraqx6O5VVW2Yprnn6ifgQ-AIIMMKyB0yy02dln-9r19SH3QJEl6faoLn6_FYfxeeJ33kgxFcqDwSfF1joxBYQbg_K4WlXWC2pqZhYEUk-J9DZQXfyj7spYMX0qOqBGeCB93ut8kr6SizZ8wivKIiRGO4SkB2-hQXCYJPfmCbQPrqb_2bTlbTdZJbdd8excOh-g6Fvu7Jx8PO4ukjsMbI4pRX93Xl_X8iCAN0Ko7hShUYNot7jxAc1iIGReUtipyH6lkTHhbSTKfLffb_fj_4FQQREO_O7CBHwyz7KKwboKfDOBmddQMZnDWzBvZJjaXYw_MQpupwmz8zvwnF8c4jZy6zhYuS6XDSADZ7YX03y8Xnd2vI-U7uRSmnHDDYnnrEhnLfzkJ4ASmqpqLhRtDVTUdSUZn8JWJmGEbJZaHhigY3DLKSbAVCM_V4UrxkoV45hIWdqbW7avlm5yTipOObYrgGIRMTOPAP2OX79UeMdNrAkv9V8WvpZKvEkbv7lQYAVuY1qU6ljYZ7KGzX7ksrMRaqTbPx2n88spZmK0zP0pHYVLGnhJGGxP7fK5oRbvkcs-3RSCpTsP2WqsdWUyWePJzsOZlX6RtipX91sxow0rZqCMsCxflaMC9a2VGfd7lslWNw8IU0nwM4H_b2E2rF_cezOkUI7KisxRtHf9gzGVYI6SrrUAprJZzmV0gfCapKvq6zKkgzSUYIeul1bxmcS12CGo19MT7X3697NQ_cQR6KMLNlGsIOdkwHsfKdDDFmA&k=6LdAvUIUAAAAAHjrjmjtNTcXyKm0WKwefLp-dQv9

def download_image(url, save_path):
    # Send a GET request to the image URL
    response = requests.get(url, stream=True)
    response.raise_for_status()

    # Check if the request was successful and the content is an image
    if response.status_code == 200 and 'image' in response.headers['Content-Type']:
        # Save the image to the specified path
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    else:
        print("Failed to download the image.")

local_path = "captcha_image.jpg"
download_image(captcha_image, local_path)

original_image = Image.open(local_path)

# Get the dimensions of the smaller images
smaller_image_width = original_image.width // 3
smaller_image_height = original_image.height // 3

# Loop through the rows and columns
for i in range(3):
    for j in range(3):
        # Define the coordinates of the smaller image
        left = j * smaller_image_width
        top = i * smaller_image_height
        right = (j + 1) * smaller_image_width
        bottom = (i + 1) * smaller_image_height
        
        # Crop the smaller image
        smaller_image = original_image.crop((left, top, right, bottom))
        
        # Save the smaller image
        smaller_image.save(f"output_image_{i}_{j}.jpg")

print("Images saved successfully.")


# # Find and click the search button
# search_button = driver.find_element_by_name('btnK')
# search_button.click()

# # Close the browser
# driver.quit()

# def click_images(argument):
#     if argument == "output_image_0_0.jpg":
#         return driver.find_element(By.CLASS_NAME, "fbc-imageselect-checkbox-1").click()
#     elif argument == "output_image_0_1.jpg":
#         return driver.find_element(By.CLASS_NAME, "fbc-imageselect-checkbox-2").click()
#     elif argument == "output_image_0_2.jpg":
#         return driver.find_element(By.CLASS_NAME, "fbc-imageselect-checkbox-3").click()
#     elif argument == "output_image_1_0.jpg":
#         return driver.find_element(By.CLASS_NAME, "fbc-imageselect-checkbox-4").click()
#     elif argument == "output_image_1_1.jpg":
#         return driver.find_element(By.CLASS_NAME, "fbc-imageselect-checkbox-5").click()
#     elif argument == "output_image_1_2.jpg":
#         return driver.find_element(By.CLASS_NAME, "fbc-imageselect-checkbox-6").click()
#     elif argument == "output_image_2_0.jpg":
#         return driver.find_element(By.CLASS_NAME, "fbc-imageselect-checkbox-7").click()
#     elif argument == "output_image_2_1.jpg":
#         return driver.find_element(By.CLASS_NAME, "fbc-imageselect-checkbox-8").click()
#     elif argument == "output_image_2_2.jpg":
#         return driver.find_element(By.CLASS_NAME, "fbc-imageselect-checkbox-9").click()
#     else:
#         return "No Match"


# example_results = [
#   {
#     "image_path": "output_image_2_0.jpg", 
#     "match": "Yes"
#   },
#   {
#     "image_path": "output_image_1_1.jpg",
#     "match": "Yes"
#   },
#   {
#     "image_path": "output_image_2_2.jpg",
#     "match": "Yes"
#   },
#   {
#     "image_path": "output_image_0_1.jpg",
#     "match": "No"
#   },
#   {
#     "image_path": "output_image_0_0.jpg", 
#     "match": "No"
#   },
#   {
#     "image_path": "output_image_0_2.jpg",
#     "match": "No"
#   },
#   {
#     "image_path": "output_image_1_2.jpg", 
#     "match": "No"
#   },
#   {
#     "image_path": "output_image_2_1.jpg",
#     "match": "No"
#   },
#   {
#     "image_path": "output_image_1_0.jpg",
#     "match": "No"
#   }
# ]

# for result in example_results:
#     if result['match'] == "Yes":
#         # print(result["image_path"])
#         click_images(result['image_path'])

# # driver.find_element(By.CLASS_NAME, "fbc-button-verify").submit()

# time.sleep(20)

