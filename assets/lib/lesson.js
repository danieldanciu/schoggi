function replaceUmlauts(string)
{
  string = string.replace(/ä/g, 'ae');
  string = string.replace(/ö/g, 'oe');
  string = string.replace(/ü/g, 'ue');
  string = string.replace(/Ä/g, 'Ae');
  string = string.replace(/Ö/g, 'Oe');
  string = string.replace(/Ü/g, 'Ue');
  string = string.replace(' ', '');
  //string = string.replace('/', '-');
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

function onFileEnd() {
  var audio = document.getElementById('chd-wort');
  var audioFiles = audio.audioFiles;
  audio.currentFile++;
  if (audio.currentFile < audioFiles.length) {
    audio.src = '/laute/' +  replaceUmlauts(audioFiles[audio.currentFile]) + '.mp3';
    audio.pause();
    audio.load();
    audio.play();
  }
}

function playAudioAll(parent, audioFiles) {
	    var playButton = document.getElementById('play_all');
	    playButton.removeEventListener('click', playAudioAll);
	    playButton.addEventListener('click', stopPlayAudioAll);
		var audio = document.getElementById('chd-wort');
		audio.removeEventListener('ended', onFileEnd);
		audio.removeEventListener('error', onFileEnd);
		audio.currentFile = 0;
		audio.audioFiles = audioFiles;
		audio.src=''
		audio.addEventListener('ended', onFileEnd);
		audio.addEventListener('error', onFileEnd);
		audio.src = '/laute/' + replaceUmlauts(audioFiles[0]) + '.mp3';
		audio.play();
}

function stopPlayAudioAll() {
	var playButton = document.getElementById('play_all');
	playButton.removeEventListener('click', stopPlayAudioAll);
    playButton.addEventListener('click', playAudioAll);
    var audio = document.getElementById('chd-wort');
	audio.removeEventListener('ended', onFileEnd);
	audio.removeEventListener('error', onFileEnd);
}


