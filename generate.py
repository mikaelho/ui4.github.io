import re
from pathlib import Path

lines_in = iter(Path("src/readme_source.md").read_text().splitlines())
lines_out = []

example_in_source = re.compile(
    r"```html example(\s+(?P<template>[\w_]+))?(\s+(?P<start_line>\d+)(-(?P<end_line>\d+))?)?"
)

# Empty line before code example is necessary to make syntax highlighting work
example_snippet = """
<table class="example">
  <tr>
    <td>
      <sub>{}</sub>
      <pre>{}</pre>
    </td>
    <td>
      {}<br/>
      {}
    </td>
  </tr>
</table>"""

running_example = (
        '<iframe style="border-style:none;box-shadow:0px 0px 2px 2px rgba(0,0,0,0.2);" src="{}"></iframe>'
)

example_number = 0

try:
    while True:
        line = next(lines_in)
        match = example_in_source.match(line)
        if not match:
            lines_out.append(line)
        else:
            example_number += 1
            meta = match.groupdict()
            example_content = []
            while line := next(lines_in):
                if line.startswith("```"):
                    break
                else:
                    example_content.append(line)
            template = Path(f"templates/{meta['template'] or 'solid'}.html").read_text()
            example = template.replace("[title]", f"ui4 Example {example_number}")
            example = example.replace("[content]", "\n".join(example_content))
            start_line = (start_as_str := meta.get("start_line")) and int(start_as_str) or None
            end_line = (end_as_str := meta.get("end_line")) and int(end_as_str) or None
            end_line = end_line or start_line
            start_line = start_line and start_line - 1 or None

            # Save example file
            example_file_name = f"example{example_number:04}.html"
            Path(f"docs/examples/{example_file_name}").write_text(example)

            # Lines to show on site
            example_lines = "\n".join(example_content[slice(start_line, end_line)])
            example_lines = example_lines.replace("<", "&lt;")  # .replace("\n", "<br/>")

            # Add example table
            example_table = example_snippet.format(
                f"Example {example_number}".upper(),
                example_lines,
                running_example.format(f"examples/{example_file_name}"),
                f'<button onclick="location.href=\'examples/{example_file_name}\'">Open in full screen</button>'
            )

            lines_out.extend(example_table.splitlines())

except StopIteration:
    pass

print(f"Examples: {example_number}")

result = "\n".join(lines_out)
Path("docs/README.md").write_text(result)
