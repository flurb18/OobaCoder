function process_blocks(blocksJSON) {
  asdfasdfasdfasdf
  const blocks_dict = JSON.parse(blocksJSON);

  for (let block_id in blocks_dict) {
    setElementPosition(block_id, blocks_dict[block_id]['x'], blocks_dict[block_id]['y'])
    makeElementDraggable(block_id);
  }

  function setElementPosition(elementId, x, y) {
    var elmnt = document.getElementById(elementId);
    elmnt.style.left = x+"px";
    elmnt.style.top = y+"px";
  }
  
  function makeElementDraggable(elementId) {
    var elmnt = document.getElementById(elementId);
    var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
    var minx = elmnt.parentNode.style.left;
    var miny = elmnt.parentNode.style.top;
    if (document.getElementById(elementId + "header")) {
      // if present, the header is where you move the DIV from:
      document.getElementById(elementId + "header").onmousedown = dragMouseDown;
    } else {
      // otherwise, move the DIV from anywhere inside the DIV:
      elmnt.onmousedown = dragMouseDown;
    }
  
    function dragMouseDown(e) {
      e.preventDefault();
      // get the mouse cursor position at startup:
      pos3 = e.clientX;
      pos4 = e.clientY;
      document.onmouseup = closeDragElement;
      // call a function whenever the cursor moves:
      document.onmousemove = elementDrag;
    }
  
    function elementDrag(e) {
      e.preventDefault();
      // calculate the new cursor position:
      pos1 = pos3 - e.clientX;
      pos2 = pos4 - e.clientY;
      pos3 = e.clientX;
      pos4 = e.clientY;
      // set the element's new position:
      elmnt.style.top = Math.max(elmnt.offsetTop - pos2, miny) + "px";
      elmnt.style.left = Math.max(elmnt.offsetLeft - pos1, minx) + "px";
    }
  
    function closeDragElement() {
      // stop moving when mouse button is released:
      document.onmouseup = null;
      document.onmousemove = null;
    }
  }
}

