/**
 * Nova Arc - Main Interactive Script
 * Features:
 *  - Sticky Navbar & Mobile Drawer
 *  - Animated Metrics Counters (Intersection Observer)
 *  - AI Platform Interactive Console Switcher
 *  - Comprehensive Demo Request Form Validation & Feedback
 *  - Smooth In-Page Anchor Navigation
 */

document.addEventListener('DOMContentLoaded', () => {
  initStickyHeader();
  initServicesMegaMenu();
  initMobileNavigation();
  initStatsCounter();
  initAITabs();
  initDemoForm();
  initSmoothScroll();
  initSolutionModals();
  initServicesAccordions();
  initCategoryPills();
  initContactPageForm();
  initAnalyticsTracking();
  initWaveformInteraction();
});

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
  const dropdownItem = document.querySelector('.nav-item-dropdown');

  if (!toggleBtn || !megaPanel) return;

  const openMenu = () => {
    megaPanel.classList.add('open');
    toggleBtn.classList.add('active');
    toggleBtn.setAttribute('aria-expanded', 'true');
    megaPanel.setAttribute('aria-hidden', 'false');
  };

  const closeMenu = () => {
    megaPanel.classList.remove('open');
    toggleBtn.classList.remove('active');
    toggleBtn.setAttribute('aria-expanded', 'false');
    megaPanel.setAttribute('aria-hidden', 'true');
  };

  const toggleMenu = (e) => {
    e.preventDefault();
    e.stopPropagation();
    const isOpen = megaPanel.classList.contains('open');
    if (isOpen) {
      closeMenu();
    } else {
      openMenu();
    }
  };

  toggleBtn.addEventListener('click', toggleMenu);

  // Close on outside click
  document.addEventListener('click', (e) => {
    if (dropdownItem && !dropdownItem.contains(e.target)) {
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

  // Close when clicking any link inside the mega menu
  const menuLinks = megaPanel.querySelectorAll('a');
  menuLinks.forEach(link => {
    link.addEventListener('click', () => {
      closeMenu();
    });
  });
}

/* --------------------------------------------------------------------------
   2. Mobile Navigation Drawer & Services Accordion
   -------------------------------------------------------------------------- */
function initMobileNavigation() {
  const toggleBtn = document.querySelector('.mobile-toggle');
  const drawer = document.querySelector('.mobile-nav-drawer') || document.querySelector('.mobile-nav');
  // Exclude accordion toggle buttons from auto-closing the drawer
  const navLinks = document.querySelectorAll(
    '.mobile-nav-link:not(.mobile-accordion-toggle), .mobile-nav-drawer .btn, .mobile-submenu-link, .mobile-submenu-sublink, .mobile-overview-btn'
  );

  if (!toggleBtn || !drawer) return;

  const toggleMenu = () => {
    const isActive = drawer.classList.contains('active');
    if (isActive) {
      drawer.classList.remove('active');
      toggleBtn.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
      toggleBtn.innerHTML = `
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <line x1="3" y1="12" x2="21" y2="12"></line>
          <line x1="3" y1="6" x2="21" y2="6"></line>
          <line x1="3" y1="18" x2="21" y2="18"></line>
        </svg>
      `;
    } else {
      drawer.classList.add('active');
      toggleBtn.setAttribute('aria-expanded', 'true');
      document.body.style.overflow = 'hidden';
      toggleBtn.innerHTML = `
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <line x1="18" y1="6" x2="6" y2="18"></line>
          <line x1="6" y1="6" x2="18" y2="18"></line>
        </svg>
      `;
    }
  };

  toggleBtn.addEventListener('click', toggleMenu);

  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      if (drawer.classList.contains('active')) {
        toggleMenu();
      }
    });
  });

  // Mobile accordion toggle for Services submenu
  const mobileServicesToggle = document.getElementById('mobileServicesToggle');
  const mobileServicesSubmenu = document.getElementById('mobileServicesSubmenu');
  if (mobileServicesToggle && mobileServicesSubmenu) {
    mobileServicesToggle.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
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



