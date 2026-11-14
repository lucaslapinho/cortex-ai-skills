# Optional local task panel

Use only if the host exposes a documented inline renderer. Read that host's live instructions for fragment location, styling and display. Do not invent a GenUI schema or chat callback. Without that capability use the Markdown task card. The runtime does not require this panel.

This minimal fragment supplies real checkboxes, expandable detail and a selectable progress note. All state is local to the displayed panel and may be lost on reload. It neither saves to XSIAM nor sends a chat message. Replace labels with the current task's checks; keep full prompt/schema/HTML in the response or complete expandable blocks, never omit them to make the panel smaller. Use a unique root ID per panel.

```html
<div id="cortex-task-checks">
  <h3>Checklist da task atual</h3>
  <div class="text-small">Anotações locais; validação no XSIAM não observada.</div>
  <label class="form-check"><input class="form-check-input" type="checkbox" data-check="Aliases revisados"><span class="form-check-label">Aliases revisados</span></label>
  <label class="form-check"><input class="form-check-input" type="checkbox" data-check="Mapeamentos revisados"><span class="form-check-label">Mapeamentos revisados</span></label>
  <label class="form-check"><input class="form-check-input" type="checkbox" data-check="JSON Schema revisado"><span class="form-check-label">JSON Schema revisado</span></label>
  <output aria-live="polite">0 de 3 itens marcados localmente</output>
  <details><summary>Registrar observação</summary>
    <label class="form-label">Erro ou observação sanitizada
      <textarea class="form-control" data-note rows="3"></textarea>
    </label>
  </details>
  <label class="form-label">Resumo para copiar e enviar no chat
    <textarea class="form-control" data-summary rows="4" readonly></textarea>
  </label>
  <button class="btn" type="button" data-select>Selecionar resumo</button>
</div>
<script>
(() => {
  const root = document.getElementById('cortex-task-checks');
  const checks = [...root.querySelectorAll('[data-check]')];
  const note = root.querySelector('[data-note]');
  const summary = root.querySelector('[data-summary]');
  const update = () => {
    const selected = checks.filter(item => item.checked).map(item => item.dataset.check);
    root.querySelector('output').textContent = `${selected.length} de ${checks.length} itens marcados localmente`;
    summary.value = 'Registro do usuário; não é resultado do Debugger.\n' +
      'Itens marcados: ' + (selected.join(', ') || 'nenhum') + '\n' +
      'Observação: ' + (note.value || 'não informada') + '\n' +
      'Aceitação/execução no tenant: não observadas por este painel.';
  };
  checks.forEach(item => item.addEventListener('change', update));
  note.addEventListener('input', update);
  root.querySelector('[data-select]').addEventListener('click', () => {
    summary.focus();
    summary.select();
  });
  update();
})();
</script>
```

The select action selects actual text; it does not claim clipboard success. Do not add an Execute, Approve, Save to XSIAM or Next Task control without a real documented capability and applicable authorization. Do not send note contents automatically. Untrusted strings are assigned through `textContent`/`value`, never `innerHTML`. Before presenting a modified panel, check its primary interactions and responsive rendering in the available host; if not tested, report that limit and keep the text fallback.
