// Main JavaScript file for Student Management System

// Wait for DOM content to be loaded
document.addEventListener('DOMContentLoaded', function() {
    // Auto-hide flash messages after 5 seconds
    const flashMessages = document.querySelectorAll('.alert');
    if (flashMessages.length > 0) {
        setTimeout(function() {
            flashMessages.forEach(function(message) {
                message.style.transition = 'opacity 1s';
                message.style.opacity = '0';
                setTimeout(function() {
                    message.remove();
                }, 1000);
            });
        }, 5000);
    }

    // Activate tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});