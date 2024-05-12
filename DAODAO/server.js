const express = require('express');
const Web3 = require('web3');

const app = express();
const port = 3000;

// Initialize web3 with a local provider
const web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:8545'));

// Load contract ABI and address
const contractABI = require('./contractABI.json'); // Load ABI from a separate JSON file
const contractAddress = 'YOUR_CONTRACT_ADDRESS'; // Replace with your actual contract address

// Serve frontend files
app.use(express.static('public'));

// Define API endpoint to interact with smart contract
app.get('/api/balance/:address', async (req, res) => {
    const { address } = req.params;
    const contract = new web3.eth.Contract(contractABI, contractAddress);
    const balance = await contract.methods.getBalance(address).call();
    res.json({ balance });
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});