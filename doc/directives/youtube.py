from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.application import Sphinx
from typing import List, Any

class YouTube(Directive):
  # Define what the directive accepts
  has_content = True
  required_arguments = 1
  optional_arguments = 0
  option_spec = { 'embed': str }

  def run(self):
    embed = self.arguments[0]

    html_code = f'''<div style="text-align:center;">
      <iframe
          width="560"
          height="315"
          src="https://www.youtube-nocookie.com/embed/{embed}"
          title="YouTube video player"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
          referrerpolicy="strict-origin-when-cross-origin"
          allowfullscreen>
      </iframe>
    </div>'''

    raw_node = nodes.raw('', html_code, format='html')
    return [raw_node]

def setup(app: Sphinx) -> dict[str, Any]:
  """Setup function for Sphinx extension."""
  app.add_directive('youtube', YouTube)
  return {
      'version': '1.0',
      'parallel_read_safe': True,
      'parallel_write_safe': True,
  }
