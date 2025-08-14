def create_html(tag, text, **attributes):
    html = f"<{tag}"
    
    for key, value in attributes.items():
        html += f" {key}='{value}'"
        
    html = html + f">{text}</{tag}>"
    return html

html = create_html("p", "Hello World!", style="paragraf")
print(html)
html = create_html("a", "Ini Link", href="https://www.example.com", target="_blank")
print(html)
html = create_html("div", "Ini Div", class_="container", id="main")
print(html)