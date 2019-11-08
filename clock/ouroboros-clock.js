// variables
let snek;
let snek1;
let snek2;
let snek3;

// setting up the canvas, ticking based on degrees and not radians
function setup() {
  createCanvas(800, 800);
  angleMode(DEGREES);

}
// loading ouroboros images; snek is the plain white version
//   https://p5js.org/reference/#/p5/loadImage
// image labelled for reuse, obtained from - 
//   https://commons.wikimedia.org/wiki/File:Ouroboros-benzene.svg
function preload() {
  snek = loadImage('snek.png');
  snek1 = loadImage('snek1.png');
  snek2 = loadImage('snek2.png');
  snek3 = loadImage('snek3.png');
}

// violet background
function draw() {
  background(88, 40, 98);

  
// for troubleshooting snake rotation
// borrowed from Zach Whalen's sketch -
//   https://editor.p5js.org/zachwhalen/sketches/kI0ED0Q6b
// text(year() + " : " + hour() + ":" + minute() + ":" + second(), 20, 20);


// concentric ticking ouroboros
// move snakes to center of canvas
//   https://p5js.org/reference/#/p5/imageMode
  imageMode(CENTER);
// translate origin of canvas
//   https://p5js.org/reference/#/p5/translate  
  translate(width / 2, height / 2);

  
// rotation adapted from:
// Zach Whalen's sketch - 
//   https://editor.p5js.org/zachwhalen/sketches/BPpajoLHY
// examinaton of "ticking" code element -
//   https://p5js.org/reference/#/p5/map
// I also consulted this p5.js example to troubleshoot and try to understand the way that clocks tick in p5.js - 
//   https://p5js.org/examples/input-clock.html
  
  
// ouroboros "ticking" once per second (innermost)
  let secondRot = map(second(), 0, 60, 0, 360);
  fill(0, 0, 0);
  rotate(secondRot);
  image(snek3, 0, 0, 150, 150);
  rotate(-secondRot);
  
// troubleshooting "ticking" by printing values to console
//   print(secondRot);
  
// ouroboros "ticking" once per minute (middle)
  let minuteRot = map(minute(), 0, 60, 0, 360);
  fill(0, 0, 0);
  rotate(minuteRot);
  image(snek2, 0, 0, 220, 220);
  rotate(-minuteRot);

// ouroboros "ticking" once per hour (outermost)
  let hourRot = map(hour(), 0, 12, 0, 360);
  fill(0, 0, 0);
  rotate(hourRot);
  image(snek1, 0, 0, 300, 300);
  rotate(-hourRot);
}
