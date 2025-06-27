import os
import time
import random
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def human_delay(self, min_seconds, max_seconds):
        time.sleep(random.uniform(min_seconds, max_seconds))

    def login(self):
        print("🚀 Starting Instagram login...")
        self.driver.get("https://www.instagram.com/accounts/login/")
        self.human_delay(2, 4)

        try:
            username_input = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
            username_input.send_keys(self.username)
            self.human_delay(1, 2)

            password_input = self.driver.find_element(By.NAME, "password")
            password_input.send_keys(self.password)
            self.human_delay(1, 2)

            login_btn = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            login_btn.click()
            self.human_delay(5, 7)
            print("✅ Login successful!")
        except TimeoutException:
            print("❌ Login failed. Could not find login elements.")
            self.close()

    def follow_and_extract_profile(self, profile_url: str, output_file: str = "cbitosc_profile.txt"):
        """
        Visit a profile, follow it, and extract profile data to a text file.
        Args:
            profile_url: Instagram profile URL (e.g., https://www.instagram.com/cbitosc/)
            output_file: Path to save extracted profile data
        """
        print(f"🔍 Visiting profile: {profile_url}")
        try:
            self.driver.get(profile_url)
            self.human_delay(3, 5)

            # Try to follow if not already following
            try:
                follow_button_xpath = "//*[text()='Follow']"
                follow_btn = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, follow_button_xpath))
                )
                follow_btn.click()
                print("✅ Followed the account.")
                self.human_delay(2, 3)
            except TimeoutException:
                print("📝 Already following or follow button not found.")

            # Extract profile data
            profile_data = {}
            try:
                header = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, "//header"))
                )

                try:
                    profile_data['username'] = header.find_element(By.XPATH, ".//h2").text
                except:
                    profile_data['username'] = "cbitosc"

                try:
                    display_name = header.find_element(By.XPATH, ".//h1").text
                except:
                    display_name = ""
                
                try:
                    # The bio is usually in a div with a specific class.
                    bio_element = header.find_element(By.XPATH, ".//div[contains(@class, '_aa_c')]")
                    # Clean the bio text by removing the display name if it's included
                    profile_data['bio'] = bio_element.text.replace(display_name, '').strip()
                except:
                    profile_data['bio'] = "Bio not found"

                try:
                    stats_list = header.find_element(By.TAG_NAME, "ul")
                    stats = stats_list.find_elements(By.TAG_NAME, "li")
                    if len(stats) >= 3:
                        posts_text = stats[0].text
                        followers_text = stats[1].text
                        following_text = stats[2].text
                        
                        profile_data['posts'] = posts_text.split('\n')[0]
                        profile_data['followers'] = followers_text.split('\n')[0]
                        profile_data['following'] = following_text.split('\n')[0]
                except Exception as e:
                    print(f"Could not extract all stats: {e}")
                    profile_data['posts'] = profile_data['followers'] = profile_data['following'] = ""

            except TimeoutException:
                 print("Could not find profile header.")
                 profile_data = {'username': 'cbitosc', 'bio': '', 'posts': '', 'followers': '', 'following': ''}


            # Save to file
            with open(output_file, "w", encoding="utf-8") as f:
                for k, v in profile_data.items():
                    f.write(f"{k}: {v}\n")
            print(f"📄 Profile data saved to {output_file}")

        except Exception as e:
            print(f"❌ Error during profile visit or data extraction: {str(e)}")

    def close(self):
        print("🔴 Closing the browser.")
        self.driver.quit()

if __name__ == "__main__":
    load_dotenv()
    # It is recommended to use environment variables for security
    INSTAGRAM_USERNAME = os.environ.get("INSTAGRAM_USERNAME")
    INSTAGRAM_PASSWORD = os.environ.get("INSTAGRAM_PASSWORD")

    if not INSTAGRAM_USERNAME or not INSTAGRAM_PASSWORD:
        print("⚠️ Please set your INSTAGRAM_USERNAME and INSTAGRAM_PASSWORD in a .env file.")
    else:
        bot = InstagramBot(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
        bot.login()
        bot.follow_and_extract_profile("https://www.instagram.com/cbitosc/")
        bot.close()
