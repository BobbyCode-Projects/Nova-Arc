/**
 * Nova Arc - Main Interactive Script
 * Features:
 *  - Sticky Navbar & Mobile Drawer
 *  - Animated Metrics Counters (Intersection Observer)
 *  - AI Platform Interactive Console Switcher
 *  - Comprehensive Demo Request Form Validation & Feedback
 *  - Smooth In-Page Anchor Navigation
 */

function safeInit(name, fn) {
  try {
    fn();
  } catch (err) {
    console.warn(`[NovaArc] Init error for ${name}:`, err);
  }
}

function initAllComponents() {
  safeInit('MobileNavigation', initMobileNavigation);
  safeInit('StickyHeader', initStickyHeader);
  safeInit('ServicesMegaMenu', initServicesMegaMenu);
  safeInit('StatsCounter', initStatsCounter);
  safeInit('AITabs', initAITabs);
  safeInit('DemoForm', initDemoForm);
  safeInit('SmoothScroll', initSmoothScroll);
  safeInit('SolutionModals', initSolutionModals);
  safeInit('ServicesAccordions', initServicesAccordions);
  safeInit('CategoryPills', initCategoryPills);
  safeInit('ContactPageForm', initContactPageForm);
  safeInit('AnalyticsTracking', initAnalyticsTracking);
  safeInit('WaveformInteraction', initWaveformInteraction);
  safeInit('NavSimpleDropdowns', initNavSimpleDropdowns);
  safeInit('SiteSearchModal', initSiteSearchModal);
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initAllComponents);
} else {
  initAllComponents();
}

/* --------------------------------------------------------------------------
   1. Sticky Header
   -------------------------------------------------------------------------- */
function initStickyHeader() {
  const header = document.querySelector('.site-header');
  if (!header) return;

  const handleScroll = () => {
    if (window.scrollY > 30) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  };

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();
}

/* --------------------------------------------------------------------------
   Services Mega-Menu Dropdown (Desktop & Touch Click-to-Pin)
   -------------------------------------------------------------------------- */
function initServicesMegaMenu() {
  const toggleBtn = document.getElementById('servicesDropdownToggle');
  const megaPanel = document.getElementById('servicesMegaMenu');
  const navItem = toggleBtn ? toggleBtn.closest('.nav-item-dropdown') : null;

  if (!toggleBtn || !megaPanel) return;

  const openMenu = (pinned = false) => {
    megaPanel.classList.add('open');
    if (pinned) {
      megaPanel.classList.add('pinned');
      if (navItem) navItem.classList.add('pinned');
    }
    if (navItem) navItem.classList.add('open');
    toggleBtn.classList.add('active');
    toggleBtn.setAttribute('aria-expanded', 'true');
    megaPanel.setAttribute('aria-hidden', 'false');
  };

  const closeMenu = () => {
    megaPanel.classList.remove('open', 'pinned');
    if (navItem) navItem.classList.remove('open', 'pinned');
    toggleBtn.classList.remove('active');
    toggleBtn.setAttribute('aria-expanded', 'false');
    megaPanel.setAttribute('aria-hidden', 'true');
  };

  // 1. CLICK on the Services dropdown toggle (text or chevron):
  // Toggles the megamenu. When opened by click, IT STAYS PINNED until clicked outside!
  toggleBtn.addEventListener('click', (e) => {
    e.preventDefault();
    e.stopPropagation();

    // Close any other open dropdowns (Solutions, Tech, Industries)
    document.querySelectorAll('.nav-item-dropdown.open').forEach(p => {
      if (p !== navItem) {
        p.classList.remove('open');
        const link = p.querySelector('.nav-dropdown-link');
        if (link) link.setAttribute('aria-expanded', 'false');
      }
    });

    const isOpen = megaPanel.classList.contains('open') || megaPanel.classList.contains('pinned');
    if (isOpen) {
      closeMenu();
    } else {
      openMenu(true);
    }
  });

  // 2. DESKTOP HOVER:
  let hoverTimer = null;
  if (navItem) {
    navItem.addEventListener('mouseenter', () => {
      if (window.innerWidth >= 992) {
        if (hoverTimer) {
          clearTimeout(hoverTimer);
          hoverTimer = null;
        }
        // Close other simple dropdowns
        document.querySelectorAll('.nav-item-dropdown.open').forEach(p => {
          if (p !== navItem) {
            p.classList.remove('open');
            const link = p.querySelector('.nav-dropdown-link');
            if (link) link.setAttribute('aria-expanded', 'false');
          }
        });
        if (!megaPanel.classList.contains('pinned')) {
          openMenu(false);
        }
      }
    });

    navItem.addEventListener('mouseleave', () => {
      if (window.innerWidth >= 992) {
        // If pinned by click, it stays open!
        if (megaPanel.classList.contains('pinned')) return;
        hoverTimer = setTimeout(() => {
          if (!megaPanel.classList.contains('pinned')) {
            closeMenu();
          }
        }, 180);
      }
    });
  }

  megaPanel.addEventListener('mouseenter', () => {
    if (hoverTimer) {
      clearTimeout(hoverTimer);
      hoverTimer = null;
    }
  });

  megaPanel.addEventListener('mouseleave', () => {
    if (window.innerWidth >= 992) {
      if (megaPanel.classList.contains('pinned')) return;
      hoverTimer = setTimeout(() => {
        if (!megaPanel.classList.contains('pinned')) {
          closeMenu();
        }
      }, 180);
    }
  });

  // 3. CLICK ON CATEGORY OR LINK INSIDE THE MEGA MENU:
  megaPanel.addEventListener('click', (e) => {
    const link = e.target.closest('a');
    if (link) {
      closeMenu();
    }
  });

  // 4. CLICK ANYWHERE OUTSIDE TO DISMISS:
  document.addEventListener('click', (e) => {
    if (megaPanel.classList.contains('open') || megaPanel.classList.contains('pinned')) {
      const clickedInside = megaPanel.contains(e.target) || toggleBtn.contains(e.target);
      if (!clickedInside) {
        closeMenu();
      }
    }
  });

  // 5. ESCAPE KEY DISMISSAL:
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      if (megaPanel.classList.contains('open') || megaPanel.classList.contains('pinned')) {
        closeMenu();
        toggleBtn.focus();
      }
    }
  });
}

/* --------------------------------------------------------------------------
   2. Mobile Navigation Sidebar & Services Accordion
   -------------------------------------------------------------------------- */
function initMobileNavigation() {
  const toggleBtn = document.querySelector('.mobile-toggle');
  const drawer = document.querySelector('.mobile-nav-drawer') || document.querySelector('.mobile-nav');

  if (!toggleBtn || !drawer) return;

  // Move drawer to document.body to escape header backdrop-filter, sticky, and containing block bugs
  if (drawer.parentElement && drawer.parentElement !== document.body) {
    document.body.appendChild(drawer);
  }

  // Ensure high-z-index dark backdrop exists
  let backdrop = document.getElementById('mobileNavBackdrop');
  if (!backdrop) {
    backdrop = document.createElement('div');
    backdrop.id = 'mobileNavBackdrop';
    backdrop.className = 'mobile-nav-backdrop';
    backdrop.setAttribute('aria-hidden', 'true');
    document.body.appendChild(backdrop);
  }

  // Ensure drawer has a clean top header with brand and dedicated close button
  let drawerHeader = drawer.querySelector('.mobile-drawer-header');
  if (!drawerHeader) {
    drawerHeader = document.createElement('div');
    drawerHeader.className = 'mobile-drawer-header';
    drawerHeader.innerHTML = `
      <div class="mobile-drawer-brand">
        <span class="mobile-drawer-logo-text">Nova<strong>Arc</strong></span>
      </div>
      <button type="button" class="mobile-drawer-close" id="mobileDrawerCloseBtn" aria-label="Close navigation menu">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <line x1="18" y1="6" x2="6" y2="18"></line>
          <line x1="6" y1="6" x2="18" y2="18"></line>
        </svg>
      </button>
    `;
    drawer.insertBefore(drawerHeader, drawer.firstChild);
  }

  const closeBtn = document.getElementById('mobileDrawerCloseBtn');

  // Add "Explore All Services" link inside the services accordion if not already present
  const mobileServicesSubmenu = drawer.querySelector('#mobileServicesSubmenu');
  if (mobileServicesSubmenu && !mobileServicesSubmenu.querySelector('.mobile-all-services-link')) {
    const isSubdir = window.location.pathname.includes('/services/') || window.location.pathname.includes('/solutions/');
    const servicesPath = isSubdir ? '../services.html' : 'services.html';
    const overviewWrap = document.createElement('div');
    overviewWrap.className = 'mobile-submenu-overview-wrap';
    overviewWrap.innerHTML = `
      <a href="${servicesPath}" class="mobile-all-services-link">
        <span>Explore All Services</span>
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
      </a>
    `;
    mobileServicesSubmenu.insertBefore(overviewWrap, mobileServicesSubmenu.firstChild);
  }

  const openMenu = () => {
    drawer.classList.add('active');
    backdrop.classList.add('active');
    toggleBtn.classList.add('active');
    toggleBtn.setAttribute('aria-expanded', 'true');
    drawer.setAttribute('aria-hidden', 'false');
    document.body.classList.add('mobile-nav-open');
    toggleBtn.innerHTML = `
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <line x1="18" y1="6" x2="6" y2="18"></line>
        <line x1="6" y1="6" x2="18" y2="18"></line>
      </svg>
    `;
  };

  const closeMenu = () => {
    drawer.classList.remove('active');
    backdrop.classList.remove('active');
    toggleBtn.classList.remove('active');
    toggleBtn.setAttribute('aria-expanded', 'false');
    drawer.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('mobile-nav-open');
    toggleBtn.innerHTML = `
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <line x1="3" y1="12" x2="21" y2="12"></line>
        <line x1="3" y1="6" x2="21" y2="6"></line>
        <line x1="3" y1="18" x2="21" y2="18"></line>
      </svg>
    `;
  };

  // Helper for 0ms tap responsiveness on touchscreens + desktop click without ghost double-triggers
  let actionLock = false;
  const bindAction = (el, action) => {
    if (!el) return;
    const trigger = (e) => {
      if (e) {
        e.preventDefault();
        e.stopPropagation();
      }
      if (actionLock) return;
      actionLock = true;
      setTimeout(() => { actionLock = false; }, 260);
      action(e);
    };
    el.addEventListener('click', trigger);
    el.addEventListener('touchend', trigger);
  };

  const toggleMenu = () => {
    if (drawer.classList.contains('active')) {
      closeMenu();
    } else {
      openMenu();
    }
  };

  bindAction(toggleBtn, toggleMenu);
  if (closeBtn) bindAction(closeBtn, closeMenu);
  bindAction(backdrop, closeMenu);

  // Close on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && drawer.classList.contains('active')) {
      closeMenu();
      toggleBtn.focus();
    }
  });

  // Close when screen resizes to desktop width (>1024px)
  window.addEventListener('resize', () => {
    if (window.innerWidth > 1024 && drawer.classList.contains('active')) {
      closeMenu();
    }
  });

  // Handle iOS Safari back-forward cache (bfcache)
  window.addEventListener('pageshow', (event) => {
    if (event.persisted && drawer.classList.contains('active')) {
      closeMenu();
    }
  });

  // Navigation links inside drawer:
  // For in-page anchor links (e.g. href="#..."), close the drawer and let smooth scroll work.
  // For page navigation links, DO NOT close the drawer synchronously or disable pointer-events,
  // which cancels the browser's navigation request on iOS Safari.
  const navLinks = drawer.querySelectorAll(
    'a.mobile-nav-link, .mobile-submenu-link, .mobile-submenu-sublink, .mobile-category-title a, .mobile-nav-bottom a, .mobile-all-services-link, .mobile-overview-btn'
  );
  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      const href = link.getAttribute('href');
      if (href && href.startsWith('#')) {
        closeMenu();
      } else {
        setTimeout(() => {
          if (drawer.classList.contains('active')) {
            closeMenu();
          }
        }, 150);
      }
    });
  });

  // Mobile search trigger inside drawer
  const mobileSearchTrigger = drawer.querySelector('#mobileSearchTrigger');
  if (mobileSearchTrigger) {
    mobileSearchTrigger.addEventListener('click', () => {
      closeMenu();
    });
  }

  // Mobile accordion toggles for all submenus
  const mobileAccordionToggles = drawer.querySelectorAll('.mobile-accordion-toggle');
  mobileAccordionToggles.forEach(toggle => {
    const targetId = toggle.getAttribute('aria-controls');
    const submenu = targetId ? document.getElementById(targetId) : toggle.nextElementSibling;
    if (submenu) {
      bindAction(toggle, () => {
        const isOpen = submenu.classList.contains('open');
        if (isOpen) {
          submenu.classList.remove('open');
          toggle.classList.remove('open');
          toggle.setAttribute('aria-expanded', 'false');
          submenu.setAttribute('aria-hidden', 'true');
        } else {
          submenu.classList.add('open');
          toggle.classList.add('open');
          toggle.setAttribute('aria-expanded', 'true');
          submenu.setAttribute('aria-hidden', 'false');
        }
      });
    }
  });
}

/* --------------------------------------------------------------------------
   3. Animated Metric Counters (Continuous Roll with 5-Second Gap)
   -------------------------------------------------------------------------- */
function initStatsCounter() {
  const statNumbers = document.querySelectorAll('.stat-number');
  const statsSection = document.querySelector('.stats-section');
  if (!statNumbers.length) return;

  let loopTimeout = null;
  let isSectionInView = false;
  let isRolling = false;
  let activeFrameIds = [];

  const animateValue = (element, start, end, duration, decimals = 0, onComplete) => {
    let startTimestamp = null;

    const step = (timestamp) => {
      if (!startTimestamp) startTimestamp = timestamp;
      const progress = Math.min((timestamp - startTimestamp) / duration, 1);
      // Smooth cubic ease-out for energetic roll decelerating into final value
      const ease = 1 - Math.pow(1 - progress, 3);
      const current = start + (end - start) * ease;
      element.textContent = decimals > 0 ? current.toFixed(decimals) : Math.floor(current);

      if (progress < 1) {
        const frameId = window.requestAnimationFrame(step);
        activeFrameIds.push(frameId);
      } else {
        element.textContent = decimals > 0 ? end.toFixed(decimals) : end;
        if (typeof onComplete === 'function') {
          onComplete();
        }
      }
    };

    const frameId = window.requestAnimationFrame(step);
    activeFrameIds.push(frameId);
  };

  const startRollingCycle = () => {
    if (isRolling) return;
    isRolling = true;

    if (loopTimeout) {
      clearTimeout(loopTimeout);
      loopTimeout = null;
    }

    // Cancel any still-running frames before starting fresh
    activeFrameIds.forEach(id => window.cancelAnimationFrame(id));
    activeFrameIds = [];

    let completedCount = 0;
    const totalCount = statNumbers.length;

    statNumbers.forEach(statEl => {
      const target = parseFloat(statEl.getAttribute('data-target'));
      const decimals = parseInt(statEl.getAttribute('data-decimals') || '0', 10);
      if (!isNaN(target)) {
        animateValue(statEl, 0, target, 1600, decimals, () => {
          completedCount++;
          if (completedCount === totalCount) {
            isRolling = false;
            // 5 seconds gap before triggering the next roll
            loopTimeout = setTimeout(() => {
              if (isSectionInView && !document.hidden) {
                startRollingCycle();
              }
            }, 5000);
          }
        });
      } else {
        completedCount++;
      }
    });
  };

  // Observe visibility in viewport
  if ('IntersectionObserver' in window && statsSection) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          isSectionInView = true;
          if (!isRolling && !loopTimeout) {
            startRollingCycle();
          }
        } else {
          isSectionInView = false;
          if (loopTimeout) {
            clearTimeout(loopTimeout);
            loopTimeout = null;
          }
        }
      });
    }, { threshold: 0.1 });

    observer.observe(statsSection);
  } else {
    // Fallback if IntersectionObserver is unavailable or section not found
    isSectionInView = true;
    startRollingCycle();
  }

  // Pause when browser tab is inactive, resume when active
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
      if (loopTimeout) {
        clearTimeout(loopTimeout);
        loopTimeout = null;
      }
    } else if (isSectionInView && !isRolling && !loopTimeout) {
      startRollingCycle();
    }
  });
}


/* --------------------------------------------------------------------------
   4. Nova Arc AI Platform Tab Switcher
   -------------------------------------------------------------------------- */
function initAITabs() {
  const tabButtons = document.querySelectorAll('.ai-tab-btn');
  const tabPanels = document.querySelectorAll('.ai-tab-content-panel');

  if (!tabButtons.length || !tabPanels.length) return;

  tabButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.getAttribute('data-tab');

      // Update button active state
      tabButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      // Update panel visibility
      tabPanels.forEach(panel => {
        if (panel.id === targetId) {
          panel.classList.add('active');
        } else {
          panel.classList.remove('active');
        }
      });
    });
  });
}

/* --------------------------------------------------------------------------
   5. Demo Request Form Validation & Feedback
   -------------------------------------------------------------------------- */
function initDemoForm() {
  const form = document.getElementById('demo-request-form');
  const successBox = document.getElementById('form-success-box');
  const resetBtn = document.getElementById('reset-form-btn');
  if (!form) return;

  const fields = {
    name: {
      el: document.getElementById('demo-name'),
      err: document.getElementById('error-name'),
      validate: (val) => val.trim().length >= 2,
      msg: 'Please enter your full name.'
    },
    email: {
      el: document.getElementById('demo-email'),
      err: document.getElementById('error-email'),
      validate: (val) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val.trim()),
      msg: 'Please provide a valid work email address.'
    },
    phone: {
      el: document.getElementById('demo-phone'),
      err: document.getElementById('error-phone'),
      validate: (val) => val.replace(/[^0-9]/g, '').length >= 10,
      msg: 'Please enter a valid 10-digit phone number.'
    },
    company: {
      el: document.getElementById('demo-company'),
      err: document.getElementById('error-company'),
      validate: (val) => val.trim().length >= 2,
      msg: 'Please specify your company or organization.'
    },
    domain: {
      el: document.getElementById('demo-domain'),
      err: document.getElementById('error-domain'),
      validate: (val) => val.trim() !== '',
      msg: 'Please select a service domain.'
    }
  };

  // Real-time error clearance on input
  Object.keys(fields).forEach(key => {
    const item = fields[key];
    if (item.el) {
      const eventName = item.el.tagName === 'SELECT' ? 'change' : 'input';
      item.el.addEventListener(eventName, () => {
        if (item.validate(item.el.value)) {
          item.el.classList.remove('error');
          if (item.err) item.err.classList.remove('visible');
        }
      });
    }
  });

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    let isValid = true;
    let firstErrorField = null;

    Object.keys(fields).forEach(key => {
      const item = fields[key];
      if (!item.el) return;

      const val = item.el.value;
      if (!item.validate(val)) {
        isValid = false;
        item.el.classList.add('error');
        if (item.err) {
          item.err.textContent = item.msg;
          item.err.classList.add('visible');
        }
        if (!firstErrorField) firstErrorField = item.el;
      } else {
        item.el.classList.remove('error');
        if (item.err) item.err.classList.remove('visible');
      }
    });

    if (!isValid) {
      if (firstErrorField) firstErrorField.focus();
      return;
    }

    // Submit Simulation
    const submitBtn = form.querySelector('.btn-submit-demo');
    const originalText = submitBtn.innerHTML;
    submitBtn.disabled = true;
    submitBtn.innerHTML = `
      <svg class="spin-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="12" cy="12" r="10" stroke-opacity="0.25"></circle>
        <path d="M12 2a10 10 0 0 1 10 10" stroke-linecap="round"></path>
      </svg>
      Sending Inquiry...
    `;

    setTimeout(() => {
      const applicantName = fields.name.el ? fields.name.el.value.trim() : '';
      const applicantOrg = fields.company.el ? fields.company.el.value.trim() : '';
      const applicantEmail = fields.email.el ? fields.email.el.value.trim() : '';
      const applicantPhone = fields.phone.el ? fields.phone.el.value.trim() : '';
      const applicantDomain = fields.domain.el ? fields.domain.el.value : '';
      const messageEl = document.getElementById('demo-message');
      const applicantMessage = messageEl ? messageEl.value.trim() : '';

      // Save submission to persistent storage
      const record = saveSubmission('demo', {
        name: applicantName,
        email: applicantEmail,
        phone: applicantPhone,
        domain: applicantDomain,
        requirements: applicantMessage,
        company: applicantOrg,
        source: 'Homepage Project Discussion Form'
      });

      // Populate success card details
      const confirmedName = document.getElementById('confirmed-name');
      const confirmedOrg = document.getElementById('confirmed-org');
      if (confirmedName) confirmedName.textContent = applicantName;
      if (confirmedOrg) confirmedOrg.textContent = applicantOrg;

      form.style.display = 'none';
      if (successBox) successBox.classList.add('active');

      submitBtn.disabled = false;
      submitBtn.innerHTML = originalText;
    }, 1000);
  });

  if (resetBtn) {
    resetBtn.addEventListener('click', () => {
      form.reset();
      Object.keys(fields).forEach(key => {
        const item = fields[key];
        if (item.el) item.el.classList.remove('error');
        if (item.err) item.err.classList.remove('visible');
      });
      if (successBox) successBox.classList.remove('active');
      form.style.display = 'flex';
    });
  }
}

/* --------------------------------------------------------------------------
   6. Smooth Anchor Navigation with Offset
   -------------------------------------------------------------------------- */
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href === '#' || href === '') return;

      const target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        const headerHeight = document.querySelector('.site-header')?.offsetHeight || 70;
        const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - (headerHeight + 16);

        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });
      }
    });
  });
}

/* --------------------------------------------------------------------------
   7. Solution Areas Modal Dialogs
   -------------------------------------------------------------------------- */
function initSolutionModals() {
  const triggers = document.querySelectorAll('[data-modal-target]');
  const overlays = document.querySelectorAll('.modal-overlay');

  if (!triggers.length && !overlays.length) return;

  const openModal = (modalId) => {
    const targetModal = document.getElementById(modalId);
    if (targetModal) {
      targetModal.classList.add('active');
      document.body.style.overflow = 'hidden';
    }
  };

  const closeModal = (modal) => {
    modal.classList.remove('active');
    // Only restore scroll if no other modals or mobile drawer active
    const activeModals = document.querySelectorAll('.modal-overlay.active');
    if (activeModals.length === 0) {
      document.body.style.overflow = '';
    }
  };

  triggers.forEach(trigger => {
    trigger.addEventListener('click', (e) => {
      e.preventDefault();
      const modalId = trigger.getAttribute('data-modal-target');
      if (modalId) {
        openModal(modalId);
      }
    });
  });

  overlays.forEach(overlay => {
    // Backdrop click
    overlay.addEventListener('click', (e) => {
      if (e.target === overlay) {
        closeModal(overlay);
      }
    });

    // Close button click
    const closeBtns = overlay.querySelectorAll('.modal-close-btn, [data-modal-close]');
    closeBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        closeModal(overlay);
      });
    });
  });

  // ESC key to close active modal
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      const activeModal = document.querySelector('.modal-overlay.active');
      if (activeModal) {
        closeModal(activeModal);
      }
    }
  });
}

/* --------------------------------------------------------------------------
   8. Services Category Accordions
   -------------------------------------------------------------------------- */
function initServicesAccordions() {
  const headers = document.querySelectorAll('.service-accordion-header');
  if (!headers.length) return;

  headers.forEach(header => {
    header.addEventListener('click', () => {
      const item = header.closest('.service-accordion-item');
      if (!item) return;

      const isOpen = item.classList.contains('open');
      const isExpanded = header.getAttribute('aria-expanded') === 'true';

      if (isOpen) {
        item.classList.remove('open');
        header.setAttribute('aria-expanded', 'false');
      } else {
        item.classList.add('open');
        header.setAttribute('aria-expanded', 'true');
      }
    });
  });
}

/* --------------------------------------------------------------------------
   9. Category Navigation Pill Links Active State
   -------------------------------------------------------------------------- */
function initCategoryPills() {
  const pillContainers = document.querySelectorAll('.services-category-nav');
  pillContainers.forEach(container => {
    const pills = container.querySelectorAll('.category-pill-link');
    pills.forEach(pill => {
      pill.addEventListener('click', () => {
        pills.forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
      });
    });
  });
}

/* --------------------------------------------------------------------------
   10. Contact Page Form Validation & Handling
   -------------------------------------------------------------------------- */
function initContactPageForm() {
  const form = document.getElementById('contact-page-form');
  const successBox = document.getElementById('contact-success-box');
  const resetBtn = document.getElementById('reset-contact-form-btn');
  if (!form) return;

  // Pre-fill from URL query param (e.g. ?service=claims-management-scrubbing)
  try {
    const urlParams = new URLSearchParams(window.location.search);
    const serviceParam = urlParams.get('service');
    if (serviceParam) {
      const interestSelect = document.getElementById('contact-interest');
      const messageField = document.getElementById('contact-message');
      
      const serviceNameMap = {
        'commerce': 'Digital Commerce & Supply Chain',
        'enterprise': 'Enterprise Business Solutions',
        'monitoring': 'Intelligent Monitoring & Automation',
        'ai-healthcare': 'AI & Healthcare Technology',
        'commerce-platforms': 'Digital Commerce Platforms',
        'foodtech': 'FoodTech Solutions',
        'supply-chain': 'Supply Chain Management',
        'procurement': 'Procurement & Vendor Management',
        'logistics': 'Logistics & Distribution',
        'crm': 'Customer Relationship Management (CRM)',
        'hrms': 'Human Resource Management Systems (HRMS)',
        'bpa': 'Business Process Automation',
        'enterprise-apps': 'Enterprise Application Development',
        'system-integration': 'System Integration & Data Connectivity',
        'real-time-monitoring': 'Real-Time Monitoring',
        'iot': 'Internet of Things (IoT) Solutions',
        'operational-analytics': 'Operational Analytics',
        'workflow-automation': 'Intelligent Workflow Automation',
        'infra-monitoring': 'System & Infrastructure Monitoring',
        'agentic-ai': 'Agentic AI & Intelligent Agents',
        'gen-ai': 'Generative AI Applications',
        'intelligent-automation': 'Intelligent Business Automation',
        'healthcare-tech': 'Healthcare Technology Solutions',
        'ai-governance': 'AI Integration & Governance',
        'multiple': 'Multiple Services',
        'other': 'Other Inquiries'
      };
      
      const serviceDisplayName = serviceNameMap[serviceParam] || serviceParam.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase());

      if (interestSelect) {
        let matchingOption = Array.from(interestSelect.options).find(opt => opt.value === serviceParam);
        if (!matchingOption) {
          matchingOption = document.createElement('option');
          matchingOption.value = serviceParam;
          matchingOption.textContent = `Service: ${serviceDisplayName}`;
          interestSelect.appendChild(matchingOption);
        }
        matchingOption.selected = true;
      }

      if (messageField && !messageField.value.trim()) {
        messageField.value = `Hello Nova Arc team, I would like to discuss our project requirements for ${serviceDisplayName}. Please connect with us to review technical specifications and solution architecture.`;
      }
    }
  } catch (e) {
    console.warn('[Nova Arc] Failed to parse URL parameters for contact form:', e);
  }

  const fields = {
    name: {
      el: document.getElementById('contact-name'),
      err: document.getElementById('error-contact-name'),
      validate: (val) => val.trim().length >= 2,
      msg: 'Please enter your full name.'
    },
    email: {
      el: document.getElementById('contact-email'),
      err: document.getElementById('error-contact-email'),
      validate: (val) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val.trim()),
      msg: 'Please provide a valid work email address.'
    },
    phone: {
      el: document.getElementById('contact-phone'),
      err: document.getElementById('error-contact-phone'),
      validate: (val) => val.replace(/[^0-9]/g, '').length >= 10,
      msg: 'Please enter a valid 10-digit phone number.'
    },
    state: {
      el: document.getElementById('contact-state'),
      err: document.getElementById('error-contact-state'),
      validate: (val) => val.trim() !== '',
      msg: 'Please select your state.'
    },
    title: {
      el: document.getElementById('contact-title'),
      err: document.getElementById('error-contact-title'),
      validate: (val) => val.trim().length >= 2,
      msg: 'Please enter your job title.'
    },
    company: {
      el: document.getElementById('contact-company'),
      err: document.getElementById('error-contact-company'),
      validate: (val) => val.trim().length >= 2,
      msg: 'Please enter your company or organization name.'
    },
    interest: {
      el: document.getElementById('contact-interest'),
      err: document.getElementById('error-contact-interest'),
      validate: (val) => val.trim() !== '',
      msg: 'Please select what you are interested in.'
    },
    message: {
      el: document.getElementById('contact-message'),
      err: document.getElementById('error-contact-message'),
      validate: (val) => val.trim().length >= 10,
      msg: 'Please provide a message (at least 10 characters).'
    }
  };

  // Real-time error removal
  Object.keys(fields).forEach(key => {
    const item = fields[key];
    if (item.el) {
      const eventType = item.el.tagName === 'SELECT' ? 'change' : 'input';
      item.el.addEventListener(eventType, () => {
        if (item.validate(item.el.value)) {
          item.el.classList.remove('error');
          if (item.err) item.err.classList.remove('visible');
        }
      });
    }
  });

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    let isValid = true;
    let firstErrorField = null;

    Object.keys(fields).forEach(key => {
      const item = fields[key];
      if (!item.el) return;

      const val = item.el.value;
      if (!item.validate(val)) {
        isValid = false;
        item.el.classList.add('error');
        if (item.err) {
          item.err.textContent = item.msg;
          item.err.classList.add('visible');
        }
        if (!firstErrorField) firstErrorField = item.el;
      } else {
        item.el.classList.remove('error');
        if (item.err) item.err.classList.remove('visible');
      }
    });

    if (!isValid) {
      if (firstErrorField) firstErrorField.focus();
      return;
    }

    const submitBtn = document.getElementById('btn-submit-contact');
    const originalText = submitBtn.innerHTML;
    submitBtn.disabled = true;
    submitBtn.innerHTML = `
      <svg class="spin-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="12" cy="12" r="10" stroke-opacity="0.25"></circle>
        <path d="M12 2a10 10 0 0 1 10 10" stroke-linecap="round"></path>
      </svg>
      Sending Message...
    `;

    setTimeout(() => {
      const applicantName = fields.name.el.value.trim();
      const applicantOrg = fields.company.el.value.trim();
      const applicantEmail = fields.email.el.value.trim();
      const applicantPhone = fields.phone.el.value.trim();
      const applicantState = fields.state.el.value;
      const applicantTitle = fields.title.el.value.trim();
      const interestSelect = fields.interest.el;
      const interestText = interestSelect.options[interestSelect.selectedIndex]?.text || fields.interest.el.value;
      const applicantMessage = fields.message.el.value.trim();

      // Save submission to persistent storage
      const record = saveSubmission('contact', {
        name: applicantName,
        email: applicantEmail,
        phone: applicantPhone,
        state: applicantState,
        title: applicantTitle,
        company: applicantOrg,
        interest: fields.interest.el.value,
        interestText: interestText,
        message: applicantMessage,
        source: 'Dedicated Contact & Inquiry Page'
      });

      const confirmedName = document.getElementById('confirmed-contact-name');
      const confirmedOrg = document.getElementById('confirmed-contact-org');
      const confirmedEmail = document.getElementById('confirmed-contact-email');
      const confirmedInterest = document.getElementById('confirmed-contact-interest');

      if (confirmedName) confirmedName.textContent = applicantName;
      if (confirmedOrg) confirmedOrg.textContent = applicantOrg;
      if (confirmedEmail) confirmedEmail.textContent = applicantEmail;
      if (confirmedInterest) confirmedInterest.textContent = interestText;

      form.style.display = 'none';
      if (successBox) {
        successBox.style.display = 'flex';
        successBox.classList.add('active');
      }

      submitBtn.disabled = false;
      submitBtn.innerHTML = originalText;
    }, 700);
  });

  if (resetBtn) {
    resetBtn.addEventListener('click', () => {
      form.reset();
      Object.keys(fields).forEach(key => {
        const item = fields[key];
        if (item.el) item.el.classList.remove('error');
        if (item.err) item.err.classList.remove('visible');
      });
      if (successBox) {
        successBox.style.display = 'none';
        successBox.classList.remove('active');
      }
      form.style.display = 'flex';
    });
  }
}

/* --------------------------------------------------------------------------
   11. Submission Persistence & CRM Storage
   -------------------------------------------------------------------------- */
function saveSubmission(type, data) {
  try {
    const key = 'novaarc_submissions';
    const existing = JSON.parse(localStorage.getItem(key) || '[]');
    const record = {
      id: 'NA-' + Date.now().toString(36).toUpperCase(),
      type: type, // 'contact' or 'demo'
      timestamp: new Date().toISOString(),
      url: window.location.href,
      status: 'received',
      data: data
    };
    existing.unshift(record);
    localStorage.setItem(key, JSON.stringify(existing));

    // Custom DOM Event for integrations
    window.dispatchEvent(new CustomEvent('novaarc:submission', { detail: record }));

    console.info(`[Nova Arc CRM] Submission stored successfully [ID: ${record.id}]`, record);

    // Track in GA4 if initialized
    if (typeof window.gtag === 'function') {
      window.gtag('event', 'generate_lead', {
        event_category: 'Leads',
        event_label: type === 'demo' ? 'Homepage Demo Request' : `Contact Inquiry: ${data.interest || 'General'}`,
        lead_id: record.id,
        value: 1
      });
    }
    return record;
  } catch (err) {
    console.warn('[Nova Arc CRM] Failed to write to localStorage:', err);
    return null;
  }
}

/* --------------------------------------------------------------------------
   12. Analytics & Event Tracking (GA4 & User Actions)
   -------------------------------------------------------------------------- */
function initAnalyticsTracking() {
  // Track phone calls
  document.querySelectorAll('a[href^="tel:"]').forEach(link => {
    link.addEventListener('click', () => {
      const phoneNumber = link.getAttribute('href').replace('tel:', '');
      if (typeof window.gtag === 'function') {
        window.gtag('event', 'click_to_call', {
          event_category: 'Direct Channel',
          event_label: phoneNumber
        });
      }
      console.info(`[Nova Arc Analytics] Direct phone call clicked: ${phoneNumber}`);
    });
  });

  // Track email clicks
  document.querySelectorAll('a[href^="mailto:"]').forEach(link => {
    link.addEventListener('click', () => {
      const email = link.getAttribute('href').replace('mailto:', '');
      if (typeof window.gtag === 'function') {
        window.gtag('event', 'click_to_email', {
          event_category: 'Direct Channel',
          event_label: email
        });
      }
      console.info(`[Nova Arc Analytics] Direct email clicked: ${email}`);
    });
  });

  // Track primary CTA demo clicks
  document.querySelectorAll('.btn-primary, .btn-submit-demo').forEach(btn => {
    if (btn.tagName === 'A' && btn.getAttribute('href')?.includes('contact.html')) {
      btn.addEventListener('click', () => {
        if (typeof window.gtag === 'function') {
          window.gtag('event', 'cta_click', {
            event_category: 'Conversion',
            event_label: btn.textContent.trim()
          });
        }
      });
    }
  });
}

/* --------------------------------------------------------------------------
   13. Global Developer & Admin Utility API
   -------------------------------------------------------------------------- */
window.NovaArc = {
  getSubmissions() {
    try {
      return JSON.parse(localStorage.getItem('novaarc_submissions') || '[]');
    } catch {
      return [];
    }
  },
  clearSubmissions() {
    localStorage.removeItem('novaarc_submissions');
    console.info('[Nova Arc CRM] All stored submissions have been cleared.');
  },
  exportSubmissions() {
    const data = this.getSubmissions();
    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `novaarc_leads_${new Date().toISOString().slice(0,10)}.json`;
    a.click();
    URL.revokeObjectURL(url);
    console.info(`[Nova Arc CRM] Exported ${data.length} submissions.`);
  },
  getStats() {
    const list = this.getSubmissions();
    return {
      total: list.length,
      demoRequests: list.filter(item => item.type === 'demo').length,
      contactInquiries: list.filter(item => item.type === 'contact').length,
      latest: list[0] || null
    };
  }
};

/* --------------------------------------------------------------------------
   14. Orchestration Waveform Interactive Ripple
   -------------------------------------------------------------------------- */
function initWaveformInteraction() {
  const hero = document.querySelector('.hero-orchestrated');
  if (!hero) return;

  const tracks = hero.querySelectorAll('.ecg-waveform-track');
  if (!tracks.length) return;

  let ticking = false;
  hero.addEventListener('mousemove', (e) => {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      const mouseY = e.clientY;

      tracks.forEach(track => {
        const bRect = track.getBoundingClientRect();
        const dist = Math.abs(bRect.top + bRect.height / 2 - mouseY);
        const signalPaths = track.querySelectorAll('.ecg-path-signal');
        
        signalPaths.forEach(signal => {
          if (dist < 100) {
            const intensity = 1 - dist / 100;
            signal.style.filter = `drop-shadow(0 0 ${6 + intensity * 8}px #38BDF8) drop-shadow(0 0 ${14 + intensity * 14}px rgba(31, 111, 235, 0.9))`;
            signal.style.stroke = '#7DD3FC';
          } else {
            signal.style.filter = '';
            signal.style.stroke = '';
          }
        });
      });
      ticking = false;
    });
  });

  hero.addEventListener('mouseleave', () => {
    tracks.forEach(track => {
      const signalPaths = track.querySelectorAll('.ecg-path-signal');
      signalPaths.forEach(signal => {
        signal.style.filter = '';
        signal.style.stroke = '';
      });
    });
  });
}

/* --------------------------------------------------------------------------
   Simple Dropdown Toggles (Solutions, Technology, Industries)
   -------------------------------------------------------------------------- */
function initNavSimpleDropdowns() {
  const toggles = document.querySelectorAll('.nav-dropdown-link:not(#servicesDropdownToggle)');

  const closeServicesIfOpen = () => {
    const servicesMega = document.getElementById('servicesMegaMenu');
    if (servicesMega && (servicesMega.classList.contains('open') || servicesMega.classList.contains('pinned'))) {
      servicesMega.classList.remove('open', 'pinned');
      servicesMega.setAttribute('aria-hidden', 'true');
      const servicesToggle = document.getElementById('servicesDropdownToggle');
      if (servicesToggle) {
        servicesToggle.classList.remove('active');
        servicesToggle.setAttribute('aria-expanded', 'false');
      }
      const servicesItem = document.querySelector('.nav-item-services');
      if (servicesItem) servicesItem.classList.remove('open', 'pinned');
    }
  };

  toggles.forEach(toggle => {
    const parent = toggle.closest('.nav-item-dropdown');
    if (!parent) return;

    // Chevron click toggles dropdown open/close on desktop & mobile
    toggle.addEventListener('click', (e) => {
      const isChevron = e.target.closest('.dropdown-chevron');
      if (isChevron) {
        e.preventDefault();
        e.stopPropagation();
        closeServicesIfOpen();
        const isOpen = parent.classList.contains('open');
        // Close other simple dropdowns
        document.querySelectorAll('.nav-item-dropdown.open').forEach(p => {
          if (p !== parent) {
            p.classList.remove('open');
            const link = p.querySelector('.nav-dropdown-link');
            if (link) link.setAttribute('aria-expanded', 'false');
          }
        });
        if (isOpen) {
          parent.classList.remove('open');
          toggle.setAttribute('aria-expanded', 'false');
        } else {
          parent.classList.add('open');
          toggle.setAttribute('aria-expanded', 'true');
        }
      }
    });

    // Desktop hover: add open class on mouseenter, remove on mouseleave
    parent.addEventListener('mouseenter', () => {
      if (window.innerWidth >= 992) {
        closeServicesIfOpen();
        document.querySelectorAll('.nav-item-dropdown.open').forEach(p => {
          if (p !== parent) {
            p.classList.remove('open');
            const link = p.querySelector('.nav-dropdown-link');
            if (link) link.setAttribute('aria-expanded', 'false');
          }
        });
        parent.classList.add('open');
        toggle.setAttribute('aria-expanded', 'true');
      }
    });

    parent.addEventListener('mouseleave', () => {
      if (window.innerWidth >= 992) {
        parent.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  });

  // Close open dropdowns when clicking outside
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.nav-item-dropdown')) {
      document.querySelectorAll('.nav-item-dropdown.open').forEach(p => {
        p.classList.remove('open');
        const link = p.querySelector('.nav-dropdown-link');
        if (link) link.setAttribute('aria-expanded', 'false');
      });
    }
  });

  // Close open dropdowns when clicking any item inside a dropdown
  document.querySelectorAll('.nav-simple-item').forEach(item => {
    item.addEventListener('click', () => {
      document.querySelectorAll('.nav-item-dropdown.open').forEach(p => {
        p.classList.remove('open');
        const link = p.querySelector('.nav-dropdown-link');
        if (link) link.setAttribute('aria-expanded', 'false');
      });
    });
  });

  // Close open dropdowns on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      document.querySelectorAll('.nav-item-dropdown.open').forEach(p => {
        p.classList.remove('open');
        const link = p.querySelector('.nav-dropdown-link');
        if (link) link.setAttribute('aria-expanded', 'false');
      });
    }
  });
}

/* --------------------------------------------------------------------------
   Site Search Modal (Instant Client-Side Search Across All Pages & Services)
   -------------------------------------------------------------------------- */
function initSiteSearchModal() {
  let backdrop = document.getElementById('siteSearchModalBackdrop');
  if (!backdrop) {
    backdrop = document.createElement('div');
    backdrop.id = 'siteSearchModalBackdrop';
    backdrop.className = 'site-search-modal-backdrop';
    backdrop.setAttribute('aria-hidden', 'true');
    backdrop.setAttribute('role', 'dialog');
    backdrop.setAttribute('aria-modal', 'true');
    backdrop.setAttribute('aria-label', 'Site Search');

    backdrop.innerHTML = `
      <div class="site-search-modal">
        <div class="site-search-header">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
          <input type="text" class="site-search-input" id="siteSearchInput" placeholder="Search services, solutions, IoT, AI, commerce..." autocomplete="off">
        </div>
        <div class="site-search-body">
          <div id="siteSearchDefaultView">
            <div class="site-search-section-title">Quick Suggestions</div>
            <div class="site-search-tags">
              <button type="button" class="site-search-tag" data-query="Commerce">Digital Commerce</button>
              <button type="button" class="site-search-tag" data-query="Supply Chain">Supply Chain</button>
              <button type="button" class="site-search-tag" data-query="CRM">CRM &amp; HRMS</button>
              <button type="button" class="site-search-tag" data-query="Automation">Intelligent Automation</button>
              <button type="button" class="site-search-tag" data-query="Monitoring">IoT &amp; Monitoring</button>
              <button type="button" class="site-search-tag" data-query="AI">Agentic AI</button>
              <button type="button" class="site-search-tag" data-query="Healthcare">Healthcare Tech</button>
            </div>
            <div class="site-search-section-title">Featured Services</div>
          </div>
          <ul class="site-search-results" id="siteSearchResultsList"></ul>
        </div>
      </div>
    `;
    document.body.appendChild(backdrop);
  }

  const isSubDir = window.location.pathname.includes('/services/') ||
                   window.location.pathname.includes('/solutions/') ||
                   window.location.pathname.includes('/technology/') ||
                   window.location.pathname.includes('/industries/') ||
                   window.location.pathname.includes('/connect/');
  const rootPrefix = isSubDir ? '../' : '';

  const searchIndex = [
    {
      title: 'Nova Arc Homepage',
      category: 'Main Navigation',
      desc: 'Engineering intelligent solutions for a connected business world. Digital commerce, enterprise systems, and AI automation.',
      url: rootPrefix + 'index.html',
      tags: ['home', 'overview', 'nova arc', 'engineering', 'solutions']
    },
    {
      title: 'All Solutions Overview',
      category: 'Solutions',
      desc: 'Unified architecture combining commerce, enterprise systems, intelligent monitoring, and AI automation.',
      url: rootPrefix + 'solutions.html',
      tags: ['solutions', 'overview', 'enterprise solutions', 'digital commerce', 'supply chain', 'monitoring']
    },
    {
      title: 'Full Services Catalog',
      category: 'Services',
      desc: 'Complete engineering services across 4 core domains: Digital Commerce, Enterprise, Monitoring, and AI.',
      url: rootPrefix + 'services.html',
      tags: ['services', 'catalog', 'engineering', 'consulting', 'capabilities']
    },
    {
      title: 'Technology Platform & Architecture',
      category: 'Technology',
      desc: 'Agentic AI, IoT telemetry, real-time analytics, and enterprise data integration architecture.',
      url: rootPrefix + 'technology.html',
      tags: ['technology', 'platform', 'ai', 'iot', 'architecture', 'data', 'analytics']
    },
    {
      title: 'Industries We Serve',
      category: 'Industries',
      desc: 'Specialized technology solutions for FoodTech, Retail Commerce, Manufacturing, Logistics, and Healthcare.',
      url: rootPrefix + 'industries.html',
      tags: ['industries', 'foodtech', 'retail', 'manufacturing', 'logistics', 'healthcare']
    },
    {
      title: 'Connect With Us & Directory',
      category: 'Contact',
      desc: 'Get in touch with Nova Arc. Hyderabad headquarters, direct departmental emails, and phone contact.',
      url: rootPrefix + 'contact.html',
      tags: ['contact', 'connect', 'phone', 'email', 'hyderabad', 'support', 'sales']
    },
    {
      title: 'Digital Commerce Solutions',
      category: 'Connected Digital Solutions',
      desc: 'End-to-end B2B and B2C commerce architectures engineered for rapid digital ordering, customer engagement, dynamic pricing, and ...',
      url: rootPrefix + 'solutions/digital-commerce.html',
      tags: ['digital', 'commerce', 'solutions', 'platforms', 'ordering', 'customer', 'portals']
    },
    {
      title: 'Supply Chain & Procurement Solutions',
      category: 'Connected Digital Solutions',
      desc: 'End-to-end supply chain visibility, intelligent warehouse coordination, automated purchase requisitions, and vendor collaborati...',
      url: rootPrefix + 'solutions/supply-chain.html',
      tags: ['supply', 'chain', 'procurement', 'solutions', 'end', 'visibility', 'digital', 'vendor', 'portals']
    },
    {
      title: 'Enterprise Business Solutions',
      category: 'Connected Digital Solutions',
      desc: 'Modernize core operations with synchronized CRM, HRMS, custom business applications, and automated cross-departmental workflows.',
      url: rootPrefix + 'solutions/enterprise-business.html',
      tags: ['enterprise', 'business', 'solutions', 'customer', 'relationship', 'management', 'crm', 'human', 'resource', 'hrms']
    },
    {
      title: 'Intelligent Monitoring Solutions',
      category: 'Connected Digital Solutions',
      desc: 'Real-time IoT sensor telemetry, low-latency operational dashboards, threshold alerting, and automated incident escalation workf...',
      url: rootPrefix + 'solutions/intelligent-monitoring.html',
      tags: ['intelligent', 'monitoring', 'solutions', 'real', 'time', 'operational', 'dashboards', 'iot', 'device', 'sensor']
    },
    {
      title: 'AI & Agentic Automation Solutions',
      category: 'Connected Digital Solutions',
      desc: 'Apply agentic AI workflows, generative enterprise assistants, intelligent document extraction, and governed business automation.',
      url: rootPrefix + 'solutions/ai-automation.html',
      tags: ['agentic', 'automation', 'solutions', 'multi', 'step', 'orchestration', 'generative', 'enterprise', 'assistants']
    },
    {
      title: 'Healthcare Technology Solutions',
      category: 'Connected Digital Solutions',
      desc: 'Administrative workflow automation, digital patient intake, scheduling coordination, healthcare document processing, and secure...',
      url: rootPrefix + 'solutions/healthcare-technology.html',
      tags: ['healthcare', 'technology', 'solutions', 'digital', 'patient', 'intake', 'registration', 'scheduling', 'operational', 'coordination']
    },
    {
      title: 'Digital Commerce & Supply Chain',
      category: 'Service Domain 01',
      desc: 'Connect commerce, procurement, inventory, distribution, and logistics through integrated digital platforms that improve operati...',
      url: rootPrefix + 'services/digital-commerce.html',
      tags: ['digital', 'commerce', 'supply', 'chain', 'platforms', 'foodtech', 'solutions']
    },
    {
      title: 'Digital Commerce Platforms',
      category: 'Digital Commerce & Supply Ch',
      desc: 'B2B and B2C commerce platforms, digital ordering, customer portals, product catalog management, pricing workflows, order proces...',
      url: rootPrefix + 'services/digital-commerce-platforms.html',
      tags: ['digital', 'commerce', 'platforms', 'enterprise', 'portals', 'omnichannel', 'storefronts']
    },
    {
      title: 'FoodTech Solutions',
      category: 'Digital Commerce & Supply Ch',
      desc: 'Digital food ordering and distribution, food procurement, supplier coordination, batch and expiry tracking, inventory visibilit...',
      url: rootPrefix + 'services/foodtech.html',
      tags: ['foodtech', 'solutions', 'digital', 'food', 'ordering', 'distribution', 'batch', 'expiry', 'date', 'management']
    },
    {
      title: 'Supply Chain Management',
      category: 'Digital Commerce & Supply Ch',
      desc: 'Inventory and warehouse management, order lifecycle tracking, demand forecasting workflows, replenishment, supplier collaborati...',
      url: rootPrefix + 'services/supply-chain-management.html',
      tags: ['supply', 'chain', 'management', 'multi', 'node', 'inventory', 'tracking', 'order', 'lifecycle', 'orchestration']
    },
    {
      title: 'Procurement & Vendor Management',
      category: 'Digital Commerce & Supply Ch',
      desc: 'Digital purchase requisitions, approval workflows, supplier onboarding, vendor portals, purchase order management, invoice work...',
      url: rootPrefix + 'services/procurement.html',
      tags: ['procurement', 'vendor', 'management', 'digital', 'purchase', 'requisitions', 'configurable', 'approval', 'hierarchies']
    },
    {
      title: 'Logistics & Distribution',
      category: 'Digital Commerce & Supply Ch',
      desc: 'Transportation management, shipment tracking, dispatch coordination, route planning, delivery visibility, and logistics perform...',
      url: rootPrefix + 'services/logistics.html',
      tags: ['logistics', 'distribution', 'transportation', 'management', 'tms', 'real', 'time', 'shipment', 'visibility']
    },
    {
      title: 'Enterprise Business Solutions',
      category: 'Service Domain 02',
      desc: 'Modernize business operations with connected CRM, HRMS, enterprise applications, and workflow automation designed to simplify p...',
      url: rootPrefix + 'services/enterprise-business.html',
      tags: ['enterprise', 'business', 'solutions', 'customer', 'relationship', 'management', 'crm', 'human', 'resource', 'hrms']
    },
    {
      title: 'Customer Relationship Management (CRM)',
      category: 'Enterprise Business Solution',
      desc: 'Lead management, sales pipeline tracking, account management, customer onboarding, engagement workflows, customer service proce...',
      url: rootPrefix + 'services/crm.html',
      tags: ['customer', 'relationship', 'management', 'crm', 'lead', 'scoring', 'sales', 'pipeline', 'deal', 'tracking']
    },
    {
      title: 'Human Resource Management Systems (HRMS)',
      category: 'Enterprise Business Solution',
      desc: 'Employee lifecycle management, recruitment, onboarding, attendance, leave management, employee self-service, performance workfl...',
      url: rootPrefix + 'services/hrms.html',
      tags: ['human', 'resource', 'management', 'systems', 'hrms', 'recruitment', 'digital', 'onboarding', 'employee', 'self']
    },
    {
      title: 'Business Process Automation (BPA)',
      category: 'Enterprise Business Solution',
      desc: 'Approval workflows, task assignment, notifications, document processing, workflow orchestration, exception handling, escalation...',
      url: rootPrefix + 'services/business-process-automation.html',
      tags: ['business', 'process', 'automation', 'bpa', 'dynamic', 'approval', 'orchestration', 'automated', 'task', 'routing']
    },
    {
      title: 'Custom Enterprise Applications',
      category: 'Enterprise Business Solution',
      desc: 'Custom business applications, enterprise portals, operational dashboards, internal business systems, legacy application moderni...',
      url: rootPrefix + 'services/enterprise-applications.html',
      tags: ['custom', 'enterprise', 'applications', 'business', 'portals', 'operational', 'dashboards']
    },
    {
      title: 'Enterprise Integration & Business Intelligence',
      category: 'Enterprise Business Solution',
      desc: 'API integration, CRM/HRMS/ERP connectivity, third-party application integration, data synchronization, centralized reporting, a...',
      url: rootPrefix + 'services/enterprise-integration.html',
      tags: ['enterprise', 'integration', 'business', 'intelligence', 'robust', 'api', 'connectors', 'rest', 'graphql', 'bidirectional']
    },
    {
      title: 'Intelligent Monitoring & Automation',
      category: 'Service Domain 03',
      desc: 'Connect IoT devices, operational systems, real-time data, and intelligent workflows to improve visibility, identify issues fast...',
      url: rootPrefix + 'services/intelligent-monitoring.html',
      tags: ['intelligent', 'monitoring', 'automation', 'real', 'time', 'dashboards', 'internet', 'things', 'iot', 'solutions']
    },
    {
      title: 'Real-Time Monitoring & Dashboards',
      category: 'Intelligent Monitoring & Aut',
      desc: 'Live operational dashboards, equipment status monitoring, event-based alerts, centralized monitoring, operational reporting, an...',
      url: rootPrefix + 'services/real-time-monitoring.html',
      tags: ['real', 'time', 'monitoring', 'dashboards', 'sub', 'second', 'telemetry', 'visualization', 'equipment', 'status']
    },
    {
      title: 'IoT & Device Integration',
      category: 'Intelligent Monitoring & Aut',
      desc: 'IoT device integration, sensor connectivity, telemetry collection, device data visualization, asset monitoring, environmental c...',
      url: rootPrefix + 'services/iot-integration.html',
      tags: ['iot', 'device', 'integration', 'industrial', 'sensor', 'connectivity', 'edge', 'gateway', 'protocol', 'translation']
    },
    {
      title: 'Operational Analytics',
      category: 'Intelligent Monitoring & Aut',
      desc: 'KPI dashboards, historical trend analysis, operational performance reporting, anomaly detection, exception identification, and ...',
      url: rootPrefix + 'services/operational-analytics.html',
      tags: ['operational', 'analytics', 'kpi', 'dashboards', 'statistical', 'anomaly', 'detection']
    },
    {
      title: 'Intelligent Workflow Automation',
      category: 'Intelligent Monitoring & Aut',
      desc: 'Event-triggered actions, automated task creation, incident escalation, resolution workflows, rule-based responses, and human ap...',
      url: rootPrefix + 'services/workflow-automation.html',
      tags: ['intelligent', 'workflow', 'automation', 'event', 'triggered', 'automated', 'actions', 'work', 'order', 'generation']
    },
    {
      title: 'System & Infrastructure Monitoring',
      category: 'Intelligent Monitoring & Aut',
      desc: 'Application health monitoring, API monitoring, availability tracking, error monitoring, centralized logs, incident reporting, a...',
      url: rootPrefix + 'services/infrastructure-monitoring.html',
      tags: ['system', 'infrastructure', 'monitoring', 'synthetic', 'api', 'endpoint', 'centralized', 'log', 'aggregation']
    },
    {
      title: 'AI & Healthcare Technology',
      category: 'Service Domain 04',
      desc: 'Apply agentic AI, intelligent information processing, workflow automation, and healthcare technology to simplify complex busine...',
      url: rootPrefix + 'services/ai-healthcare.html',
      tags: ['healthcare', 'technology', 'agentic', 'intelligent', 'agents', 'generative', 'applications']
    },
    {
      title: 'Agentic AI & Intelligent Agents',
      category: 'Ai & Healthcare Technology',
      desc: 'AI agents for defined business workflows, multi-step task orchestration, API-connected agents, retrieval-augmented generation (...',
      url: rootPrefix + 'services/agentic-ai.html',
      tags: ['agentic', 'intelligent', 'agents', 'multi', 'step', 'task', 'orchestration', 'api', 'connected', 'tool']
    },
    {
      title: 'Generative AI & Enterprise Assistants',
      category: 'Ai & Healthcare Technology',
      desc: 'Enterprise knowledge assistants, intelligent search, document understanding, information extraction, automated summaries, repor...',
      url: rootPrefix + 'services/generative-ai.html',
      tags: ['generative', 'enterprise', 'assistants', 'knowledge', 'rag', 'semantic', 'document', 'search']
    },
    {
      title: 'Intelligent Document Processing',
      category: 'Ai & Healthcare Technology',
      desc: 'Document processing, intelligent classification, information routing, automated validation, AI-assisted support workflows, repe...',
      url: rootPrefix + 'services/document-processing.html',
      tags: ['intelligent', 'document', 'processing', 'automated', 'classification', 'complex', 'table', 'entity', 'extraction']
    },
    {
      title: 'AI-Powered Workflow Automation',
      category: 'Ai & Healthcare Technology',
      desc: 'Combining generative reasoning, document intelligence, and deterministic business rules to automate cross-system administrative...',
      url: rootPrefix + 'services/ai-workflow-automation.html',
      tags: ['powered', 'workflow', 'automation', 'inbound', 'email', 'communication', 'triage', 'cross', 'system', 'administrative']
    },
    {
      title: 'Healthcare Technology & Automation',
      category: 'Ai & Healthcare Technology',
      desc: 'Healthcare administrative automation, digital patient intake, appointment coordination, healthcare document processing, operati...',
      url: rootPrefix + 'services/healthcare-automation.html',
      tags: ['healthcare', 'technology', 'automation', 'digital', 'patient', 'pre', 'registration', 'appointment', 'coordination', 'scheduling']
    },
    {
      title: 'Healthcare Data Integration & Analytics',
      category: 'Ai & Healthcare Technology',
      desc: 'Healthcare administrative dashboards, EHR data connectivity, operational clinic metrics, and administrative billing assistance ...',
      url: rootPrefix + 'services/healthcare-data-analytics.html',
      tags: ['healthcare', 'data', 'integration', 'analytics', 'operational', 'clinic', 'dashboards', 'ehr', 'practice', 'management']
    },
    {
      title: 'Agentic AI',
      category: 'Technology Platform Architec',
      desc: 'AI agents for defined business tasks, multi-step task orchestration, tool and API integrations, knowledge retrieval, and human ...',
      url: rootPrefix + 'technology/agentic-ai.html',
      tags: ['agentic', 'goal', 'decomposition', 'task', 'planning', 'safe', 'api', 'tool', 'calling']
    },
    {
      title: 'Generative AI',
      category: 'Technology Platform Architec',
      desc: 'Enterprise AI assistants, conversational interfaces, document summarization, information extraction, enterprise knowledge searc...',
      url: rootPrefix + 'technology/generative-ai.html',
      tags: ['generative', 'retrieval', 'augmented', 'generation', 'rag', 'private', 'enterprise', 'knowledge', 'search']
    },
    {
      title: 'Intelligent Automation',
      category: 'Technology Platform Architec',
      desc: 'Rule-based automation, AI-assisted workflows, document and data processing, workflow routing and approvals, exception handling,...',
      url: rootPrefix + 'technology/intelligent-automation.html',
      tags: ['intelligent', 'automation', 'deterministic', 'business', 'rule', 'engines', 'event', 'driven', 'webhook', 'orchestration']
    },
    {
      title: 'Internet of Things (IoT)',
      category: 'Technology Platform Architec',
      desc: 'Connected devices and sensors, device and asset data, real-time telemetry, equipment monitoring, IoT data visualization, and ed...',
      url: rootPrefix + 'technology/iot.html',
      tags: ['internet', 'things', 'iot', 'lightweight', 'edge', 'protocols', 'gateway', 'computing']
    },
    {
      title: 'Enterprise Integration',
      category: 'Technology Platform Architec',
      desc: 'API integrations, third-party system connectivity, data synchronization, application interoperability, enterprise system modern...',
      url: rootPrefix + 'technology/enterprise-integration.html',
      tags: ['enterprise', 'integration', 'api', 'gateways', 'rest', 'graphql', 'bidirectional', 'data', 'buses']
    },
    {
      title: 'Data Analytics & Operational Intelligence',
      category: 'Technology Platform Architec',
      desc: 'Operational dashboards, KPI monitoring, trend analysis, reporting and visualization, anomaly detection where supported, and dat...',
      url: rootPrefix + 'technology/data-analytics.html',
      tags: ['data', 'analytics', 'operational', 'intelligence', 'interactive', 'dashboards', 'automated', 'etl', 'warehousing']
    },
    {
      title: 'FoodTech & Food Distribution',
      category: 'Target Industry Focus',
      desc: 'Digital food commerce, supplier coordination, procurement, inventory management, batch and expiry traceability, and cold chain ...',
      url: rootPrefix + 'industries/foodtech.html',
      tags: ['foodtech', 'food', 'distribution', 'digital', 'ordering', 'portals', 'fefo', 'inventory', 'batch', 'traceability']
    },
    {
      title: 'Retail & Digital Commerce',
      category: 'Target Industry Focus',
      desc: 'Digital storefronts, B2B/B2C commerce platforms, catalog management, customer portals, order fulfillment, and inventory integra...',
      url: rootPrefix + 'industries/retail-ecommerce.html',
      tags: ['retail', 'digital', 'commerce', 'unified', 'omnichannel', 'storefronts', 'dynamic', 'product', 'information', 'pim']
    },
    {
      title: 'Manufacturing & Industrial Operations',
      category: 'Target Industry Focus',
      desc: 'Industrial IoT monitoring, connected equipment, operational dashboards, event-driven alerts, predictive maintenance, and proces...',
      url: rootPrefix + 'industries/manufacturing.html',
      tags: ['manufacturing', 'industrial', 'operations', 'iot', 'telemetry', 'ingestion', 'real', 'time', 'oee', 'plant']
    },
    {
      title: 'Logistics & Supply Chain',
      category: 'Target Industry Focus',
      desc: 'Shipment visibility, warehouse management, supplier collaboration, procurement workflows, logistics analytics, and dispatch coo...',
      url: rootPrefix + 'industries/logistics.html',
      tags: ['logistics', 'supply', 'chain', 'real', 'time', 'freight', 'fleet', 'tracking', 'dynamic', 'route']
    },
    {
      title: 'Enterprise & Professional Services',
      category: 'Target Industry Focus',
      desc: 'CRM, HRMS, business process automation, custom enterprise applications, and connected business systems for corporate and consul...',
      url: rootPrefix + 'industries/enterprise.html',
      tags: ['enterprise', 'professional', 'services', 'client', 'relationship', 'management', 'crm', 'workforce', 'hrms', 'platforms']
    },
    {
      title: 'Healthcare & Health Technology',
      category: 'Target Industry Focus',
      desc: 'Healthcare administrative automation, patient intake, scheduling workflows, healthcare document processing, system integration,...',
      url: rootPrefix + 'industries/healthcare.html',
      tags: ['healthcare', 'health', 'technology', 'digital', 'patient', 'pre', 'registration', 'appointment', 'coordination', 'scheduling']
    },
    {
      title: 'General Enquiries',
      category: 'Connect With Nova Arc',
      desc: 'Get in touch with Nova Arc for general corporate communications, media inquiries, partnership discussions, or company information.',
      url: rootPrefix + 'connect/general-enquiries.html',
      tags: ['general', 'enquiries', 'corporate', 'communications', 'strategic', 'partnerships']
    },
    {
      title: 'Discuss a Project',
      category: 'Connect With Nova Arc',
      desc: 'Schedule a technical consultation to explore your business requirements, software architecture, and implementation roadmap.',
      url: rootPrefix + 'connect/project-enquiry.html',
      tags: ['discuss', 'project', 'architecture', 'discovery', 'sessions', 'tailored', 'solution', 'roadmaps']
    },
    {
      title: 'Service Enquiries',
      category: 'Connect With Nova Arc',
      desc: 'Inquire about specific technical capabilities across Digital Commerce, Enterprise Systems, Intelligent Monitoring, or AI & Heal...',
      url: rootPrefix + 'connect/service-enquiry.html',
      tags: ['service', 'enquiries', 'digital', 'commerce', 'scm', 'advisory', 'enterprise', 'business']
    },
    {
      title: 'Technical Support',
      category: 'Connect With Nova Arc',
      desc: 'Submit product tickets, report operational anomalies, or access dedicated client technical helpdesk resources.',
      url: rootPrefix + 'connect/technical-support.html',
      tags: ['technical', 'support', 'ticket', 'submission', 'tracking', 'direct', 'helpdesk', 'channels']
    }
  ];

  const searchInput = document.getElementById('siteSearchInput');
  const searchClose = document.getElementById('siteSearchCloseBtn');
  const resultsList = document.getElementById('siteSearchResultsList');
  const defaultView = document.getElementById('siteSearchDefaultView');

  const openSearch = () => {
    backdrop.classList.add('open');
    backdrop.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    renderResults(searchIndex.slice(0, 6));
    setTimeout(() => searchInput.focus(), 80);
  };

  const closeSearch = () => {
    backdrop.classList.remove('open');
    backdrop.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    searchInput.value = '';
  };

  const renderResults = (items) => {
    resultsList.innerHTML = '';
    if (!items.length) {
      resultsList.innerHTML = `<li class="site-search-empty">No matching services found. Try searching for "Commerce", "CRM", "IoT", or "AI".</li>`;
      return;
    }
    items.forEach(item => {
      const li = document.createElement('li');
      li.innerHTML = `
        <a href="${item.url}" class="site-search-result-item">
          <span class="site-search-result-cat">${item.category}</span>
          <h4 class="site-search-result-title">${item.title}</h4>
          <p class="site-search-result-desc">${item.desc}</p>
        </a>
      `;
      resultsList.appendChild(li);
    });
  };

  document.querySelectorAll('#siteSearchBtn, #mobileSearchTrigger, .open-search-trigger').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      openSearch();
    });
  });

  if (searchClose) searchClose.addEventListener('click', closeSearch);

  backdrop.addEventListener('click', (e) => {
    if (e.target === backdrop) closeSearch();
  });

  document.addEventListener('keydown', (e) => {
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      if (backdrop.classList.contains('open')) {
        closeSearch();
      } else {
        openSearch();
      }
    } else if (e.key === 'Escape' && backdrop.classList.contains('open')) {
      closeSearch();
    }
  });

  searchInput.addEventListener('input', () => {
    const query = searchInput.value.trim().toLowerCase();
    if (!query) {
      defaultView.style.display = 'block';
      renderResults(searchIndex.slice(0, 6));
      return;
    }
    defaultView.style.display = 'none';
    const matches = searchIndex.filter(item => {
      return item.title.toLowerCase().includes(query) ||
             item.category.toLowerCase().includes(query) ||
             item.desc.toLowerCase().includes(query) ||
             item.tags.some(tag => tag.includes(query));
    });
    renderResults(matches);
  });

  document.querySelectorAll('.site-search-tag').forEach(tag => {
    tag.addEventListener('click', () => {
      const q = tag.getAttribute('data-query');
      searchInput.value = q;
      searchInput.dispatchEvent(new Event('input'));
      searchInput.focus();
    });
  });
}
