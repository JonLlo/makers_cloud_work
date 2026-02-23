// Create a pen

const pen = new Pen();

// Create some sheep

const dolly = new Sheep('dolly');
const molly = new Sheep('molly');

// Add Sheep to the Pen

pen.admit(dolly);
pen.admit(molly);

// Get the Sheep names

console.log(pen.sheepNames());
