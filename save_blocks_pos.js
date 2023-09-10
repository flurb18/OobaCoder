function save_blocks_pos(blocksJSON) {
    var blocks_dict = JSON.parse(blocksJSON);
    for (let block_id in blocks_dict) {
        var elmnt = document.getElementById(block_id);
        blocks_dict[block_id]['x'] = elmnt.style.left;
        blocks_dict[block_id]['y'] = elmnt.style.top;
    }
    console.log(JSON.stringify(blocks_dict));
    return JSON.stringify(blocks_dict);
}