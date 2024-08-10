
# TikTok Video Uploader Bot

This Python script automates the process of uploading videos to TikTok using Selenium and Chrome WebDriver. The bot allows you to log in manually, then automatically uploads a video to your TikTok account.

## Features
- Manual login process for added security.
- Automatic video uploading with customizable captions.
- Error handling and retry mechanism for failed uploads.

## Prerequisites

Before you can run the script, ensure you have the following installed:

- Python 3.x
- Google Chrome
- `pip` (Python package installer)

### Required Python Packages

Install the required packages using pip:

```bash
pip install selenium requests webdriver-manager
```

## Usage

1. **Download the script**: Clone the repository or download the script directly.

   ```bash
   git clone https://github.com/yourusername/tiktok-video-uploader-bot.git
   cd tiktok-video-uploader-bot
   ```

2. **Edit the Script**:
   - Modify the `video_path` in the `upload()` function to point to the video you want to upload.
   - Ensure you have a `caption.txt` file in the same directory as the script, containing the captions or hashtags you want to add to the video.

3. **Run the Script**:
   - Open a terminal in the directory containing the script.
   - Run the script using Python:

   ```bash
   python tiktok_uploader.py
   ```

4. **Manual Login**:
   - The script will open a Chrome window and navigate to TikTok's login page.
   - You will have 50 seconds to log in manually.
   - Once logged in, the bot will proceed to upload the video automatically.

## Customization

### Video Path

You need to update the video path in the `upload()` function to point to your video file.

```python
upload(r"C:\Users\yourusername\Videos\your-video-here.mov")
```

### Captions

The bot reads captions from a `caption.txt` file. Each line in the file should be a separate caption or hashtag.

## Known Issues

- **Login Timeout**: If you are unable to log in within 50 seconds, you may need to increase the wait time in the script.
- **Upload Errors**: The bot includes a retry mechanism, but some errors may still require manual intervention.

## Contributing

If you find a bug or want to contribute to the project, feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
