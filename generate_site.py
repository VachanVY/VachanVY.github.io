#!/usr/bin/env python3
"""
Static Site Generator for Academic Blog
Converts Markdown posts to HTML with proper styling and navigation.
"""

import os
import re
import glob
from datetime import datetime
from pathlib import Path

def extract_metadata(content):
    """Extract title and date from markdown content."""
    lines = content.split('\n')
    title = "Untitled Post"
    date = datetime.now().strftime("%B %d, %Y")
    
    # Look for title (first h1)
    for line in lines:
        if line.startswith('# '):
            title = line[2:].strip()
            break
    
    # Look for date in italic format
    for line in lines:
        date_match = re.search(r'\*Published:\s*([^*]+)\*', line)
        if date_match:
            date = date_match.group(1).strip()
            break
    
    return title, date

def markdown_to_html(markdown_content):
    """Convert basic markdown to HTML."""
    html = markdown_content
    
    # Convert headers
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    
    # Convert bold and italic
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    
    # Convert links
    html = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', html)
    
    # Convert code blocks (simple)
    html = re.sub(r'`(.+?)`', r'<code>\1</code>', html)
    
    # Convert paragraphs
    paragraphs = html.split('\n\n')
    processed_paragraphs = []
    
    for para in paragraphs:
        para = para.strip()
        if para:
            # Skip if it's already an HTML tag
            if not (para.startswith('<h') or para.startswith('<ul') or 
                   para.startswith('<ol') or para.startswith('<div')):
                # Convert lists
                if para.startswith('- '):
                    items = para.split('\n')
                    list_html = '<ul>\n'
                    for item in items:
                        if item.startswith('- '):
                            list_html += f'  <li>{item[2:].strip()}</li>\n'
                    list_html += '</ul>'
                    processed_paragraphs.append(list_html)
                else:
                    processed_paragraphs.append(f'<p>{para}</p>')
            else:
                processed_paragraphs.append(para)
    
    return '\n\n'.join(processed_paragraphs)

def create_html_page(title, date, content, back_link="../index.html"):
    """Create a complete HTML page for a blog post."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Vachan V Y</title>
    <link rel="stylesheet" href="../style.css">
</head>
<body>
    <div class="container">
        <a href="{back_link}" class="back-link">← Back to Home</a>
        
        <article>
            <header class="post-header">
                <h1 class="post-title">{title}</h1>
                <div class="post-date">{date}</div>
            </header>
            
            <div class="post-content">
                {content}
            </div>
        </article>
        
        <a href="{back_link}" class="back-link">← Back to Home</a>
    </div>
</body>
</html>"""

def process_markdown_files(posts_dir="posts"):
    """Process all markdown files in the posts directory."""
    if not os.path.exists(posts_dir):
        print(f"Posts directory '{posts_dir}' not found!")
        return
    
    markdown_files = glob.glob(os.path.join(posts_dir, "*.md"))
    
    if not markdown_files:
        print(f"No markdown files found in '{posts_dir}' directory!")
        return
    
    print(f"Processing {len(markdown_files)} markdown files...")
    
    for md_file in markdown_files:
        print(f"Processing: {md_file}")
        
        # Read markdown content
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract metadata
        title, date = extract_metadata(content)
        
        # Convert to HTML
        html_content = markdown_to_html(content)
        
        # Create full HTML page
        html_page = create_html_page(title, date, html_content)
        
        # Write HTML file
        html_filename = os.path.splitext(md_file)[0] + '.html'
        with open(html_filename, 'w', encoding='utf-8') as f:
            f.write(html_page)
        
        print(f"Created: {html_filename}")

def main():
    """Main function to run the static site generator."""
    print("=== Academic Site Generator ===")
    print("Converting Markdown posts to HTML...")
    
    # Change to the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Process markdown files
    process_markdown_files()
    
    print("\nDone! Your static site is ready.")
    print("\nTo view your site:")
    print("1. Open index.html in a web browser")
    print("2. Or serve with: python -m http.server 8000")
    print("3. Then visit: http://localhost:8000")

if __name__ == "__main__":
    main()