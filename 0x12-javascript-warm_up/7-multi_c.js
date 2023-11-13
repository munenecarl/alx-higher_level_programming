#!/usr/bin/node

if (isNaN(process.argv[2])) {
	console.log("Missing number of occurrences")
} else {
	for (let index = 0; index < Number(process.argv[2]); index++) {
		console.log("C is fun")		
	}
}
