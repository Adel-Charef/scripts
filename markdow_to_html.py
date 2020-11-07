import markdown

def md_to_html(): 
    md_text = "# Hello **World**"
    html = markdown.markdown(md_text)
    return html

def table_of_contact():
    md_text = '[TOC]\n# Title\n**text**'
    html = markdown.markdown(md_text, extension=['toc'])
    return html
    

def highlight_code():
    md_text = """
    ```python hl_lines="1 3"
    # some Python code
    hi = 'Hello'
    print(hi)
    ```
    """
    html = markdown.markdown(md_text, extensions=['fenced_code', 'codehilite'])
    return html


