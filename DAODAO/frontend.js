document.addEventListener('DOMContentLoaded', async () => {
    // Fetch account balance from backend server
    const response = await fetch('/api/balance/address');
    const { balance } = await response.json();

    // Update frontend UI with account balance
    document.getElementById('balance').innerText = balance;
});