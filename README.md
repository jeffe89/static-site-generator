# Static Site Generator

## Overview

The **Static Site Generator** project converts Markdown content files into static HTML pages using a templating system. This tool allows users to create and manage static websites with ease, making it suitable for blogs, documentation, or personal portfolios.

## Project Structure

```
static-site-generator/
├── .git/                  # Git repository files
├── .gitignore             # Specifies files ignored by Git
├── README.md              # Project documentation (this file)
├── main.sh                # Shell script to run the application and serve the site
├── test.sh                # Shell script to run unit tests
├── template.html          # HTML template with placeholders for content
├── static/                # Static assets (CSS, images)
│   ├── index.css          # Default stylesheet
│   └── images/            # Image assets
├── public/                # Output directory for generated static files
│   ├── index.html         # Generated homepage
│   └── majesty/index.html # Example generated subpage
├── content/               # Markdown files for content
│   ├── index.md           # Main content markdown
│   └── majesty/index.md   # Example subpage markdown
└── src/                   # Source code for the generator
    ├── main.py            # Main entry point for the generator
    ├── htmlnode.py        # Handles HTML node generation
    ├── inline_markdown.py # Processes inline Markdown elements
    ├── markdown_blocks.py # Handles block-level Markdown parsing
    ├── textnode.py        # Defines text node structures
    └── __pycache__/       # Compiled Python files (ignored)
```

## Installation

### Prerequisites

- **Python 3.x**: Make sure Python is installed. You can verify with:
  ```bash
  python3 --version
  ```
- **Git** *(optional)*: For version control and repository management.

### Steps

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd static-site-generator
   ```
2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:** There are no external dependencies required beyond Python's standard library.

## Running the Program

To generate and serve the static site:

```bash
./main.sh
```

This script:

1. Executes the main Python program (`src/main.py`) to process Markdown files into HTML.
2. Launches a local server at `http://localhost:8888` to view the generated site.

## Project Implementation

### Core Files:

- ``: Entry point; reads Markdown files from `content/` and generates corresponding HTML files in `public/`.
- ``: Manages HTML elements with attributes and content.
- ``: Converts inline Markdown (bold, italics, links) to HTML.
- ``: Processes block-level Markdown elements (headers, lists, code blocks).
- ``: Defines the basic data structure for text content.

### Templates

- ``: Provides the HTML structure with placeholders:
  - `{{ Title }}`: Replaced with the page title.
  - `{{ Content }}`: Replaced with the generated HTML from Markdown.

### Static Assets

- ``: Contains stylesheets (`index.css`) and images used in the generated pages.
- ``: Output directory where final HTML files and assets are placed for serving.

## Running Unit Tests

Run the test suite to ensure code correctness:

```bash
./test.sh
```

This executes unit tests located in the `src/` directory, including:

- `test_htmlnode.py`: Tests for HTML node creation and manipulation.
- `test_inline_markdown.py`: Tests inline Markdown parsing.
- `test_markdown_blocks.py`: Validates block-level Markdown processing.
- `test_textnode.py`: Verifies text node functionality.

## Additional Notes

- **Content Management:** Place Markdown files inside the `content/` directory. The script mirrors the directory structure when generating pages.
- **Template Customization:** Edit `template.html` to change the page layout or styling.
- **Deployment:** Upload the contents of the `public/` folder to any static hosting service (e.g., GitHub Pages, Netlify).
- **Image Support:** Images referenced in Markdown files are automatically copied to the `public/images/` directory.

## Contribution Guidelines

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit changes with descriptive messages.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Author
Geoffrey Giordano

---

Generated with ❤️ to make static site creation simple and efficient.


