/*require('dotenv').config()
const fs = require('fs');
const url = `https://api.etherscan.io/api?module=account&action=tokentx&address=${process.env.ETHEREUM_ADDRESS}&page=1&offset=100&startblock=0&endblock=27025780&sort=asc&apikey=${process.env.ETHERSCAN_API_KEY}`;

// https://api.arkhamintelligence.com/transfers?base=${process.env.ETHEREUM_ADDRESS}&tokens=apecoin&chain=ethereum&sortDir=desc&limit=20&valuegte=1000

// https://api.arkhamintelligence.com/transfers?base=0xb1Df9c43981479dCD43BB738fF5001322A65fDfc&tokens=apecoin&chain=ethereum&sortDir=desc&limit=20&valuegte=1000

*/

require('dotenv').config()
const fs = require('fs');

const url = `https://api.arkhamintelligence.com/transfers?base=${process.env.ETHEREUM_ADDRESS}&tokens=apecoin&chain=ethereum&sortDir=desc&limit=20&valuegte=1000`;

fetch(url, {
  headers: {
    'Authorization': `API-KEY${process.env.ARKHAM}`
  }
})
.then(response => response.json())
.then(data => {
  fs.writeFile('data.json', JSON.stringify(data, null, 2), (err) => {
    if (err) throw err;
    console.log('Data written to file');
  });
})
.catch(error => console.error('Error:', error));
