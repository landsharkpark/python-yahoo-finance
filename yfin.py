// JavaScript program to convert csv to json file

console.log('JavaScript Program To Convert CSV to JSON');

// Verify filename is passed in as argument
if (process.env.length < 3) {
    console.log("Usage: node " + process.argv[1] + ' FILENAME');
    process.exit(1);
}

console.log("\nreadFileSync method...");

var fs = require('fs');
var readCSV = fs.readFileSync(process.argv[2], 'utf8').split(/\r?\n/);
console.log("\nreadCSV array: ", readCSV, "\n");

var repDay = [];
var linecount;
for (linecount = 2; linecount < readCSV.length; linecount++) {
    var prevDay = readCSV[linecount - 1].split(',');
    var prevDayClose = prevDay[5];
    var csvDay = readCSV[linecount].split(',');

    // repDay
    //  date
    //  dayClose
    //  dayRange
    //  prevDayChange
    //  prevDayPctChange
    repDay.push({
        "day": csvDay[0],
        "dayClose": parseFloat(csvDay[5]).toFixed(2),
        "dayRange": parseFloat(csvDay[2] - csvDay[3]).toFixed(2),
        "dayPtsChgPrevDay": parseFloat(csvDay[5] - prevDayClose).toFixed(2),
        "dayPctChgPrevDay": parseFloat(((csvDay[5] - prevDayClose) / prevDayClose) * 100).toFixed(2) + "%"
    })
}

// new JSON - Dow Jones
if (process.argv[2].substring(5,8) === 'dow') {
    let dowJson = {
        "ticker": "^DJI",
        "name": "Dow Jones Industrial Average",
        "tradingdays": repDay
    }
    
    console.log(JSON.stringify(dowJson));

    fs.writeFileSync('./data/dow.json', JSON.stringify(dowJson));
}

if (process.argv[2].substring(5,11) === 'nasdaq') {
    let nasdaqJson = {
        "ticker": "^IXIC",
        "name": "NASDAQ",
        "tradingdays": repDay
    }
    
    console.log(JSON.stringify(nasdaqJson));
    fs.writeFileSync('./data/nasdaq.json', JSON.stringify(nasdaqJson));
}

if (process.argv[2].substring(5,10) === 'sp500') {
    let sp500Json = {
        "ticker": "^GSPC",
        "name": "S&P 500",
        "tradingdays": repDay
    }
    
    console.log(JSON.stringify(sp500Json));
    fs.writeFileSync('./data/sp500.json', JSON.stringify(sp500Json));
}
