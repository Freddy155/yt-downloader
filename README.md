# YouTube Video Downloader

The **YouTube Video Downloader** is a command-line Python application for downloading YouTube videos. It utilizes the PyTube library for video retrieval and the Click library for creating a user-friendly command-line interface.

## Installation

**Prerequisites:**

- Python 3.x installed on your system.
- pip (Python package manager) for installing Python packages.

**Installation Steps:**

1. Clone or download the source code from the [GitHub repository](https://github.com/Freddy155/yt-downloader).

```bash
git clone https://github.com/Freddy155/yt-downloader.git
```

2. Navigate to the directory where you saved the source code using the command line.

```bash
cd yt-downloader
```

3. Install the necessary Python libraries using pip:

```bash
pip install pytube click
```


## Usage

To download a YouTube video using this tool, follow these steps:

1. Open your command-line interface.

2. Navigate to the directory where you saved the YouTube Video Downloader script.

3. Run the script with the following command:

```bash
python app.py
```

4. The application will prompt you to enter the YouTube video URL. Provide the URL and press Enter.

5. The video will be downloaded in the highest available resolution and saved in a 'downloads' folder in the same directory as the script.

## Error Handling

If an error occurs during the download process, the application will display an error message to inform you about the issue.

## Customization

You can customize the behavior of the YouTube Video Downloader by modifying the script. Here are some potential customization options:

- Change the output directory by editing the `output_path` parameter in the script.

- Modify the filename format by adjusting the `filename` variable.

## Contributing

If you'd like to contribute to this project or report issues, you can do so on the [GitHub repository](https://github.com/Freddy155/yt-downloader).

## License

This YouTube Video Downloader is open-source and is released under the [MIT License](LICENSE).

---

Enjoy using the YouTube Video Downloader to save your favorite YouTube videos for offline viewing! If you encounter any issues or have suggestions for improvements, please don't hesitate to reach out on the GitHub repository.
