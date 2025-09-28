document.addEventListener('DOMContentLoaded', function() {
    const tabButtons = document.querySelectorAll('.tab-button');
    const clientForm = document.getElementById('client-form');
    const therapistForm = document.getElementById('therapist-form');
    const accountTypeInput = document.getElementById('account_type');

    function disableFields(container, disabled) {
        container.querySelectorAll('input, select, textarea').forEach(el => {
            el.disabled = disabled;
        });
    }

    function toggleTab(tab) {
        tabButtons.forEach(btn => btn.classList.remove('active'));
        document.querySelector(`.tab-button[data-tab="${tab}"]`).classList.add('active');

        clientForm.classList.remove('active');
        therapistForm.classList.remove('active');

        disableFields(clientForm, true);
        disableFields(therapistForm, true);

        if (tab === 'client') {
            clientForm.classList.add('active');
            accountTypeInput.value = 'client';
            disableFields(clientForm, false);
        } else if (tab === 'therapist') {
            therapistForm.classList.add('active');
            accountTypeInput.value = 'therapist';
            disableFields(therapistForm, false);
        }
    }

    toggleTab('client');

    tabButtons.forEach(button => {
        button.addEventListener('click', function() {
            toggleTab(this.dataset.tab);
        });
    });
});
