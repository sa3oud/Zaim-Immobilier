import re

def convert_template(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create a complete HTML structure
    html_template = f'''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>ZAIM - Trouvez Votre Maison Idéale à Casablanca</title>
    <link rel="stylesheet" href="static/css/style.css">
    <link rel="stylesheet" href="static/css/styles.css">
</head>
<body>
{content}
    <script src="static/js/script.js"></script>
</body>
</html>
'''
    
    # Remove Jinja2 template tags
    html_template = re.sub(r'{%\s*extends\s*".*?"\s*%}', '', html_template)
    html_template = re.sub(r'{%\s*block\s*\w+\s*%}', '', html_template)
    html_template = re.sub(r'{%\s*endblock\s*%}', '', html_template)
    
    # Replace url_for references
    html_template = re.sub(
        r'{{ url_for\(\'static\', filename=\'(.*?)\'\) }}', 
        r'static/\1', 
        html_template
    )
    
    # Fix image URLs
    html_template = re.sub(
        r'background-image: url\(""(.*?)""\)', 
        r'background-image: url("static/images/\1")', 
        html_template
    )
    
    # Remove any remaining Jinja2 template syntax
    html_template = re.sub(r'{{.*?}}', '', html_template)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_template)

# Run the conversion
convert_template('templates/index.html', 'public/index.html')
