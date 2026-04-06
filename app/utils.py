import re
import html
from logger import logger


def log_error(message):
    logger.error(message)


def format_response(response):
    """
    Convert markdown-like response into HTML-safe formatted output
    """

    # escape HTML 
    response = html.escape(response)

    # Handle code blocks
    if "```" in response:
        parts = response.split("```")
        formatted_response = ""

        for i, part in enumerate(parts):
            if i % 2 == 1:
                formatted_response += f'<pre class="code-block"><code>{part}</code></pre>'
            else:
                formatted_response += part.replace('\n', '<br>')

        return formatted_response
    
    #replace newlines with <br> for line breaks
    response = response.replace("\n", "<br>")

    # Convert bold texts
    response = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', response)
    
    # Convert italic texts
    response = re.sub(r'(?<!\*)\*(?!\*)(.*?)\*(?<!\*)', r'<em>\1</em>', response)


    response = re.sub(
        r'(?m)^(#+)\s*(.*)',
        lambda m: f'<h{len(m.group(1))}>{m.group(2)}</h{len(m.group(1))}>',
        response
    )

    response = re.sub(r'(?m)^\d+\.\s*(.*)', r'<li>\1</li>', response)
    response = re.sub(r'(?m)^\-\s*(.*)', r'<li>\1</li>', response)


    response = re.sub(r'(<li>.*?</li>)+', lambda m: f"<ul>{m.group(0)}</ul>", response)

    return response