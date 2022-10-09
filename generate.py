import re
from pathlib import Path

lines_in = iter(Path("src/readme_source.md").read_text().splitlines())
lines_out = []

example_re = re.compile(
    r"```html example(\s+(?P<template>[\w_]+))?(\s+(?P<start_line>\d+)(-(?P<end_line>\d+))?)?"
)

example_snippet = """
<table class="example">
  <tr>
    <td>
      <sub>{}</sub>
      <pre lang="html">{}</pre>
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
        match = example_re.match(line)
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
            # lines_out.append("<table>")
            # lines_out.append("<tr>")
            # lines_out.append("<td><code>")
            # lines_out.append(example_lines)
            # lines_out.append("</code></td>")
            # lines_out.append("<td>")
            # lines_out.append(running_example.format(f"examples/{example_file_name}"))
            # lines_out.append("</td>")
            # lines_out.append("</tr>")
            # lines_out.append("<tr>")
            # lines_out.append("</table>")

            # Add example snippet
            # lines_out.extend()

            # Add example tag
            # lines_out.append(f"<sup>Example {example_number}</sup>".upper())

            # Add example iframe
            # lines_out.append(running_example.format(f"examples/{example_file_name}"))

            # Add link to full example code
            # lines_out.append(
            #     f'<button onclick="location.href=\'examples/{example_file_name}\'">Open in full screen</button>'
            # )

except StopIteration:
    pass

print(f"Examples: {example_number}")

result = "\n".join(lines_out)
Path("docs/README.md").write_text(result)
