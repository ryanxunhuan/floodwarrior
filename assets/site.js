(() => {
  const menu = document.querySelector('.research-menu');
  if (!menu) return;
  document.addEventListener('click', event => {
    if (!menu.contains(event.target)) menu.open = false;
  });
  menu.addEventListener('keydown', event => {
    if (event.key === 'Escape') {
      menu.open = false;
      menu.querySelector('summary').focus();
    }
  });
  menu.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
    menu.open = false;
  }));
})();
