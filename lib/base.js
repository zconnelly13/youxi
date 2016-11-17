/*
 * Settings
 */

SHOW_GRID = true;

function drawGrid() {
  cols = 6;
  width = @(WIDTH);
  height = @(HEIGHT);
  col_width = width / cols;
  ctx = getCtx();
  ctx.lineWidth = 1;

  /*
   * This is some nonsense where you have to give a value that ends
   * in ".5" for the canvas to not draw a line that is 2px thick...
   */
  function getDrawI(i) {
    drawI = parseInt(i)
    if (drawI >= i) {
      drawI -= 0.5
    }
    else if (drawI < i) {
      drawI += 0.5
    }
    return drawI
  }

  for (i=col_width;i<width;i+=col_width) {
    drawI = getDrawI(i);
    ctx.moveTo(drawI, 0);
    ctx.lineTo(drawI, height);
    ctx.stroke();
  }
  for (i=col_width; i<height; i+= col_width) {
    drawI = getDrawI(i)
    ctx.moveTo(0, drawI);
    ctx.lineTo(height, drawI);
    ctx.stroke();
  }
}

function getCanvas() {
  canvas = document.getElementById("canvas");
  return canvas
}

function getCtx() {
  return getCanvas().getContext("2d");
}

function main() {
  if (SHOW_GRID) {
    drawGrid();
  }
}

window.onload = main;
