import json
import os

def json_to_html(json_file, html_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    html_content = '''
    <html>
    <head>
        <title>Test Report</title>
        <style>
            body { font-family: Arial, sans-serif; }
            h1 { color: #333; }
            h2 { color: #666; }
            h3 { color: #999; }
            p { font-size: 14px; }
            img { max-width: 500px; margin-top: 10px; }
        </style>
    </head>
    <body>
    '''
    html_content += '<h1>Test Report</h1>'
    
    for feature in data:
        html_content += f'<h2>Feature: {feature["name"]}</h2>'
        for scenario in feature['elements']:
            html_content += f'<h3>Scenario: {scenario["name"]}</h3>'
            for step in scenario['steps']:
                status = step.get('result', {}).get('status', 'unknown')
                step_name = step["name"].replace(' ', '_')
                html_content += f'<p>{step["keyword"]} {step["name"]}: {status}</p>'
                screenshot_path = os.path.abspath(os.path.join('reports', 'screenshots', f'{step_name}.png'))
                if os.path.exists(screenshot_path):
                    html_content += f'<img src="file://{screenshot_path}" alt="{step_name}"><br>'
                if 'error_message' in step.get('result', {}):
                    html_content += '<pre>' + '\n'.join(step['result']['error_message']) + '</pre>'
    
    html_content += '</body></html>'
    
    with open(html_file, 'w') as f:
        f.write(html_content)

json_to_html('./features/ReporteJson_Requisito1/Requisito1.json', './features/ReporteJson_Requisito1/Requisito1.html')
