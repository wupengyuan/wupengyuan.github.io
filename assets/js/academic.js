(() => {
  const toggle = document.getElementById('color-theme-toggle');
  if (!toggle) return;
  const root = document.documentElement;
  const updateLabel = () => {
    const dark = root.getAttribute('data-theme') === 'dark';
    toggle.setAttribute('aria-label', dark ? 'Switch to light theme' : 'Switch to dark theme');
    toggle.setAttribute('aria-pressed', String(dark));
  };
  toggle.hidden = false;
  updateLabel();
  toggle.addEventListener('click', () => {
    const theme = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', theme);
    try { localStorage.setItem('academic-theme', theme); } catch (e) {}
    updateLabel();
  });
})();
