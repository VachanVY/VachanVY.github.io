# Academic Website for GitHub Pages

A clean, minimal static academic website built for GitHub Pages. Features a responsive design, blog functionality, and easy content management.

## Features

- **Clean Design**: Minimal, professional styling focused on content
- **Responsive**: Works perfectly on desktop and mobile devices
- **Blog System**: Markdown-to-HTML conversion for easy blog post creation
- **Academic Focus**: Sections for publications, projects, and professional information
- **GitHub Pages Ready**: Works seamlessly with GitHub Pages hosting

## Structure

```
├── index.html              # Main homepage
├── style.css              # CSS styling
├── generate_site.py       # Python script to convert markdown to HTML
├── posts/                 # Blog posts directory
│   ├── *.md              # Markdown blog posts
│   └── *.html            # Generated HTML blog posts
└── README.md             # This file
```

## Usage

### Adding Blog Posts

1. Create a new markdown file in the `posts/` directory
2. Follow this format:

```markdown
# Your Post Title

*Published: Month Day, Year*

Your content here...
```

3. Run the site generator:

```bash
python generate_site.py
```

4. Update `index.html` to include the new post in the blog section

### Customizing Content

- **Personal Information**: Edit the bio, contact details, and sections in `index.html`
- **Publications**: Update the publications section with your actual papers
- **Projects**: Add your real projects with links to repositories
- **Styling**: Modify `style.css` to customize the appearance

### Local Development

1. Generate HTML from markdown posts:
```bash
python generate_site.py
```

2. Start a local server:
```bash
python -m http.server 8000
```

3. Open http://localhost:8000 in your browser

### Deployment to GitHub Pages

1. Commit all files to your repository
2. Push to the `main` branch (or `gh-pages` branch)
3. Enable GitHub Pages in repository settings
4. Your site will be available at `https://yourusername.github.io`

## Customization

The site is designed to be easily customizable:

- **Colors**: Modify CSS variables for consistent color scheme
- **Layout**: Adjust max-width, spacing, and layout in CSS
- **Content**: Update HTML content and structure as needed
- **Blog Generator**: Extend `generate_site.py` for additional markdown features

## Technical Details

- **HTML5/CSS3**: Modern web standards
- **Python 3**: For markdown processing
- **No Dependencies**: Uses only standard library
- **Mobile-First**: Responsive design principles
- **Fast Loading**: Optimized for speed and accessibility

## License

MIT License - see LICENSE file for details.