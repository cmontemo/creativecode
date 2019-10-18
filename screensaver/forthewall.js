// setting up variables
let counter = 0;
let blocks = new Array();

let eye;
let hed;
let head;

let x = 40;
let y = 0;
let x2 = window.innerWidth
let y2 = 0


// loads images
function preload() {
  eye = loadImage('eye.jpg');
  hed = loadImage('hed.png');
  head = loadImage('head.png');
}


// sets up background, canvas size that scales 
function setup() {
  background(0);
  createCanvas(window.innerWidth, window.innerHeight);
  image(eye,0,0);
  image(hed,10,10,200,267);
  image(head,155,70,300,400);
}


function draw() {
  
//drawing images on canvas
  //image(head, x2,y2,head.width/5, head.height/5);
  image(hed,10,10,200,267);
  image(head,155,70,300,400);
  
//adding text, used guide: https://p5js.org/reference/#/p5/text
textSize(50);
text('wake me up', 350, 200);
text('wake',80,300);
text('me',80,360);
text('up',80,420);
text('inside',80, 500);
  
textSize(150);
text('SAVE ME',350,400);
fill(200, 102, 153);
// textAlign(CENTER,CENTER);
  
//star array design by Zach Whalen: https://editor.p5js.org/zachwhalen/sketches/Ll6g4jb7- 
  if (counter % 5 == 0){
    blocks.push( new Block(random(0,width),random(0,height)) );
  }

  for (let s = 0; s < blocks.length; s++){
    blocks[s].draw();
  }
  
  counter += 1;
}

function Block(x,y){
   this.x = x;
   this.y = y;

   
//drawing blocks as 25x10 pixels
   this.draw = function (){
       fill(232,230,210);
       noStroke();
       rect(this.x,this.y,25,10);
   }
}
 


// The following are snippets of code that I tried to use in various ways.  I heep it here so that I can revisit it later and perhaps implement some of my ideas.


//making eyeball heads appear in array (instead of blocks), using Zach Whalen's star array example as a (attempted) starting point
// let heds = new Array();

// if (counter % 20 == 0){
// heds.push( new Hed(img(random (0,width),random(0,height)))  )
// }

// for (let s = 0; s < heds.length; s++){
//   heds[s].draw();
// }

// function Hed(img,x,y)
//   this.x = x;
//   this.y = y;

// this.draw = function (){
//   image(this.x, this.y, 150, 200);
//      }


   
// from random color squares by ivymeadows: https://editor.p5js.org/ivymeadows/sketches/S13gG2GhW; wanted to have randomly-placed blocks in random colors, need to figure out how to keep color static and not fluctuating
//     randomColor = color(random(255),random(255),random(255));
//     fill(randomColor);
//     noStroke();

     //}


// // mine - fills canvas full of aligned blocks
// function draw() {
//   background(220);
  
  // for (var x = 0; x <= width; x += 50){
  //   for (var y = 0; y <= height; y += 20)
  //   rect(x,y,50,20);
  //   fill(232,230,210)
//   }
// }


//part of my attempt at screenshot manipulation
//let extraCanvas;

// function setup() {
//   createCanvas(600,375);
//   img = loadImage('p5jsscreen-1.png');
//   //extraCanvas = createGraphics(400,400);
//   //extraCanvas.background(255);
// }

// function draw() {
//   background(0);
//   image(img, 0, 0);
//   fill(103,45,85,255);
//   ellipse(mouseX,mouseY,50,50);
// }
