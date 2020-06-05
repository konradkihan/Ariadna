function read() {
    document.getElementById('wynik').innerHTML = '<iframe src="wynik.txt"></iframe>';
}

function handleFileSelect(evt) {
    var files = evt.target.files;
    var output = [];
    output.push('<li><strong>', escape(f.name), '</strong> (', f.type || 'n/a', ') - ',
        f.size, ' bytes, last modified: ',
        f.lastModifiedDate ? f.lastModifiedDate.toLocaleDateString() : 'n/a',
        '</li>');
    document.getElementById('list').innerHTML = output.join('');
}
