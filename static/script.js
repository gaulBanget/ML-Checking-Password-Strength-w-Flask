document.addEventListener('DOMContentLoaded', function() {
    const passwordInput = document.getElementById('passwordInput');
    const checkButton = document.getElementById('checkButton');
    const togglePassword = document.getElementById('togglePassword');
    const resultContainer = document.getElementById('resultContainer');
    const errorContainer = document.getElementById('errorContainer');

    // Toggle password visibility
    togglePassword.addEventListener('click', function() {
        const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordInput.setAttribute('type', type);
        togglePassword.textContent = type === 'password' ? '👁️' : '🙈';
    });

    // Check password on button click
    checkButton.addEventListener('click', checkPassword);

    // Check password on Enter key
    passwordInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            checkPassword();
        }
    });

    // Clear error when typing
    passwordInput.addEventListener('input', function() {
        if (errorContainer.classList.contains('hidden') === false) {
            errorContainer.classList.add('hidden');
        }
    });

    function checkPassword() {
        const password = passwordInput.value.trim();

        if (!password) {
            showError('Please enter a password');
            return;
        }

        // Disable button and show loading state
        checkButton.disabled = true;
        checkButton.textContent = 'Checking...';

        // Send request to server
        fetch('/api/check-password', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ password: password })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                displayResult(data);
                loadTips();
                errorContainer.classList.add('hidden');
            } else {
                showError(data.error || 'An error occurred');
            }
        })
        .catch(error => {
            showError('Network error: ' + error.message);
        })
        .finally(() => {
            checkButton.disabled = false;
            checkButton.textContent = 'Check Strength';
        });
    }

    function displayResult(data) {
        // Update strength display
        document.getElementById('strengthEmoji').textContent = data.emoji;
        document.getElementById('strengthLabel').textContent = data.strength_label;
        document.getElementById('strengthAdvice').textContent = data.advice;

        // Update details
        document.getElementById('passwordLength').textContent = data.password_length;
        document.getElementById('confidence').textContent = data.confidence + '%';

        // Update progress bar
        const progress = document.getElementById('strengthProgress');
        const strengthPercentages = {
            0: 33,  // Weak
            1: 66,  // Medium
            2: 100  // Strong
        };
        const percentage = strengthPercentages[data.strength_code];
        progress.style.width = percentage + '%';
        progress.style.backgroundColor = data.color;

        // Show result container
        resultContainer.classList.remove('hidden');
    }

    function loadTips() {
        fetch('/api/password-tips')
            .then(response => response.json())
            .then(data => {
                const tipsList = document.getElementById('tipsList');
                tipsList.innerHTML = '';
                data.tips.forEach(tip => {
                    const li = document.createElement('li');
                    li.textContent = tip;
                    tipsList.appendChild(li);
                });
            })
            .catch(error => console.error('Error loading tips:', error));
    }

    function showError(message) {
        document.getElementById('errorMessage').textContent = message;
        errorContainer.classList.remove('hidden');
        resultContainer.classList.add('hidden');
    }
});
