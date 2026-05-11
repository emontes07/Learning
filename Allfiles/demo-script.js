// ===== Shared Demo Page JS =====
// Used by all styled demo pages under Instructions/Demos/

function togglePart(bodyId, headerEl) {
  const body = document.getElementById(bodyId);
  const icon = headerEl.querySelector('.toggle-icon');
  body.classList.toggle('collapsed');
  icon.classList.toggle('open');
}

function copyPrompt(btn) {
  const box = btn.parentElement;
  const text = box.textContent.replace('Copy', '').replace('Copied!', '').trim();
  navigator.clipboard.writeText(text).then(() => {
    btn.textContent = 'Copied!';
    btn.classList.add('copied');
    setTimeout(() => {
      btn.textContent = 'Copy';
      btn.classList.remove('copied');
    }, 2000);
  });
}

function openSidebar() {
  document.getElementById('sidebar').classList.add('open');
  document.getElementById('sidebarOverlay').classList.add('open');
}
function closeSidebar() {
  document.getElementById('sidebar').classList.remove('open');
  document.getElementById('sidebarOverlay').classList.remove('open');
}

document.addEventListener('DOMContentLoaded', () => {
  // Close sidebar on link click (mobile)
  document.querySelectorAll('.sidebar a').forEach(link => {
    link.addEventListener('click', () => {
      if (window.innerWidth <= 900) closeSidebar();
    });
  });

  const sidebarLinks = document.querySelectorAll('.sidebar a[href^="#"]');
  const targets = [];
  sidebarLinks.forEach(link => {
    const id = link.getAttribute('href').substring(1);
    const el = document.getElementById(id);
    if (el) targets.push({ link, el });
  });

  // Auto-expand collapsed parts when their anchor is clicked
  sidebarLinks.forEach(link => {
    link.addEventListener('click', () => {
      const id = link.getAttribute('href').substring(1);
      const target = document.getElementById(id);
      if (!target) return;
      const partCard = target.closest('.part-card');
      if (partCard) {
        const bodyEl = partCard.querySelector('.part-body');
        if (bodyEl && bodyEl.classList.contains('collapsed')) {
          const header = partCard.querySelector('.part-header');
          togglePart(bodyEl.id, header);
        }
      }
    });
  });

  // Active link highlight on scroll
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.id;
        sidebarLinks.forEach(link => {
          link.classList.remove('active');
          if (link.getAttribute('href') === '#' + id) link.classList.add('active');
        });
      }
    });
  }, { threshold: 0.2, rootMargin: '-10% 0px -70% 0px' });
  targets.forEach(t => observer.observe(t.el));
});
