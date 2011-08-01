from django import template

from pygments import highlight
from pygments.lexers import guess_lexer, PythonLexer, get_lexer_by_name
from pygments.formatters import HtmlFormatter
from BeautifulSoup import BeautifulSoup
# Python Markdown (dropped in my project directory)
from markdown import markdown

register = template.Library()

@register.filter
def pygmentize(value):
    try:
        soup = BeautifulSoup(value)
        code_blocks = soup.findAll('code')
        for code in code_blocks:
            #print code
            try:
                lexer = guess_lexer(code.string)
            except ValueError:
                lexer = PythonLexer()
            code.replaceWith(highlight(code.string, lexer, HtmlFormatter()))
        return str(soup)
    except:
        return value.replace('<code>', '<div class="highlight"><pre>').replace('</code>', '</pre></div>')

@register.filter
def render(content, safe="unsafe"):
    """Render this content for display."""

    # First, pull out all the <code></code> blocks, to keep them away
    # from Markdown (and preserve whitespace).
    soup = BeautifulSoup(str(content))
    code_blocks = soup.findAll('code')
    for block in code_blocks:
        block.replaceWith('<code class="removed"></code>')

    # Run the post through markdown.
    if safe == "unsafe":
        safe_mode = False
    else:
        safe_mode = True
    markeddown = markdown(str(soup), safe_mode=safe_mode)

    # Replace the pulled code blocks with syntax-highlighted versions.
    soup = BeautifulSoup(markeddown)
    empty_code_blocks, index = soup.findAll('code', 'removed'), 0
    formatter = HtmlFormatter(cssclass='source')
    for block in code_blocks:
        if block.has_key('class'):
            # <code class='python'>python code</code>
            language = block['class']
        else:
            # <code>plain text, whitespace-preserved</code>
            language = 'text'
        try:
            lexer = get_lexer_by_name(language, stripnl=True, encoding='UTF-8')
        except ValueError, e:
            try:
                # Guess a lexer by the contents of the block.
                lexer = guess_lexer(block.renderContents())
            except ValueError, e:
                # Just make it plain text.
                lexer = get_lexer_by_name('text', stripnl=True, encoding='UTF-8')
        empty_code_blocks[index].replaceWith(
                highlight(block.renderContents(), lexer, formatter))
        index = index + 1

    return str(soup)