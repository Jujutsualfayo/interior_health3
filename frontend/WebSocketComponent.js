import React, { useEffect, useState } from 'react';

function WebSocketComponent() {
  const [message, setMessage] = useState('');
  const [socket, setSocket] = useState(null);

  useEffect(() => {
    const webSocket = new WebSocket('wss://cuddly-funicular-4jjv5xg9p7vg35xg5-3000.app.github.dev:3000/ws');

    webSocket.onopen = () => {
      console.log('WebSocket is open now.');
    };

    webSocket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      console.log('Received:', data);
      setMessage(data.message);
    };

    webSocket.onerror = (error) => {
      console.error('WebSocket error:', error);
    };

    webSocket.onclose = () => {
      console.log('WebSocket is closed now.');
    };

    setSocket(webSocket);

    return () => {
      webSocket.close();
    };
  }, []);

  return (
    <div>
      <h1>WebSocket Message: {message}</h1>
    </div>
  );
}

export default WebSocketComponent;
