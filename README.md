# Haichao Xing Photography Portfolio

A minimal and elegant photography portfolio website for showcasing themed photo collections. The left sidebar features theme navigation, and the right displays large images. Click the image to switch to the next photo within the same theme.

## Directory Structure

```
510Portofolio_Web/
├── app.py
├── README.md
└── static/
    └── photos/
        ├── Sakura-1.jpg
        ├── Sakura-2.jpg
        ├── Muse-1.jpg
        ├── Muse-2.jpg
        ├── Botanica-1.jpg
        ├── Botanica-2.jpg
        ├── Pier-1.jpg
        └── Pier-2.jpg
```

## How to Add or Replace Images
1. Place your images in the `static/photos/` folder.
2. File names must match those in `app.py`, e.g., `Sakura-1.jpg`, `Muse-2.jpg`, etc.
3. Each theme contains two images; replace as needed.

## How to Run
1. Install dependencies (recommended: use a virtual environment):
   ```bash
   pip install flask
   ```
2. Start the website:
   ```bash
   python app.py
   ```
3. Open your browser and visit:
   ```
   http://127.0.0.1:5001/
   ```

## Customizing Themes and Images
- Edit the `portfolio_groups` list in `app.py` to change theme names or image paths.
- Both local images (recommended: jpg/png) and online image URLs are supported.

## Features
- Minimal white background, non-wrapping sidebar navigation, and centered adaptive image display.
- Click the image to switch to the next photo in the current theme.
- Easily add or remove themes and images by editing `app.py`.

---
For further customization or feature requests, feel free to contact the author or continue improving the project! 