#!/usr/bin/node
if (console.argv.length == 2){
	console.log('No argument');
}else if (console.argv.length == 3){
	console.log('Argument found');
}else{
	console.log('Arguments found');
}