// Conference Website - Main JavaScript

document.addEventListener('DOMContentLoaded', function() {

    // ---------- Mobile Nav Toggle ----------
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('open');
        });

        // Close menu when clicking a link
        navMenu.querySelectorAll('a').forEach(function(link) {
            link.addEventListener('click', function() {
                navMenu.classList.remove('open');
            });
        });
    }

    // ---------- Schedule Tabs ----------
    const scheduleTabs = document.querySelectorAll('.schedule-tab');
    const schedulePanels = document.querySelectorAll('.schedule-panel');

    scheduleTabs.forEach(function(tab) {
        tab.addEventListener('click', function() {
            const target = this.getAttribute('data-day');

            scheduleTabs.forEach(function(t) { t.classList.remove('active'); });
            this.classList.add('active');

            schedulePanels.forEach(function(panel) {
                if (panel.getAttribute('data-day') === target) {
                    panel.style.display = 'block';
                } else {
                    panel.style.display = 'none';
                }
            });
        });
    });

    // ---------- Back to Top ----------
    const backToTop = document.querySelector('.back-to-top');

    if (backToTop) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 400) {
                backToTop.classList.add('visible');
            } else {
                backToTop.classList.remove('visible');
            }
        });

        backToTop.addEventListener('click', function() {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // ---------- Countdown Timer ----------
    const countdownEl = document.getElementById('countdown');
    if (countdownEl) {
        const targetDate = new Date(countdownEl.getAttribute('data-date')).getTime();

        function updateCountdown() {
            const now = new Date().getTime();
            const diff = targetDate - now;

            if (diff < 0) {
                countdownEl.innerHTML = '会议已开始';
                return;
            }

            const days = Math.floor(diff / (1000 * 60 * 60 * 24));
            const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));

            countdownEl.innerHTML = days + ' 天 ' + hours + ' 小时 ' + minutes + ' 分钟';
        }

        updateCountdown();
        setInterval(updateCountdown, 60000);
    }

    // ---------- Smooth Scroll for Anchor Links ----------
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#' || targetId === '') return;

            const target = document.querySelector(targetId);
            if (target) {
                e.preventDefault();
                const offset = 80;
                const targetPos = target.getBoundingClientRect().top + window.scrollY - offset;
                window.scrollTo({ top: targetPos, behavior: 'smooth' });
            }
        });
    });

    // ---------- Language Switch (placeholder) ----------
    const langSwitches = document.querySelectorAll('.lang-switch span');
    langSwitches.forEach(function(sw) {
        sw.addEventListener('click', function() {
            langSwitches.forEach(function(s) { s.classList.remove('active'); });
            this.classList.add('active');
        });
    });

});
