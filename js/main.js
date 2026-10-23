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
   Services Mega-Menu Dropdown (Desktop & Keyboard/A11y)
   -------------------------------------------------------------------------- */
function initServicesMegaMenu() {
  const toggleBtn = document.getElementById('servicesDropdownToggle');
  const megaPanel = document.getElementById('servicesMegaMenu');
  const navItem = toggleBtn ? toggleBtn.closest('.nav-item-dropdown') : null;

  if (!toggleBtn || !megaPanel) return;

  const openMenu = () => {
    megaPanel.classList.add('open');
    if (navItem) navItem.classList.add('open');
    toggleBtn.classList.add('active');
    toggleBtn.setAttribute('aria-expanded', 'true');
    megaPanel.setAttribute('aria-hidden', 'false');
  };

  const closeMenu = () => {
    megaPanel.classList.remove('open');
    if (navItem) navItem.classList.remove('open');
    toggleBtn.classList.remove('active');
    toggleBtn.setAttribute('aria-expanded', 'false');
    megaPanel.setAttribute('aria-hidden', 'true');
  };

  // Hover support: open on mouseenter
  // Persistent Display When Cursor Leaves: do NOT close on mouseleave!
  if (navItem) {
    navItem.addEventListener('mouseenter', () => {
      openMenu();
    });
  }

  // Clicking the Services dropdown toggle:
  // - If clicking the chevron arrow: toggle the megamenu open/close
  // - If clicking "Services" link text:
  //   * If already on services.html, close megamenu so page content is visible
  //   * If on another page, navigate to services.html!
  toggleBtn.addEventListener('click', (e) => {
    const isChevron = e.target.closest('.dropdown-chevron');
    if (isChevron) {
      e.preventDefault();
      e.stopPropagation();
      const isOpen = megaPanel.classList.contains('open');
      if (isOpen) {
        closeMenu();
      } else {
        openMenu();
      }
      return;
    }

    const isCurrentServicesPage = window.location.pathname.endsWith('services.html') || 
                                  window.location.pathname.endsWith('/services') ||
                                  window.location.pathname === '/services.html';
    if (isCurrentServicesPage) {
      if (megaPanel.classList.contains('open')) {
        closeMenu();
      }
    } else {
      closeMenu();
    }
  });

  // If user clicks a link inside the mega menu, close menu on navigation
  megaPanel.addEventListener('click', (e) => {
    const link = e.target.closest('a');
    if (link) {
      closeMenu();
    }
  });

  // If user enters another dropdown in navbar (e.g. Solutions or AI Platform), close Services
  const otherDropdowns = document.querySelectorAll('.nav-item-dropdown:not(.nav-item-services)');
  otherDropdowns.forEach(otherItem => {
    otherItem.addEventListener('mouseenter', () => {
      closeMenu();
    });
  });

  // Close when clicking outside navbar and megamenu so user can interact with the page
  document.addEventListener('click', (e) => {
    if (navItem && !navItem.contains(e.target) && !megaPanel.contains(e.target)) {
      if (megaPanel.classList.contains('open')) {
        closeMenu();
      }
    }
  });

  // Close on Escape key and return focus
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && megaPanel.classList.contains('open')) {
      closeMenu();
      toggleBtn.focus();
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

  // Mobile accordion toggle for Services submenu
  const mobileServicesToggle = drawer.querySelector('#mobileServicesToggle');
  if (mobileServicesToggle && mobileServicesSubmenu) {
    bindAction(mobileServicesToggle, () => {
      const isOpen = mobileServicesSubmenu.classList.contains('open');
      if (isOpen) {
        mobileServicesSubmenu.classList.remove('open');
        mobileServicesToggle.classList.remove('open');
        mobileServicesToggle.setAttribute('aria-expanded', 'false');
        mobileServicesSubmenu.setAttribute('aria-hidden', 'true');
      } else {
        mobileServicesSubmenu.classList.add('open');
        mobileServicesToggle.classList.add('open');
        mobileServicesToggle.setAttribute('aria-expanded', 'true');
        mobileServicesSubmenu.setAttribute('aria-hidden', 'false');
      }
    });
  }
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
    state: {
      el: document.getElementById('demo-state'),
      err: document.getElementById('error-state'),
      validate: (val) => val.trim() !== '',
      msg: 'Please select your state.'
    },
    title: {
      el: document.getElementById('demo-title'),
      err: document.getElementById('error-title'),
      validate: (val) => val.trim() !== '',
      msg: 'Please select your professional role.'
    },
    company: {
      el: document.getElementById('demo-company'),
      err: document.getElementById('error-company'),
      validate: (val) => val.trim().length >= 2,
      msg: 'Please specify your healthcare organization.'
    }
  };

  // Real-time error clearance on input
  Object.keys(fields).forEach(key => {
    const item = fields[key];
    if (item.el) {
      item.el.addEventListener('input', () => {
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
      Scheduling Demo...
    `;

    setTimeout(() => {
      const applicantName = fields.name.el.value.trim();
      const applicantOrg = fields.company.el.value.trim();
      const applicantEmail = fields.email.el.value.trim();
      const applicantPhone = fields.phone.el.value.trim();
      const applicantState = fields.state.el.value;
      const applicantTitle = fields.title.el.value;

      // Save submission to persistent storage
      const record = saveSubmission('demo', {
        name: applicantName,
        email: applicantEmail,
        phone: applicantPhone,
        state: applicantState,
        title: applicantTitle,
        company: applicantOrg,
        source: 'Homepage Demo Request Form'
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
        'physician-query-management': 'Physician Query Management & Education Coaching',
        'hcc-risk-adjustment': 'Inpatient DRG Validation & HCC Risk Adjustment',
        'cdm-charge-capture': 'CDM Pricing Audit & Missed-Charge Reconciliation',
        'compliance-audit-defense': 'OIG & RAC Audit Defense & Compliance Management',
        'cdi-chart-auditing': 'Clinical Documentation Improvement (CDI) & Chart Auditing',
        'full-cycle-medical-coding': 'Full-Cycle Medical Coding (Inpatient, Outpatient, ProFee)',
        'referral-order-management': 'Referral & Order Management (LCD/NCD & ABN)',
        'point-of-service-collections': 'Point-of-Service (POS) Collection Assistance',
        'financial-clearance-gfe': 'Pre-Service Financial Clearance & Good Faith Estimates (GFE)',
        'patient-registration-verification': 'Scheduling & Patient Registration Verification',
        'real-time-insurance-eligibility': 'Real-Time Insurance Eligibility & Benefits (270/271)',
        'claims-management-scrubbing': 'Claims Management & Clearinghouse Scrubbing',
        'payment-posting-reconciliation': 'Payment Posting & Electronic Remittance (ERA / 835)',
        'prior-authorization': 'Prior Authorization & Referral Management',
        'patient-access': 'Patient Access Services',
        'ar-management': 'A/R Management & Aged Claims Liquidation',
        'denial-management': 'Denial & Appeals Management (Root-Cause Recovery)',
        'payer-contract-modeling': 'Payer Contract Modeling & Underpayment Variance Recovery',
        'patient-billing-collections': 'Patient Billing, Self-Pay & Omnichannel Collections',
        'credit-balance-resolution': 'Credit Balance Resolution & Overpayment Refund Compliance',
        'extended-business-office': 'Extended Business Office (EBO) Surge & Aged A/R Cleanup',
        'full-cycle-rcm': 'End-to-End Enterprise Full-Cycle RCM (Single SLA)',
        'rcm-workflow-audit': 'RCM Workflow Audit, KPI Benchmarking & Tech Stack Advisory',
        'fractional-rcm-leadership': 'Fractional CFO & Interim RCM Leadership (EHR Surge Staffing)'
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
        messageField.value = `Hello Nova Arc team, I would like to schedule an operational review for ${serviceDisplayName}. Please provide your detailed workflow specifications and SLA benchmarks.`;
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
      msg: 'Please specify your healthcare organization.'
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
   Simple Dropdown Toggles (Solutions & AI Platform)
   -------------------------------------------------------------------------- */
function initNavSimpleDropdowns() {
  const toggles = document.querySelectorAll('.nav-dropdown-link');
  toggles.forEach(toggle => {
    toggle.addEventListener('click', (e) => {
      if (window.innerWidth < 992) {
        e.preventDefault();
        const parent = toggle.closest('.nav-item-dropdown');
        if (parent) {
          parent.classList.toggle('open');
          const isExpanded = parent.classList.contains('open');
          toggle.setAttribute('aria-expanded', isExpanded ? 'true' : 'false');
        }
      }
    });
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
          <input type="text" class="site-search-input" id="siteSearchInput" placeholder="Search services, solutions, coding, prior auth..." autocomplete="off">
          <button type="button" class="site-search-close" id="siteSearchCloseBtn" aria-label="Close search">ESC</button>
        </div>
        <div class="site-search-body">
          <div id="siteSearchDefaultView">
            <div class="site-search-section-title">Quick Suggestions</div>
            <div class="site-search-tags">
              <button type="button" class="site-search-tag" data-query="Eligibility">Eligibility &amp; Benefits</button>
              <button type="button" class="site-search-tag" data-query="Prior Authorization">Prior Authorization</button>
              <button type="button" class="site-search-tag" data-query="Medical Coding">Medical Coding</button>
              <button type="button" class="site-search-tag" data-query="Medical Necessity">Medical Necessity</button>
              <button type="button" class="site-search-tag" data-query="Denial Management">Denials &amp; Appeals</button>
              <button type="button" class="site-search-tag" data-query="AI Platform">AI Platform</button>
              <button type="button" class="site-search-tag" data-query="Collections">Point-of-Service</button>
            </div>
            <div class="site-search-section-title">Featured Services</div>
          </div>
          <ul class="site-search-results" id="siteSearchResultsList"></ul>
        </div>
      </div>
    `;
    document.body.appendChild(backdrop);
  }

  const isServicesDir = window.location.pathname.includes('/services/');
  const rootPrefix = isServicesDir ? '../' : '';
  const servicesPrefix = isServicesDir ? '' : 'services/';

  const searchIndex = [
    {
      title: 'Insurance Eligibility & Benefits Verification',
      category: 'Patient Access',
      desc: 'Real-time 270/271 EDI coverage verification and co-pay validation.',
      url: servicesPrefix + 'real-time-insurance-eligibility.html',
      tags: ['eligibility', 'benefits', 'insurance', 'coverage', '270', '271', 'copay']
    },
    {
      title: 'Prior Authorization Management',
      category: 'Patient Access',
      desc: 'Proactive requirement verification, tracking, and end-to-end payer submission.',
      url: servicesPrefix + 'prior-authorization-management.html',
      tags: ['prior auth', 'authorization', 'precertification', 'stat auth', 'peer to peer']
    },
    {
      title: 'Patient Scheduling & Registration QA',
      category: 'Patient Access',
      desc: 'Demographic validation and appointment QA preventing front-end rework.',
      url: servicesPrefix + 'patient-registration-verification.html',
      tags: ['scheduling', 'registration', 'qa', 'demographics', 'intake', 'patient access']
    },
    {
      title: 'Financial Clearance & Good Faith Estimates',
      category: 'Patient Access',
      desc: 'Pre-service liability calculation, No Surprises Act compliance, and GFE generation.',
      url: servicesPrefix + 'financial-clearance-gfe.html',
      tags: ['financial clearance', 'gfe', 'good faith estimates', 'no surprises act', 'estimates']
    },
    {
      title: 'Point-of-Service Collections',
      category: 'Patient Access',
      desc: 'Compassionate upfront patient payment collection and financial counseling.',
      url: servicesPrefix + 'point-of-service-collections.html',
      tags: ['pos', 'collections', 'point of service', 'upfront', 'copays', 'self-pay']
    },
    {
      title: 'Medical Necessity & Order Verification',
      category: 'Patient Access',
      desc: 'LCD/NCD validation, order signatures, and clinical compliance checks before care.',
      url: servicesPrefix + 'referral-order-management.html',
      tags: ['medical necessity', 'order verification', 'lcd', 'ncd', 'abn', 'referral']
    },
    {
      title: 'Full-Cycle Medical Coding Services',
      category: 'HIM & Coding',
      desc: 'Inpatient DRG, outpatient surgery, and profee multi-specialty coding.',
      url: servicesPrefix + 'full-cycle-medical-coding.html',
      tags: ['medical coding', 'drg', 'cpt', 'icd-10', 'profee', 'inpatient']
    },
    {
      title: 'Risk Adjustment & HCC Coding',
      category: 'HIM & Coding',
      desc: 'Hierarchical Condition Category capture ensuring Medicare Advantage revenue integrity.',
      url: servicesPrefix + 'hcc-risk-adjustment.html',
      tags: ['hcc', 'risk adjustment', 'medicare advantage', 'raf', 'chart audit']
    },
    {
      title: 'Clinical Documentation Improvement (CDI)',
      category: 'HIM & Coding',
      desc: 'Concurrent and retrospective chart auditing to capture true patient acuity.',
      url: servicesPrefix + 'cdi-chart-auditing.html',
      tags: ['cdi', 'chart auditing', 'acuity', 'clinical documentation', 'query']
    },
    {
      title: 'Computer-Assisted Coding (CAC) Review',
      category: 'HIM & Coding',
      desc: 'Expert human validation optimizing NLP and AI auto-suggested coding pipelines.',
      url: servicesPrefix + 'cac-review.html',
      tags: ['cac', 'nlp', 'computer-assisted', 'validation', 'automation']
    },
    {
      title: 'Coding Compliance & Audit Defense',
      category: 'HIM & Coding',
      desc: 'External quality audits, RAC defense, and OIG workplan risk mitigation.',
      url: servicesPrefix + 'compliance-audit-defense.html',
      tags: ['compliance', 'audit', 'defense', 'rac', 'oig', 'quality']
    },
    {
      title: 'Charge Capture & CDM Audit',
      category: 'HIM & Coding',
      desc: 'Reconciling clinical administration against chargemaster entries to eliminate revenue leakage.',
      url: servicesPrefix + 'cdm-charge-capture.html',
      tags: ['cdm', 'charge capture', 'chargemaster', 'leakage', 'reconciliation']
    },
    {
      title: 'Physician Query Management',
      category: 'HIM & Coding',
      desc: 'Compliant clinical clarification workflows for non-leading provider queries.',
      url: servicesPrefix + 'physician-query-management.html',
      tags: ['physician query', 'clarification', 'ahima', 'acdis', 'queries']
    },
    {
      title: 'Claims Submission & Scrubbing (EDI 837)',
      category: 'Patient Financial Services',
      desc: '98%+ first-pass clean claim rates through automated multi-payer rules engines.',
      url: servicesPrefix + 'claims-management-scrubbing.html',
      tags: ['claims', 'scrubbing', '837', 'clean claim', 'edi', 'submission']
    },
    {
      title: 'Payment Posting & Reconciliation (EDI 835)',
      category: 'Patient Financial Services',
      desc: 'Automated ERA posting, manual EOB indexing, and zero-balance banking reconciliation.',
      url: servicesPrefix + 'payment-posting-reconciliation.html',
      tags: ['payment posting', '835', 'era', 'eob', 'reconciliation', 'remittance']
    },
    {
      title: 'A/R Management Services',
      category: 'Patient Financial Services',
      desc: 'Targeted aging bucket resolution across commercial, Medicare, and Medicaid accounts.',
      url: servicesPrefix + 'ar-management.html',
      tags: ['ar', 'accounts receivable', 'aging', 'follow-up', 'payer']
    },
    {
      title: 'Denial Management & Appeals',
      category: 'Patient Financial Services',
      desc: 'Root-cause CARC/RARC analysis, clinical appeals, and overturned recovery workflows.',
      url: servicesPrefix + 'denial-management.html',
      tags: ['denials', 'appeals', 'carc', 'rarc', 'overturn', 'recovery']
    },
    {
      title: 'Underpayment Recovery & Contract Compliance',
      category: 'Patient Financial Services',
      desc: 'Fee schedule modeling and forensic variance audits recovering unpaid contractual balances.',
      url: servicesPrefix + 'payer-contract-modeling.html',
      tags: ['underpayment', 'contract modeling', 'variance', 'fee schedule']
    },
    {
      title: 'Patient Billing & Self-Pay Collections',
      category: 'Patient Financial Services',
      desc: 'Clear statements, digital payment portals, and patient-friendly financial resolution.',
      url: servicesPrefix + 'patient-billing-collections.html',
      tags: ['patient billing', 'self-pay', 'statements', 'portal', 'balances']
    },
    {
      title: 'Credit Balance & Refund Management',
      category: 'Patient Financial Services',
      desc: 'Auditing overpayments and processing CMS-compliant refunds to prevent compliance penalties.',
      url: servicesPrefix + 'credit-balance-resolution.html',
      tags: ['credit balance', 'refunds', 'overpayments', 'compliance']
    },
    {
      title: 'Extended Business Office (EBO)',
      category: 'Patient Financial Services',
      desc: 'Scalable revenue cycle staffing extending your internal business office operations.',
      url: servicesPrefix + 'extended-business-office.html',
      tags: ['ebo', 'extended business office', 'staffing', 'scaling']
    },
    {
      title: 'Full-Cycle RCM Management',
      category: 'Solutions',
      desc: 'Comprehensive front-to-back revenue cycle management for hospitals and health systems.',
      url: servicesPrefix + 'full-cycle-rcm.html',
      tags: ['full cycle', 'end-to-end', 'operations', 'comprehensive rcm']
    },
    {
      title: 'Nova Arc AI Platform',
      category: 'Technology',
      desc: 'Sub-second autonomous AI agents, intelligent prior auth, and autonomous clinical coding.',
      url: rootPrefix + 'ai-platform.html',
      tags: ['ai', 'platform', 'agents', 'automation', 'intelligence', 'autonomous']
    },
    {
      title: 'All Solutions Overview',
      category: 'Solutions',
      desc: 'Discover Nova Arc’s complete enterprise healthcare revenue cycle portfolio.',
      url: rootPrefix + 'solutions.html',
      tags: ['solutions', 'overview', 'suite', 'services portfolio']
    },
    {
      title: 'Who We Serve',
      category: 'Organization',
      desc: 'Health systems, academic medical centers, ambulatory groups, and specialty practices.',
      url: rootPrefix + 'who-we-serve.html',
      tags: ['who we serve', 'health systems', 'hospitals', 'physician groups', 'specialties']
    },
    {
      title: 'Connect with Us / Request Consultation',
      category: 'Contact',
      desc: 'Get in touch with Nova Arc revenue cycle leadership for tailored consultations.',
      url: rootPrefix + 'contact.html',
      tags: ['contact', 'consultation', 'demo', 'connect', 'phone', 'email']
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
      resultsList.innerHTML = `<li class="site-search-empty">No matching services found. Try searching for "Prior Auth", "Coding", or "Eligibility".</li>`;
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
