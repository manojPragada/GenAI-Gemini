import os, re
import export
import google.generativeai as genai

history = []

def askGemini(prompt):
    apikey = os.getenv("API_KEY")
    genai.configure(api_key=apikey)
    model = genai.GenerativeModel("gemini-1.5-flash")
    chat = model.start_chat(history=history)
    response = chat.send_message(prompt)
    gemini_output = response.text
    history.append({"role": "user", "parts": prompt})
    history.append({"role": "model", "parts": gemini_output})
    # print(history)
    return gemini_to_html(gemini_output)

def gemini_to_html(content):
    html = ''
    in_list = False  # Track whether we're inside a list
    in_code_block = False  # Track if we're in a code block

    lines = content.splitlines()

    for line in lines:
        line = applystyles(line)
        # Handle Code Blocks (start and end with ``` or detect indented lines)
        if line.startswith('```'):
            if in_code_block:
                html += "</code></pre>\n"
                in_code_block = False
            else:
                html += "<pre><code>\n"
                in_code_block = True
            continue
        
        if in_code_block:
            html += f"{line}\n"
            continue

        # Handle Headings
        if line.startswith('# '):
            html += f"<h1>{line[2:]}</h1>\n"
        elif line.startswith('## '):
            html += f"<h2>{line[3:]}</h2>\n"
        elif line.startswith('### '):
            html += f"<h3>{line[4:]}</h3>\n"

        # Handle Links
        elif line.startswith('=>'):
            parts = line.split(' ', 2)
            url = parts[1]
            label = parts[2] if len(parts) > 2 else url
            html += f'<a href="{url}">{label}</a><br>\n'

        # Handle Lists
        elif line.startswith('* ') or line.startswith('- '):
            if not in_list:
                html += "<ul>\n"
                in_list = True
            html += f"<li>{line[2:]}</li>\n"

        # Handle Block Quotes
        elif line.startswith('> '):
            html += f"<blockquote>{line[2:]}</blockquote>\n"

        # Handle Inline Code
        else:
            # Close list if we're no longer in it
            if in_list:
                html += "</ul>\n"
                in_list = False

            line = applystyles(line)

            # Convert the line to a paragraph unless it's empty
            if line.strip():
                html += f"<p>{line}</p>\n"

    # Close any unclosed list
    if in_list:
        html += "</ul>\n"

    # Close code block if it wasn't closed properly
    if in_code_block:
        html += "</code></pre>\n"

    return html

def applystyles(line):
    # Convert inline code (e.g., `code` to <code>code</code>)
    line = re.sub(r'`(.+?)`', r'<code>\1</code>', line)

    # Convert bold text (e.g., **bold** to <b>bold</b>)
    line = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', line)

    # Convert italic text (e.g., _italic_ to <i>italic</i>)
    line = re.sub(r'_(.+?)_', r'<i>\1</i>', line)
    return line