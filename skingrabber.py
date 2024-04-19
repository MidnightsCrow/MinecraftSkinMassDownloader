import os
import threading
import requests

def download_skin(url, folder="skins"):
    """Downloads a Minecraft skin from the given URL to the specified folder.

    Args:
        url (str): The URL of the Minecraft skin to download.
        folder (str, optional): The folder to save the downloaded skin. Defaults to "skins".

    Returns:
        None
    """

    filename = url.split("/")[-1]  # Extract filename from URL
    filepath = os.path.join(folder, filename)

    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(filepath, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Downloaded skin: {filename}")
        else:
            print(f"Error downloading {filename} - Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {filename}: {e}")

def main():
    """Reads usernames from a file, builds URLs, and downloads skins concurrently using threads."""
    folder = "Skins"  # Change this to your desired folder
    os.makedirs(folder, exist_ok=True)  # Create folder if it doesn't exist

    with open("uuid_list.txt", 'r') as file:
        usernames = [line.strip() for line in file]  # Read all usernames into a list

    # Limit the number of concurrent downloads
    max_threads = 30

    threads = []
    for i, username in enumerate(usernames):
        if i >= max_threads:
            # Wait for a thread to finish before starting a new one
            for thread in threads:
                thread.join()
            threads.clear()

        url = f"https://minotar.net/download/{username}.png"
        thread = threading.Thread(target=download_skin, args=(url, folder))
        threads.append(thread)
        thread.start()

    # Wait for all remaining threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
    