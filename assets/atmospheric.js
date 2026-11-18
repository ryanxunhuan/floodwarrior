(() => {
  document.querySelectorAll('[data-animation]').forEach(container => {
    const image = container.querySelector('img');
    const source = container.querySelector('[data-animated-source]');
    const reducedSource = container.querySelector('[data-reduced-motion]');
    const button = container.querySelector('.animation-toggle');
    const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
    const gif = image.getAttribute('src');
    const webp = source.getAttribute('srcset');
    let running = false;

    function setRunning(value) {
      running = value;
      source.srcset = running ? webp : image.dataset.still;
      image.src = running ? gif : image.dataset.still;
      reducedSource.media = 'not all';
      button.textContent = running ? 'Stop Animation' : 'Play Animation';
    }

    setRunning(!motion.matches);
    button.hidden = false;
    button.addEventListener('click', () => setRunning(!running));
    motion.addEventListener('change', event => setRunning(!event.matches));
  });

  document.querySelectorAll('.forecast-switch').forEach(switcher => {
    const buttons = [...switcher.querySelectorAll('[data-panel]')];
    function show(id) {
      buttons.forEach(button => {
        const selected = button.dataset.panel === id;
        button.setAttribute('aria-pressed', String(selected));
        document.getElementById(button.dataset.panel).hidden = !selected;
      });
    }
    show(buttons[0].dataset.panel);
    switcher.hidden = false;
    buttons.forEach(button => button.addEventListener('click', () => show(button.dataset.panel)));
  });
})();
