'''
Each of the functions in this file takes a single line of input and transforms the line in some way.
'''

def compile_headers(line):
    '''
    Convert markdown headers into <h1>,<h2>,etc tags.

    HINT:
    This is the simplest function to implement in this assignment.
    Use a slices to extract the first part of the line,
    then use if statements to check if they match the appropriate header markdown commands.

    >>> compile_headers('# This is the main header')
    '<h1> This is the main header</h1>'
    >>> compile_headers('## This is a sub-header')
    '<h2> This is a sub-header</h2>'
    >>> compile_headers('### This is a sub-header')
    '<h3> This is a sub-header</h3>'
    >>> compile_headers('#### This is a sub-header')
    '<h4> This is a sub-header</h4>'
    >>> compile_headers('##### This is a sub-header')
    '<h5> This is a sub-header</h5>'
    >>> compile_headers('###### This is a sub-header')
    '<h6> This is a sub-header</h6>'
    >>> compile_headers('      # this is not a header')
    '      # this is not a header'
    '''
    if line.startswith('######'):
        return '<h6>' + line[6:] + '</h6>'
    elif line.startswith('#####'):
        return '<h5>' + line[5:] + '</h5>'
    elif line.startswith('####'):
        return '<h4>' + line[4:] + '</h4>'
    elif line.startswith('###'):
        return '<h3>' + line[3:] + '</h3>'
    elif line.startswith('##'):
        return '<h2>' + line[2:] + '</h2>'
    elif line.startswith('#'):
        return '<h1>' + line[1:] + '</h1>'
    return line

def compile_italic_star(line):
    '''
    Convert "*italic*" into "<i>italic</i>".

    HINT:
    Italics require carefully tracking the beginning and ending positions of the text to be replaced.
    This is similar to the `delete_HTML` function that we implemented in class.
    It's a tiny bit more complicated since we are not just deleting substrings from the text,
    but also adding replacement substrings.

    >>> compile_italic_star('*This is italic!* This is not italic.')
    '<i>This is italic!</i> This is not italic.'
    >>> compile_italic_star('*This is italic!*')
    '<i>This is italic!</i>'
    >>> compile_italic_star('This is *italic*!')
    'This is <i>italic</i>!'
    >>> compile_italic_star('This is not *italic!')
    'This is not *italic!'
    >>> compile_italic_star('*')
    '*'
    '''
    result = ''
    i = 0
    while i < len(line):
        if line[i] == '*':
            # Look for closing *
            closing = -1
            for j in range(i + 1, len(line)):
                if line[j] == '*':
                    closing = j
                    break
            if closing != -1:
                # Found a pair
                result += '<i>' + line[i+1:closing] + '</i>'
                i = closing + 1
            else:
                # No closing *, keep the *
                result += line[i]
                i += 1
        else:
            result += line[i]
            i += 1
    return result


def compile_italic_underscore(line):
    '''
    Convert "_italic_" into "<i>italic</i>".

    HINT:
    This function is almost exactly the same as `compile_italic_star`.

    >>> compile_italic_underscore('_This is italic!_ This is not italic.')
    '<i>This is italic!</i> This is not italic.'
    >>> compile_italic_underscore('_This is italic!_')
    '<i>This is italic!</i>'
    >>> compile_italic_underscore('This is _italic_!')
    'This is <i>italic</i>!'
    >>> compile_italic_underscore('This is not _italic!')
    'This is not _italic!'
    >>> compile_italic_underscore('_')
    '_'
    '''
    import re
    return re.sub(r'_([^_]+)_', r'<i>\1</i>', line)


def compile_strikethrough(line):
    '''
    Convert "~~strikethrough~~" to "<ins>strikethrough</ins>".

    HINT:
    The strikethrough annotations are very similar to implement as the italic function.
    The difference is that there are two delimiting characters instead of one.
    This will require carefully thinking about the range of your for loop and all of your list indexing.

    >>> compile_strikethrough('~~This is strikethrough!~~ This is not strikethrough.')
    '<ins>This is strikethrough!</ins> This is not strikethrough.'
    >>> compile_strikethrough('~~This is strikethrough!~~')
    '<ins>This is strikethrough!</ins>'
    >>> compile_strikethrough('This is ~~strikethrough~~!')
    'This is <ins>strikethrough</ins>!'
    >>> compile_strikethrough('This is not ~~strikethrough!')
    'This is not ~~strikethrough!'
    >>> compile_strikethrough('~~')
    '~~'
    '''
    result = ''
    i = 0
    while i < len(line):
        # Check if we have opening ~~
        if i < len(line) - 1 and line[i] == '~' and line[i+1] == '~':
            # Look for closing ~~
            closing = -1
            for j in range(i + 2, len(line) - 1):
                if line[j] == '~' and line[j+1] == '~':
                    closing = j
                    break
            if closing != -1:
                # Found matching pair
                result += '<ins>' + line[i+2:closing] + '</ins>'
                i = closing + 2
            else:
                # No closing found, keep original
                result += line[i]
                i += 1
        else:
            result += line[i]
            i += 1
    return result


def compile_bold_stars(line):
    '''
    Convert "**bold**" to "<b>bold</b>".

    HINT:
    This function is similar to the strikethrough function.

    >>> compile_bold_stars('**This is bold!** This is not bold.')
    '<b>This is bold!</b> This is not bold.'
    >>> compile_bold_stars('**This is bold!**')
    '<b>This is bold!</b>'
    >>> compile_bold_stars('This is **bold**!')
    'This is <b>bold</b>!'
    >>> compile_bold_stars('This is not **bold!')
    'This is not **bold!'
    >>> compile_bold_stars('**')
    '**'
    '''
    import re
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', line)


def compile_bold_underscore(line):
    '''
    Convert "__bold__" to "<b>bold</b>".

    HINT:
    This function is similar to the strikethrough function.

    >>> compile_bold_underscore('__This is bold!__ This is not bold.')
    '<b>This is bold!</b> This is not bold.'
    >>> compile_bold_underscore('__This is bold!__')
    '<b>This is bold!</b>'
    >>> compile_bold_underscore('This is __bold__!')
    'This is <b>bold</b>!'
    >>> compile_bold_underscore('This is not __bold!')
    'This is not __bold!'
    >>> compile_bold_underscore('__')
    '__'
    '''
    import re
    return re.sub(r'__(.+?)__', r'<b>\1</b>', line)


def compile_code_inline(line):
    '''
    Add <code> tags.

    HINT:
    This function is like the italics functions because inline code uses only a single character as a delimiter.
    It is more complex, however, because inline code blocks can contain valid HTML inside of them,
    but we do not want that HTML to get rendered as HTML.
    Therefore, we must convert the `<` and `>` signs into `&lt;` and `&gt;` respectively.

    >>> compile_code_inline('You can use backticks like this (`1+2`) to include code in the middle of text.')
    'You can use backticks like this (<code>1+2</code>) to include code in the middle of text.'
    >>> compile_code_inline('This is inline code: `1+2`')
    'This is inline code: <code>1+2</code>'
    >>> compile_code_inline('`1+2`')
    '<code>1+2</code>'
    >>> compile_code_inline('This example has html within the code: `<b>bold!</b>`')
    'This example has html within the code: <code>&lt;b&gt;bold!&lt;/b&gt;</code>'
    >>> compile_code_inline('this example has a math formula in the  code: `1 + 2 < 4`')
    'this example has a math formula in the  code: <code>1 + 2 &lt; 4</code>'
    >>> compile_code_inline('this example has a <b>math formula</b> in the  code: `1 + 2 < 4`')
    'this example has a <b>math formula</b> in the  code: <code>1 + 2 &lt; 4</code>'
    >>> compile_code_inline('```')
    '```'
    >>> compile_code_inline('```python3')
    '```python3'
    '''
    import re
    
    # Don't process lines that start with ``` (code fence markers)
    if line.startswith('```'):
        return line
    
    result = []
    i = 0
    while i < len(line):
        # Check for backtick that's not part of triple backticks
        if line[i] == '`':
            # Check it's not a triple backtick
            if i + 2 < len(line) and line[i:i+3] == '```':
                result.append('```')
                i += 3
                continue
            # Find closing backtick
            end = line.find('`', i + 1)
            if end != -1:
                # Extract code content
                code_content = line[i+1:end]
                # Escape HTML characters
                code_content = code_content.replace('<', '&lt;').replace('>', '&gt;')
                result.append(f'<code>{code_content}</code>')
                i = end + 1
            else:
                result.append(line[i])
                i += 1
        else:
            result.append(line[i])
            i += 1
    
    return ''.join(result)


def compile_links(line):
    '''
    Add <a> tags.

    HINT:
    The links and images are potentially more complicated because they have many types of delimeters: `[]()`.
    These delimiters are not symmetric, however, so we can more easily find the start and stop locations using the strings find function.

    >>> compile_links('Click on the [course webpage](https://github.com/mikeizbicki/cmc-csci040)!')
    'Click on the <a href="https://github.com/mikeizbicki/cmc-csci040">course webpage</a>!'
    >>> compile_links('[course webpage](https://github.com/mikeizbicki/cmc-csci040)')
    '<a href="https://github.com/mikeizbicki/cmc-csci040">course webpage</a>'
    >>> compile_links('this is wrong: [course webpage]    (https://github.com/mikeizbicki/cmc-csci040)')
    'this is wrong: [course webpage]    (https://github.com/mikeizbicki/cmc-csci040)'
    >>> compile_links('this is wrong: [course webpage](https://github.com/mikeizbicki/cmc-csci040')
    'this is wrong: [course webpage](https://github.com/mikeizbicki/cmc-csci040'
    '''
def compile_links(line):
    while True:
        # Find the start of a potential link
        bracket_open = line.find('[')
        if bracket_open == -1:
            break
        
        bracket_close = line.find(']', bracket_open)
        if bracket_close == -1:
            break
        
        # Check if '(' immediately follows ']'
        if bracket_close + 1 >= len(line) or line[bracket_close + 1] != '(':
            break
        
        paren_open = bracket_close + 1
        paren_close = line.find(')', paren_open)
        if paren_close == -1:
            break
        
        # Extract text and URL
        link_text = line[bracket_open + 1:bracket_close]
        url = line[paren_open + 1:paren_close]
        
        # Build the <a> tag
        html_link = f'<a href="{url}">{link_text}</a>'
        
        # Replace in line
        line = line[:bracket_open] + html_link + line[paren_close + 1:]
    
    return line


def compile_images(line):
    '''
    Add <img> tags.

    HINT:
    Images are formatted in markdown almost exactly the same as links,
    except that images have a leading `!`.
    So your code here should be based off of the <a> tag code.

    >>> compile_images('[Mike Izbicki](https://avatars1.githubusercontent.com/u/1052630?v=2&s=460)')
    '[Mike Izbicki](https://avatars1.githubusercontent.com/u/1052630?v=2&s=460)'
    >>> compile_images('![Mike Izbicki](https://avatars1.githubusercontent.com/u/1052630?v=2&s=460)')
    '<img src="https://avatars1.githubusercontent.com/u/1052630?v=2&s=460" alt="Mike Izbicki" />'
    >>> compile_images('This is an image of Mike Izbicki: ![Mike Izbicki](https://avatars1.githubusercontent.com/u/1052630?v=2&s=460)')
    'This is an image of Mike Izbicki: <img src="https://avatars1.githubusercontent.com/u/1052630?v=2&s=460" alt="Mike Izbicki" />'
    '''
    import re
    line = re.sub(
        r'!\[([^\]]*)\]\(([^)]*)\)',
        r'<img src="\2" alt="\1" />',
        line
    )
    return line

