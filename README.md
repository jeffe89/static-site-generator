# Static Site Generator

## Overview

The **Static Site Generator** converts Markdown content into static HTML pages using a customizable template system. This project enables users to create static websites easily, ideal for blogs, documentation, and personal portfolios.

Project deployed via GitHub-Pages: [Static-Site-Generator!](https://jeffe89.github.io/static-site-generator/) (ctrl+click to open in new tab)

## Project Structure

```
static-site-generator/
├── .git/                      # Git repository data
├── .gitignore                 # Specifies files ignored by Git
├── README.md                  # Project documentation (this file)
├── main.sh                    # Script to run the generator and serve the site
├── test.sh                    # Script to execute unit tests
├── template.html              # HTML template for page generation
├── static/                    # Static assets (CSS, images)
│   ├── index.css              # Default stylesheet
│   └── images/                # Image assets
│       └── rivendell.png      # Example image
├── public/                    # Output directory for generated static files
│   ├── index.html             # Generated homepage
│   ├── majesty/               # Example subpage directory
│   │   └── index.html         # Generated subpage
│   ├── images/                # Copied static images
│   │   └── rivendell.png      # Copied image for site use
│   └── index.css              # Copied stylesheet
├── content/                   # Markdown source content
│   ├── index.md               # Main page content
│   └── majesty/               # Subpage content directory
│       └── index.md           # Subpage content
└── src/                       # Source code for the generator
    ├── main.py                # Main script to generate site pages
    ├── htmlnode.py            # HTML element generation logic
    ├── inline_markdown.py     # Inline Markdown parsing
    ├── markdown_blocks.py     # Block-level Markdown processing
    ├── textnode.py            # Text node data structure
    ├── test_htmlnode.py       # Tests for htmlnode.py
    ├── test_inline_markdown.py# Tests for inline_markdown.py
    ├── test_markdown_blocks.py# Tests for markdown_blocks.py
    └── test_textnode.py       # Tests for textnode.py
```

## Installation

### Prerequisites

- **Python 3.x**: Confirm installation with:
  ```bash
  python3 --version
  ```
- **Git** *(optional)*: For version control.

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd static-site-generator
   ```
2. **(Optional) Set up a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```
3. **Install dependencies:** No external dependencies beyond Python's standard library are required.

## Running the Program

To generate and preview the static site:

```bash
./main.sh
```

**Workflow:**

1. Runs `src/main.py` to process Markdown files and generate HTML files into the `public/` directory.
2. Launches a local HTTP server at `http://localhost:8888` for previewing the generated site.

## Core Implementation Details
### Source Code Overview
- **`src/main.py`**: The main entry point of the project. It handles the following tasks:
  - Reads Markdown files from the `content/` directory.
  - Uses helper modules to convert Markdown into HTML.
  - Integrates the generated HTML into the `template.html` file.
  - Saves the final pages into the `public/` directory.
- **`src/htmlnode.py`**: Contains the `HTMLNode` class, responsible for creating and rendering HTML elements with:
  - Tag names (e.g., `div`, `p`, `h1`)
  - Attributes (e.g., classes, ids)
  - Child nodes and text content.
- **`src/inline_markdown.py`**: Processes inline Markdown elements, handling conversions like:
  - Bold text: `**bold**` → `<strong>`
  - Italics: `*italic*` → `<em>`
  - Links: `[link](url)` → `<a href='url'>link</a>`
- **`src/markdown_blocks.py`**: Focuses on block-level Markdown processing, converting elements like:
  - Headers: `# Header` → `<h1>Header</h1>`
  - Lists: `- Item` or `1. Item` → `<ul>`/`<ol>`
  - Code blocks and blockquotes.
- **`src/textnode.py`**: Defines the `TextNode` class, which represents text elements that may include inline styles or links. Used extensively in the conversion pipeline.
- **Test Files:**
  - **`src/test_htmlnode.py`**: Validates HTML node creation, rendering logic, and attribute handling.
  - **`src/test_inline_markdown.py`**: Tests inline Markdown conversions, ensuring correct HTML output.
  - **`src/test_markdown_blocks.py`**: Ensures block-level Markdown elements are converted accurately.
  - **`src/test_textnode.py`**: Confirms proper construction and manipulation of text nodes.
  
These modules work together to read content, process Markdown, and generate HTML files for static web pages.\

## Unit Tests

Run tests using:

```bash
./test.sh
```

## Deployment

The generated static files in `public/` can be hosted on platforms like:

- **GitHub Pages**: Push to a `gh-pages` branch.
- **Netlify**: Drag and drop the `public/` folder in the dashboard.
- **Vercel**: Deploy directly through the Vercel CLI.

## Contribution Guidelines

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit changes with clear messages.
4. Submit a pull request.

## License

This project is under the MIT License. See `LICENSE` for details.

## Author
Geoffrey Giordano

---

This README was generated to provide clarity on the project's structure, usage, and best practices.
