require('dotenv').config()

const url = `https://api.etherscan.io/api?module=account&action=tokentx&address=${process.env.ETHEREUM_ADDRESS}&page=1&offset=100&startblock=0&endblock=27025780&sort=asc&apikey=${process.env.ETHERSCAN_API_KEY}`;

fetch(url)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));

  fetch(url)
  .then(response => response.json())
  .then(data => {
    // Access and handle the response data here
    console.log(data);
  })
  .catch(error => console.error('Error:', error));
