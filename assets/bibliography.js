(() => {
  const controls = document.querySelector('.bib-controls');
  if (!controls) return;
  controls.hidden = false;
  const search = document.querySelector('#bib-search');
  const category = document.querySelector('#bib-category');
  const records = [...document.querySelectorAll('.bib-entry')];
  const groups = [...document.querySelectorAll('.bib-group')];
  const count = document.querySelector('#bib-count');
  const empty = document.querySelector('.bib-empty');
  function filterRecords() {
    const terms = search.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    let visible = 0;
    for (const record of records) {
      const matches = terms.every(term => record.dataset.search.includes(term)) &&
        (category.value === 'all' || record.dataset.category === category.value);
      record.hidden = !matches;
      visible += Number(matches);
    }
    for (const group of groups) {
      const matches = group.querySelectorAll('.bib-entry:not([hidden])').length;
      group.hidden = matches === 0;
      group.querySelector('.group-count').textContent = matches;
      const jump = document.querySelector(`[data-group-link="${group.id}"]`);
      jump.hidden = matches === 0;
      jump.querySelector("span").textContent = matches;
    }
    count.textContent = `${visible} of ${records.length} records`;
    empty.hidden = visible !== 0;
  }
  search.addEventListener('input', filterRecords);
  category.addEventListener('change', filterRecords);
  filterRecords();
})();
