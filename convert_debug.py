import re
import os

def convert_template(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Debug: print original content length
    print(f"Original content length: {len(content)} characters")
    
    # Remove Jinja2 block tags
    content = re.sub(r'{%\s*extends\s*".*?"%}', '<!DOCTYPE html>\n<html lang="fr">', content)
    content = re.sub(r'{%\s*block\s*\w+\s*%}', '', content)
    content = re.sub(r'{%\s*endblock\s*%}', '', content)
    
    # Detailed URL conversion with debug logging
    def url_replace(match):
        original = match.group(0)
        replaced = f'"{original.split("\'")[-2]}"'
        print(f"URL Conversion - Original: {original}, Replaced: {replaced}")
        return replaced
    
    content = re.sub(r'{{ url_for\(\'static\', filename=\'(.*?)\'\) }}', 
                     lambda m: f'"{m.group(1)}"', content)
    
    # Fix background image URLs with detailed logging
    def bg_image_replace(match):
        original = match.group(0)
        replaced = f'background-image: url("{original.split("\'")[1]}")'
        print(f"Background Image - Original: {original}, Replaced: {replaced}")
        return replaced
    
    content = re.sub(r'background-image: url\(\'(.*?)\'\)', bg_image_replace, content)
    
    # Add closing html tag
    content += '\n</html>'
    
    # Debug: print converted content length
    print(f"Converted content length: {len(content)} characters")
    
    # Write converted content
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Additional debug: print first 500 characters
    print("First 500 characters of converted content:")
    print(content[:500])

# Create public directory if it doesn't exist
os.makedirs('public', exist_ok=True)

# Run the conversion
convert_template('templates/index.html', 'public/index.html')
