// Wolf-Byte Interactive Features
document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu Toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const navMenu = document.querySelector('.nav-menu');
    
    if (menuToggle) {
        menuToggle.addEventListener('click', () => {
            navMenu.classList.toggle('active');
            menuToggle.classList.toggle('active');
        });
    }
    
    // Smooth Scroll
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
                // Close mobile menu if open
                if (navMenu.classList.contains('active')) {
                    navMenu.classList.remove('active');
                    menuToggle.classList.remove('active');
                }
            }
        });
    });
    
    // Navbar Background on Scroll
    const header = document.querySelector('.header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 100) {
            header.style.background = 'rgba(10, 10, 10, 0.98)';
        } else {
            header.style.background = 'linear-gradient(180deg, rgba(10,10,10,0.95) 0%, rgba(26,26,26,0.9) 100%)';
        }
    });
    
    // Animate Stats on Scroll
    const observerOptions = {
        threshold: 0.5,
        rootMargin: '0px 0px -100px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateValue(entry.target);
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    document.querySelectorAll('.stat-value').forEach(stat => {
        observer.observe(stat);
    });
    
    function animateValue(element) {
        const text = element.textContent;
        const hasPercent = text.includes('%');
        const hasPlus = text.includes('+');
        const hasMinus = text.includes('-');
        
        let numericValue = parseInt(text.replace(/[^0-9]/g, ''));
        if (isNaN(numericValue)) return;
        
        const duration = 2000;
        const stepTime = 50;
        const steps = duration / stepTime;
        const increment = numericValue / steps;
        let current = 0;
        
        const timer = setInterval(() => {
            current += increment;
            if (current >= numericValue) {
                current = numericValue;
                clearInterval(timer);
            }
            
            let displayValue = Math.floor(current);
            if (hasMinus) displayValue = '-' + displayValue;
            if (hasPlus) displayValue = '+' + displayValue;
            if (hasPercent) displayValue += '%';
            
            element.textContent = displayValue;
        }, stepTime);
    }
    
    // Typing Effect for AI Chat
    const typingMessages = document.querySelectorAll('.chat-message.bot:not(.typing)');
    let typingObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }, 300);
                typingObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });
    
    typingMessages.forEach(msg => {
        msg.style.opacity = '0';
        msg.style.transform = 'translateY(20px)';
        msg.style.transition = 'all 0.5s ease';
        typingObserver.observe(msg);
    });
    
    // Form Submission
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            // Get form values
            const formData = new FormData(contactForm);
            const data = Object.fromEntries(formData);
            
            // Show success message
            const submitButton = contactForm.querySelector('.submit-button');
            const originalText = submitButton.textContent;
            
            submitButton.textContent = '✓ Mensaje Enviado!';
            submitButton.style.background = 'linear-gradient(135deg, #2ecc71, #27ae60)';
            
            // Reset form
            contactForm.reset();
            
            // Reset button after 3 seconds
            setTimeout(() => {
                submitButton.textContent = originalText;
                submitButton.style.background = 'linear-gradient(135deg, var(--lannister-gold), var(--lannister-red))';
            }, 3000);
            
            // In production, you would send data to backend here
            console.log('Form submitted:', data);
        });
    }
    
    // Solution Cards Hover Effect
    document.querySelectorAll('.solution-card').forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'translateY(-10px)';
        });
        
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'translateY(0)';
        });
    });
    
    // Create Simple Chart Animation (using Canvas)
    const chartCanvas = document.getElementById('chart1');
    if (chartCanvas) {
        const ctx = chartCanvas.getContext('2d');
        chartCanvas.width = chartCanvas.offsetWidth;
        chartCanvas.height = 200;
        
        let chartObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    drawChart(ctx, chartCanvas.width, chartCanvas.height);
                    chartObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });
        
        chartObserver.observe(chartCanvas);
    }
    
    function drawChart(ctx, width, height) {
        const data = [65, 78, 85, 72, 90, 95, 88, 92, 97, 100, 105, 110];
        const padding = 40;
        const chartWidth = width - padding * 2;
        const chartHeight = height - padding * 2;
        
        // Clear canvas
        ctx.clearRect(0, 0, width, height);
        
        // Set styles
        ctx.strokeStyle = '#d4af37';
        ctx.lineWidth = 3;
        ctx.lineCap = 'round';
        ctx.lineJoin = 'round';
        
        // Draw gradient
        const gradient = ctx.createLinearGradient(0, padding, 0, height - padding);
        gradient.addColorStop(0, 'rgba(212, 175, 55, 0.3)');
        gradient.addColorStop(1, 'rgba(212, 175, 55, 0.05)');
        
        // Animate drawing
        let progress = 0;
        const animationDuration = 2000;
        const startTime = Date.now();
        
        function animate() {
            const currentTime = Date.now();
            progress = Math.min((currentTime - startTime) / animationDuration, 1);
            
            ctx.clearRect(0, 0, width, height);
            
            // Draw grid
            ctx.strokeStyle = 'rgba(192, 192, 192, 0.1)';
            ctx.lineWidth = 1;
            for (let i = 0; i <= 5; i++) {
                const y = padding + (chartHeight / 5) * i;
                ctx.beginPath();
                ctx.moveTo(padding, y);
                ctx.lineTo(width - padding, y);
                ctx.stroke();
            }
            
            // Calculate points
            const maxValue = Math.max(...data);
            const points = data.slice(0, Math.floor(data.length * progress)).map((value, index) => {
                const x = padding + (chartWidth / (data.length - 1)) * index;
                const y = height - padding - (value / maxValue) * chartHeight;
                return { x, y };
            });
            
            if (points.length > 1) {
                // Draw filled area
                ctx.fillStyle = gradient;
                ctx.beginPath();
                ctx.moveTo(points[0].x, height - padding);
                points.forEach(point => ctx.lineTo(point.x, point.y));
                ctx.lineTo(points[points.length - 1].x, height - padding);
                ctx.closePath();
                ctx.fill();
                
                // Draw line
                ctx.strokeStyle = '#d4af37';
                ctx.lineWidth = 3;
                ctx.beginPath();
                ctx.moveTo(points[0].x, points[0].y);
                points.forEach(point => ctx.lineTo(point.x, point.y));
                ctx.stroke();
                
                // Draw points
                points.forEach(point => {
                    ctx.fillStyle = '#d4af37';
                    ctx.beginPath();
                    ctx.arc(point.x, point.y, 4, 0, Math.PI * 2);
                    ctx.fill();
                    
                    // Glow effect
                    ctx.shadowBlur = 10;
                    ctx.shadowColor = '#d4af37';
                    ctx.fill();
                    ctx.shadowBlur = 0;
                });
            }
            
            if (progress < 1) {
                requestAnimationFrame(animate);
            }
        }
        
        animate();
    }
    
    // Parallax Effect for Hero
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const heroContent = document.querySelector('.hero-content');
        if (heroContent) {
            heroContent.style.transform = `translateY(${scrolled * 0.5}px)`;
            heroContent.style.opacity = 1 - (scrolled / 600);
        }
    });
    
    // Add entrance animations
    const animateOnScroll = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
                animateOnScroll.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });
    
    document.querySelectorAll('.solution-card, .about-card, .info-card').forEach(element => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(50px)';
        element.style.transition = 'all 0.6s ease';
        animateOnScroll.observe(element);
    });
    
    // Add animate-in class styles dynamically
    const style = document.createElement('style');
    style.textContent = `
        .animate-in {
            opacity: 1 !important;
            transform: translateY(0) !important;
        }
    `;
    document.head.appendChild(style);
});
