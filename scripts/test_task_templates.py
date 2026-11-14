"""Offline contract/handler checks; not a browser, ChatGPT host or Cortex test."""
import json
from pathlib import Path
import re
import shutil
import subprocess
import unittest

SKILL = Path(__file__).resolve().parents[1] / "source/cortex-playbook-engineer"


class TaskTemplateTests(unittest.TestCase):
    def test_complete_output_schemas(self):
        for relative in ("templates/ai-triage-contract.md", "examples/windows-ai-task.md"):
            with self.subTest(template=relative):
                schema = json.loads(re.search(r"```json\n(.*?)\n```", (SKILL / relative).read_text(), re.S)[1])
                self.assertEqual(schema["type"], "object")
                self.assertEqual(set(schema["required"]), set(schema["properties"]))
                self.assertFalse(schema["additionalProperties"])
                self.assertEqual(set(schema), {"type", "properties", "required", "additionalProperties"})

    def test_windows_aliases_have_explicit_mapping_rows(self):
        content = (SKILL / "examples/windows-ai-task.md").read_text()
        prompt = re.search(r"```text\n(.*?)\n```", content, re.S)[1]
        aliases = re.findall(r"\$\{([^}]+)\}", prompt)
        rows = re.findall(r"^\| (\w+) / `\$\{(\w+)\}`", content, re.M)
        self.assertEqual(len(aliases), len(set(aliases)))
        self.assertEqual(set(aliases), {alias for alias, _ in rows})
        self.assertTrue(all(alias == placeholder for alias, placeholder in rows))

    @unittest.skipUnless(shutil.which("node"), "Node unavailable; local handler execution NOT RUN")
    def test_panel_handlers_with_minimal_element_doubles(self):
        content = (SKILL / "templates/interactive-task-panel.md").read_text()
        script = re.search(r"<script>\n(.*?)\n</script>", content, re.S)[1]
        # Element doubles exercise callbacks and text handling, not DOM/layout/clipboard.
        harness = r'''
const assert = require('node:assert/strict');
const vm = require('node:vm');
const fs = require('node:fs');
function element(label) {
  return {checked:false, dataset:{check:label}, value:'', textContent:'', events:{},
    addEventListener(name, fn){this.events[name]=fn;},
    focus(){this.focused=true;}, select(){this.selected=true;}};
}
const checks=['aliases','mappings','schema'].map(element);
const note=element(), summary=element(), output=element(), select=element();
const nodes={'[data-note]':note,'[data-summary]':summary,'output':output,'[data-select]':select};
const root={querySelectorAll(selector){assert.equal(selector,'[data-check]');return checks;},
  querySelector(selector){assert.ok(nodes[selector]);return nodes[selector];}};
vm.runInNewContext(fs.readFileSync(0,'utf8'),{document:{getElementById(id){assert.equal(id,'cortex-task-checks');return root;}}});
assert.equal(output.textContent,'0 de 3 itens marcados localmente');
checks[0].checked=true;checks[0].events.change();
assert.equal(output.textContent,'1 de 3 itens marcados localmente');
note.value='<img src=x onerror="sendSecret()">';note.events.input();
assert.ok(summary.value.includes(note.value));
checks.forEach(item=>{item.checked=true;item.events.change();});
assert.equal(output.textContent,'3 de 3 itens marcados localmente');
assert.ok(summary.value.includes('não observadas'));
assert.ok(!summary.value.includes('PASS'));
checks[0].checked=false;checks[0].events.change();
assert.equal(output.textContent,'2 de 3 itens marcados localmente');
select.events.click();assert.equal(summary.selected,true);assert.equal(summary.focused,true);
'''
        result = subprocess.run([shutil.which("node"), "-e", harness], input=script,
                                text=True, capture_output=True, timeout=15)
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
