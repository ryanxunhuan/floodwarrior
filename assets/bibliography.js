(() => {
  const controls = document.querySelector('.bib-controls');
  if (!controls) return;
  controls.hidden = false;
  const search = document.querySelector('#bib-search');
  const status = document.querySelector('#bib-status');
  const records = [...document.querySelectorAll('.bib-entry')];
  const count = document.querySelector('#bib-count');
  const empty = document.querySelector('.bib-empty');
  function filterRecords() {
    const terms = search.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    let visible = 0;
    for (const record of records) {
      const matches = terms.every(term => record.dataset.search.includes(term)) &&
        (status.value === 'all' || record.dataset.status === status.value);
      record.hidden = !matches;
      visible += Number(matches);
    }
    count.textContent = `${visible} of ${records.length} records`;
    empty.hidden = visible !== 0;
  }
  search.addEventListener('input', filterRecords);
  status.addEventListener('change', filterRecords);
})();
