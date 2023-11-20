var synthesis = window.speechSynthesis;

function sayIt(poem){
  if ('speechSynthesis' in window) {
    var utterance = new SpeechSynthesisUtterance(poem);
    synthesis.speak(utterance);
  } else {
    console.log('Text-to-speech not supported.');
  }
};