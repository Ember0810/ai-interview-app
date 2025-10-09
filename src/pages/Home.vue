<template>
  <div>
    <a-button @click="startRecording">開始錄音</a-button>
    <a-button @click="stopRecording">停止錄音</a-button>
    <div>
      <h3>逐字稿</h3>
      <p>{{ transcript }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

let mediaRecorder;
let ws;
const transcript = ref('');

const startRecording = async () => {
  const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
  ws = new WebSocket('ws://localhost:8000/ws');
  ws.binaryType = 'arraybuffer';
  
  ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    transcript.value += data.text;
  };
  
  mediaRecorder = new MediaRecorder(stream, { mimeType: 'audio/webm' });
  mediaRecorder.ondataavailable = (e) => {
    if (ws.readyState === WebSocket.OPEN) {
      ws.send(e.data);
    }
  };
  
  mediaRecorder.start(500); // 每 500ms 產生一個 chunk
};

const stopRecording = () => {
  mediaRecorder.stop();
  ws.close();
};
</script>
