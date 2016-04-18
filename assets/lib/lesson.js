function replaceUmlauts(string)
{
    string = string.replace(/ä/g, 'ae');
    string = string.replace(/ö/g, 'oe');
    string = string.replace(/ü/g, 'ue');
     string = string.replace(/Ä/g, 'Ae');
    string = string.replace(/Ö/g, 'Oe');
    string = string.replace(/Ü/g, 'Ue');
    string = string.replace(' ', '');
     string = string.replace('/', '-');
    return string;
}

function playAudio(parent) {
  var audio = document.getElementById('chd-wort');
  audio.src = '/laute/' + replaceUmlauts(parent.id) + '.mp3';
  audio.play();
} 

function playAudioFile(parent, file) {
	  var audio = document.getElementById('chd-wort');
	  audio.src = '/laute/' + replaceUmlauts(file);
	  audio.play();
}

function playAudioAll(parent, audioFiles) {
		var audio = document.getElementById('chd-wort');
		audio.currentFile = 0;
		audio.addEventListener('ended',function(){
			audio.currentFile++;
			if (audio.currentFile < audioFiles.length) {
	          audio.src = '/laute/' +  replaceUmlauts(audioFiles[audio.currentFile]) + '.mp3';
	          audio.pause();
	          audio.load();
	          audio.play();
		    }
	    });
		audio.src = '/laute/' + replaceUmlauts(audioFiles[0]) + '.mp3';
		audio.play();
}


