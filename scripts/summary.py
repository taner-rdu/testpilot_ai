"""Turn a pytest JUnit XML file into a Markdown summary for the GitHub job summary."""
import sys
import xml.etree.ElementTree as ET

root = ET.parse(sys.argv[1]).getroot()
suite = root if root.tag == "testsuite" else root.find("testsuite")
total = int(suite.get("tests"))
failed = int(suite.get("failures")) + int(suite.get("errors"))
skipped = int(suite.get("skipped"))
passed = total - failed - skipped

print(f"## {'✅' if not failed else '❌'} Test report\n")
print(f"**{passed} passed** · **{failed} failed** · {skipped} skipped · {float(suite.get('time')):.1f}s\n")
print("| Result | Test | Time |\n|---|---|---|")
for case in suite.iter("testcase"):
    failure = case.find("failure") if case.find("failure") is not None else case.find("error")
    icon = "❌" if failure is not None else "⏭️" if case.find("skipped") is not None else "✅"
    print(f"| {icon} | `{case.get('classname')}::{case.get('name')}` | {float(case.get('time')):.1f}s |")

for case in suite.iter("testcase"):
    failure = case.find("failure") if case.find("failure") is not None else case.find("error")
    if failure is not None:
        print(f"\n<details><summary>❌ {case.get('name')}</summary>\n\n```\n{(failure.get('message') or '')[:1500]}\n```\n</details>")
